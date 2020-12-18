"""
Make summarization data from the original MIMIC-CXR release. This script requires:
    (1) the original compressed report file from the MIMIC-CXR v2.0 download; this file is named as 
        "mimic-cxr-reports.zip" in the original MIMIC-CXR package.
    (2) an official split file in CSV format as released by the MEDIQA 2021 shared task.
    (3) a separate `section_parser.py` script that can be found in the MEDIQA official repo.
    
The output will be written into json files at paths as specified by the arguments. The output json files
will contain examples as a list of dictionary entries, with each entry having the following keys:
    - study_id: the study ID of the particular radiology report;
    - subject_id: the unique (de-identified) ID of the patient that corresponds to this report;
    - findings: the original radiology findings text (input to summarization);
    - impression: the radiology impression text (output of summarization);
    - background: background information to the study in text format.

Usage:
    python make_mimic_data.py MIMIC_REPORT_ZIP SPLIT_FILE \
        --train_file TRAIN_FILE \
        --dev_file DEV_FILE \
        --test_file TEST_FILE

Authors:
    MEDIQA 2021 Organizers (https://sites.google.com/view/mediqa2021)
"""

import re
import argparse
import json
import csv
from collections import defaultdict
from zipfile import ZipFile

import section_parser as sp

def parse_args():
    parser = argparse.ArgumentParser("Make summarization data from the original MIMIC-CXR downloads.")
    parser.add_argument("mimic_report_zip", type=str, help="Path to the original compressed report file in the MIMIC-CXR release.")
    parser.add_argument("split_file", type=str, help="Path to the CSV file that contains the split information.")
    parser.add_argument("--train_file", type=str, help="Path to a file where the training data will be written to.")
    parser.add_argument("--dev_file", type=str, help="Path to a file where the dev data will be written to.")
    parser.add_argument("--test_file", type=str, help="Path to a file where the test data will be written to.")

    args = parser.parse_args()
    return args

def main():
    # read arguments
    args = parse_args()
    if all([x is None for x in (args.train_file, args.dev_file, args.test_file)]):
        raise Exception("At least one output file path must be specified with "
            "--train_file, --dev_file or --test_file.")
    
    # read the split file
    print(f"Reading the official split file from {args.split_file}...")
    split2ids, all_ids = read_split_file(args.split_file)
    print(f"Total entries found: {len(all_ids)}, including:")
    print(f"\ttrain = {len(split2ids['train'])}")
    print(f"\tdev = {len(split2ids['dev'])}")
    print(f"\ttest = {len(split2ids['test'])}")

    # extract reports
    print(f"\nExtracting and parsing the MIMIC-CXR reports from {args.mimic_report_zip}. This may take a while...")
    id2data = load_mimic_reports(args.mimic_report_zip, all_ids)
    print(f"Total reports extracted: {len(id2data)}")

    # write to output
    if args.train_file is not None and len(args.train_file) > 0:
        print(f"\nWriting training data to {args.train_file}...")
        write_split_to_json('train', split2ids, id2data, args.train_file)
    
    if args.dev_file is not None and len(args.dev_file) > 0:
        print(f"\nWriting dev data to {args.dev_file}...")
        write_split_to_json('dev', split2ids, id2data, args.dev_file)
    
    if args.test_file is not None and len(args.test_file) > 0:
        print(f"\nWriting test data to {args.test_file}...")
        write_split_to_json('test', split2ids, id2data, args.test_file)
    return

def load_mimic_reports(filename, all_ids):
    """ Load the MIMIC-CXR reports from the zip file, using a set of study and subject IDs.
    """
    if not filename.endswith('.zip'):
        raise Exception("Unrecognizable format; expecting a .zip file for the MIMIC reports.")
    
    # load and parse reports from file
    id2data = dict()
    with ZipFile(filename) as zfile:
        for study_id, subject_id in all_ids:
            fn = get_filename_from_ids(study_id, subject_id)
            # read from zipfile
            with zfile.open(fn, 'r') as infile:
                text = infile.read().decode('utf-8')
            
            # parse sections
            sections, section_names, section_idx = sp.section_text(text)
            findings = sections[section_names.index('findings')]
            impression = sections[section_names.index('impression')]
            
            findings_start = section_idx[section_names.index('findings')]
            background = text[:findings_start]

            findings = clean_findings(findings)
            impression = clean_impression(impression)
            background = clean_background(background)

            data = {
                'study_id': study_id,
                'subject_id': subject_id,
                'findings': findings,
                'impression': impression,
                'background': background
            }
            id2data[study_id] = data
    return id2data

def get_filename_from_ids(study_id, subject_id):
    """ Compose the filename in the zip file based on a study ID and a subject ID.
    The filename is in a format similar to: `files/p11/p11148901/s58832226.txt`.
    """
    filename = f"files/p{subject_id[:2]}/p{subject_id}/s{study_id}.txt"
    return filename

def read_split_file(filename):
    """ Read the official split data from the csv file.
    """
    if not filename.endswith('.csv'):
        raise Exception(f"Split file must be in .csv format, but found: {filename}")
    split2ids = defaultdict(list)
    all_ids = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            split = row['split']
            pair = (row['study_id'], row['subject_id'])
            split2ids[split].append(pair)
            all_ids.append(pair)
    return split2ids, all_ids

def write_split_to_json(split, split2ids, id2data, filename):
    """ Write the parsed reports of a particular split into a json file.
    """
    data = []
    ids = split2ids[split]
    if len(ids) == 0:
        print(f"No data is found for {split} split. Possible that the {split} split has not been released yet. Skipping...")
        return
    for study_id, subject_id in ids:
        data.append(id2data[study_id])
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)
    print(f"{len(data)} total examples written to file {filename}.")
    return

def clean_findings(text):
    """ Clean up the findings string.
    """
    text = text.strip().replace('\n', '')
    # reduce consecutive spaces
    text = re.sub(r'\s\s+', ' ', text)
    return text

def clean_impression(text):
    """ Clean up the impression string.
    This mainly removes bullet numbers for consistency.
    """
    text = text.strip().replace('\n', '')
    # remove bullet numbers
    text = re.sub(r'^[0-9]\.\s+', '', text)
    text = re.sub(r'\s[0-9]\.\s+', ' ', text)
    text = re.sub(r'\s\s+', ' ', text)
    return text

def clean_background(text):
    """ Clean up the background string.
    """
    text = text.strip()
    # remove common prefix title
    if text.startswith('FINAL REPORT'):
        text = text[12:].lstrip()
    # remove findings header
    if text.endswith(':'):
        idx = text.rfind(' ')
        text = text[:idx].rstrip()
    text = re.sub(r'\s\s+', ' ', text)
    text = text.strip().replace('\n', '')
    return text

if __name__ == "__main__":
    main()
