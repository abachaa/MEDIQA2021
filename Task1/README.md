MEDIQA @ NAACL-BioNLP 2021 -- Task 1: Consumer Health Question Summarization (MEDIQA-QS)

https://sites.google.com/view/mediqa2021

## <h2> MEDIQA-QS Dataset </h2> 

**Training Data**

The [MeQSum Dataset](https://github.com/abachaa/MeQSum) of consumer health questions and their summaries could be used for training. 

Participants can use available external resources, including, but not limited to [medical QA datasets](https://github.com/abachaa/Existing-Medical-QA-Datasets) and question focus & type recognition datasets. 

For instance, the [CHQs Dataset](https://bmcbioinformatics.biomedcentral.com/track/pdf/10.1186/s12859-018-2045-1.pdf?site=bmcbioinformatics.biomedcentral.com) contains additional annotations (e.g. medical entities, question focus, question type, keywords) of the MeQSum questions.  

**Validation and test sets** 

Consist of consumer health questions received by the U.S. National Library of Medicine (NLM) in December 2020 and their associated summaries, manually created by medical experts. 

- The **validation set** is available [here](https://github.com/abachaa/MEDIQA2021/blob/main/Task1/MEDIQA2021-Task1-QuestionSummarization-ValidationSet.xlsx). It contains 50 NLM questions and their summaries. We also provided additional information (question focus and type) with the summaries. 

- Please note that in the official test set, we will **not provide** the question focus and type for the test questions. Also, the **test questions** of the Question Summarization and Answer Summarization tasks will be different.  

- The **test set** is available [here](https://github.com/abachaa/MEDIQA2021/blob/main/Task1/MEDIQA2021-Task1-TestSet-ReferenceSummaries.xlsx). It contains 100 consumer health questions and their reference summaries.  


## <h2>License</h2>
- The MEDIQA-QS dataset is published under a Creative Commons Attribution 4.0 International License ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)). Please cite our paper: 

         @inproceedings{mediqa-2021,
          title = "Overview of the {MEDIQA} 2021 Shared Task on Summarization in the Medical Domain",
          author = "Ben Abacha, Asma  and
          Mrabet, Yassine  and
          Zhang, Yuhao  and
          Shivade, Chaitanya  and
          Langlotz, Curtis  and
          Demner-Fushman, Dina",
         booktitle = "Proceedings of the 20th Workshop on Biomedical Language Processing",
        month = jun,
        year = "2021",
        publisher = "Association for Computational Linguistics",
        url = "https://aclanthology.org/2021.bionlp-1.8/",
        pages = "74--85",
        abstract = "The MEDIQA 2021 shared tasks at the BioNLP 2021 workshop addressed three tasks on summarization for medical text: (i) a question summarization task aimed at exploring new approaches to understanding complex real-world consumer health queries, (ii) a multi-answer summarization task that targeted aggregation of multiple relevant answers to a biomedical question into one concise and relevant answer, and (iii) a radiology report summarization task addressing the development of clinically relevant impressions from radiology report findings. Thirty-five teams participated in these shared tasks with sixteen working notes submitted (fifteen accepted) describing a wide variety of models developed and tested on the shared and external datasets. In this paper, we describe the tasks, the datasets, the models and techniques developed by various teams, the results of the evaluation, and a study of correlations among various summarization evaluation measures. We hope that these shared tasks will bring new research and insights in biomedical text summarization and evaluation."
        }
