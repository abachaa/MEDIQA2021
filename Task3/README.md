
MEDIQA @ NAACL-BioNLP 2021 -- Task 3: Radiology Report Summarization 

https://sites.google.com/view/mediqa2021

Obtaining MIMIC Data
--------------

To obtain training data for this task, you'll need to first obtain access to the [MIMIC-CXR v2.0 dataset](https://physionet.org/content/mimic-cxr/2.0.0/). Note that since we are only using the radiology report text data, you do NOT need to download the entire MIMIC-CXR release. The only file you'll need to download from the MIMIC-CXR website is the compressed report file (`mimic-cxr-reports.zip`).

After obtaining the compressed report file (`mimic-cxr-reports.zip`), you can make summarization data with the scripts included in this repo. Our scripts will find report IDs that you will use for training and validation, extract and parse the report text from the zip file, and write the resulting data into json files. To do this, run:
```python
python make_mimic_data.py MIMIC_CXR_ZIP mimic_split_train_dev.csv \
    --train_file train.json
    --dev_file dev.json
```
where `MIMIC_CXR_ZIP` is the path to the compressed report zip file you should have downloaded. Feel free to replace the json file names to whatever you are comfortable with. Note that at this moment, you will only have training and development IDs. Example IDs for the test portion of the MIMIC dataset will be released in a later phase.

After successfully running the script, you should be able to see 91,544 total training examples in your `train.json` file, and 2,000 total development examples in your `dev.json` file. If you are seeing a different number, please check if your downloaded file is corrupted, and re-download if necessary.

Also note that it is a rule of this shared task that you are only allowed to use the reports in the resulting `train.json` file to train your summarization model. This is because we have reserved a portion of the rest of the reports in MIMIC-CXR for the purpose of validating your systems. It is therefore a violation of the rules of the shared task to train your system with other reports in MIMIC-CXR.

File Structures
--------------
The output json files will contain examples as a list of dictionary entries, with each entry having the following keys:
- `study_id`: the study ID of the particular radiology report (same as the original ID in MIMIC-CXR);
- `subject_id`: the unique (de-identified) ID of the patient that corresponds to this report;
- `findings`: the original human-written radiology findings text (input to summarization);
- `impression`: the human-written radiology impression text (output of summarization);
- `background`: background information of the study in text format (optional input to your system).

Note that in the test data distributed to registered participants via our [AIcrowd shared task page](https://www.aicrowd.com/challenges/mediqa-2021), the `impression` field will not be available, as this is expected to be test output from your system. See below for more information on the test data.

Validation Data
--------------
While the training data for this task is only from the MIMIC-CXR dataset as we have described above, we provide two validation datasets that come from two different institutes to help you validate your models. Apart from the same `MIMIC-CXR` development examples that can be generated following the above command, you can also see a `indiana_dev.json` file in the root directory, including another 2,000 dev examples from the [Open-i, or Indiana University radiology report dataset](https://openi.nlm.nih.gov/faq#collection).

Test Data
--------------
As part of the shared task, the test data will be distributed to registered participants via our [AIcrowd shared task page](https://www.aicrowd.com/challenges/mediqa-2021), upon the signing of a Data Usage Agreement that's available on the shared task page. The test data will consist of 600 total radiology reports, with 300 from the Indiana University dataset, and 300 from the Stanford University. Note that you are not allowed to share the test data with groups or people that did not sign the data usage agreement.

The test data will be distributed in the same format as the training and validation json files, except for the absence of a `impression` field, which is expected to be output by your system and submitted to AIcrowd for scoring. Please check out the AIcrowd page or our emails for more details on how the submission needs to be formatted.

Overall Statistics
--------------
As a summary, the information for our training, validation and test datasets is shown in the following table:

| Split | Number of Reports | Source Dataset |
| ---- | :----: | ---- |
| Training | 91,544 | MIMIC-CXR |
| Dev1 | 2,000 | MIMIC-CXR |
| Dev2 | 2,000 | Indiana University Dataset |
| Test | 600   | Indianna University (300) + Stanford University (300) |

As part of the shared task rules, we ask that you do not use other reports in the MIMIC-CXR or Indiana University dataset to train or validate your models.
