"""
Make summarization data from the original MIMIC-CXR downloads. This script requires:
    (1) the original sectioned file from the MIMIC-CXR v2.0 download; this file is named as 
        "mimic_cxr_sectioned.csv.gz" in the original MIMIC-CXR package.
    (2) an official split file in CSV format as released by the MEDIQA 2021 shared task.
    
The output will be written into json files at paths as specified by the arguments. The output json files
will contain examples as a list of dictionary entries, with each entry having the following keys:
    - study_id: the study ID of the particular radiology report;
    - subject_id: the unique (de-identified) ID of the patient that corresponds to this report;
    - findings: the original radiology findings text (input to summarization);
    - impression: the radiology impression text (output of summarization);
    - background: background information to the study in text format.

Usage:
    python make_mimic_data.py MIMIC_SECTIONED_FILE SPLIT_FILE \
        --train_file TRAIN_FILE \
        --dev_file DEV_FILE \
        --test_file TEST_FILE
"""

import argparse
import gzip
import json
import csv
from collections import defaultdict

def parse_args():
    parser = argparse.ArgumentParser("Make summarization data from the original MIMIC-CXR downloads.")
    parser.add_argument("mimic_sectioned_file", type=str, help="Path to the original sectioned file in the MIMIC-CXR download.")
    parser.add_argument("split_file", type=str, help="Path to the CSV file that contains the split information.")
    parser.add_argument("--train_file", type=str, help="Path to a file where the training data will be written to.")
    parser.add_argument("--dev_file", type=str, help="Path to a file where the dev data will be written to.")
    parser.add_argument("--test_file", type=str, help="Path to a file where the test data will be written to.")

    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    if all([x is None for x in (args.train_file, args.dev_file, args.test_file)]):
        raise Exception("At least one output file path must be specified with "
            "--train_file, --dev_file or --test_file.")
    
    print(f"Reading the MIMIC-CXR sectioned file from {args.mimic_sectioned_file}...")
    id2data = read_sectioned_file(args.mimic_sectioned_file)
    
    print(f"Reading the official split file from {args.split_file}...")
    split2ids, total = read_split_file(args.split_file)
    print(f"Total entries found: {total}, including:")
    print(f"\ttrain = {len(split2ids['train'])}")
    print(f"\tdev = {len(split2ids['dev'])}")
    print(f"\ttest = {len(split2ids['test'])}")
    print("")

    # write to output
    if args.train_file is not None and len(args.train_file) > 0:
        print(f"Writing training data to file at {args.train_file}...")
        write_to_json('train', split2ids, id2data, args.train_file)
    
    if args.dev_file is not None and len(args.dev_file) > 0:
        print(f"Writing dev data to file at {args.dev_file}...")
        write_to_json('dev', split2ids, id2data, args.dev_file)
    
    if args.test_file is not None and len(args.test_file) > 0:
        print(f"Writing test data to file at {args.test_file}...")
        write_to_json('test', split2ids, id2data, args.test_file)
    return

def read_sectioned_file(filename):
    """ Read the original MIMIC-CXR sectioned file. """
    # decide file opener
    open_func = None
    if filename.endswith('.csv.gz'):
        open_func = lambda fn: gzip.open(fn, 'rt')
    elif filename.endswith('.csv'):
        open_func = lambda fn: open(fn, 'r')
    else:
        raise Exception("Unrecognizable format of the MIMIC-CXR sectioned file. "
            "Must be either a .csv file or a .csv.gz file.")
    
    # load from file
    id2data = dict()
    with open_func(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            study = row['study']
            id2data[study] = row
    return id2data

def read_split_file(filename):
    """ Read the official split file. """
    if not filename.endswith('.csv'):
        raise Exception(f"Split file must be in .csv format, but found: {filename}")
    split2ids = defaultdict(list)
    total = 0
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            split = row['split']
            split2ids[split].append((row['study_id'], row['subject_id']))
            total +=1 
    return split2ids, total

def write_to_json(split, split2ids, id2data, filename):
    data = []
    ids = split2ids[split]
    if len(ids) == 0:
        print(f"No id is found for {split} split. Skipping...")
        return
    for study_id, subject_id in ids:
        entry = {'study_id': study_id, 'subject_id': subject_id}
        report = id2data[study_id]
        entry['findings'] = report['findings'].replace('\n', '')
        entry['impression'] = report['impression'].replace('\n', '')
        entry['background'] = report['comparison'].replace('\n', '')
        data.append(entry)
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)
    print(f"{len(data)} total examples written to file {filename}.")
    return

if __name__ == "__main__":
    main()