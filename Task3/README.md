
MEDIQA @ NAACL-BioNLP 2021 -- Task 3: Radiology Report Summarization 

https://sites.google.com/view/mediqa2021

Obtaining Data
--------------

To obtain training data for this task, you'll need to first obtain access to the [MIMIC-CXR v2.0 dataset](https://physionet.org/content/mimic-cxr/2.0.0/). Note that since we are only using the radiology report text data, you do NOT need to download the entire MIMIC-CXR release. The only file you'll need to download from the MIMIC-CXR website is the compressed report file (`mimic-cxr-reports.zip`).

After obtaining the compressed report file (`mimic-cxr-reports.zip`), you can make summarization data with the scripts included in this repo. Our scripts will find report IDs that you will use for training and validation, extract and parse the report text from the zip file, and write the resulting data into json files. To do this, run:
```python
python make_mimic_data.py MIMIC_CXR_ZIP mimic_split_train_only.csv \
    --train_file train.json
    --dev_file dev.json
```
where `MIMIC_CXR_ZIP` is the path to the compressed report zip file you should have downloaded. Feel free to replace the json file names to whatever you are comfortable with. Note that in the initial release of the task, you will only have training IDs, therefore you will only see a `train.json` after running the above command. You can rerun this script to generate the validation (dev) data after we release them in a later phase.

After successfully running the script, you should be able to see 91,544 total training examples in your `train.json` file. If you are seeing a different number, please check if your downloaded file is corrupted, and re-download if necessary.

Also note that it is a rule of this shared task that you are only allowed to use the reports in the resulting `train.json` file to train your summarization model. This is because we have reserved a portion of the rest of the reports in MIMIC-CXR for the purpose of testing your systems. It is therefore a violation of the rules to train your system with other reports in MIMIC-CXR.

File Structures
--------------
The output json files will contain examples as a list of dictionary entries, with each entry having the following keys:
- `study_id`: the study ID of the particular radiology report (same as the original ID in MIMIC-CXR);
- `subject_id`: the unique (de-identified) ID of the patient that corresponds to this report;
- `findings`: the original human-written radiology findings text (input to summarization);
- `impression`: the human-written radiology impression text (output of summarization);
- `background`: background information of the study in text format (optional input to your system).
