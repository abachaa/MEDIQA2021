# MEDIQA2021

The second edition of the MEDIQA challenge will be organized at NAACL-BioNLP 2021 and will focus on summarization in the medical domain with three tasks: 
Consumer health question summarization, Multi-answer summarization, and Radiology report summarization. 

- Website: https://sites.google.com/view/mediqa2021

- Paper: https://www.aclweb.org/anthology/2021.bionlp-1.8.pdf 

- Post-challenge Round: https://www.aicrowd.com/challenges/mediqa-2021 

- Mailing list: https://groups.google.com/forum/#!forum/bionlp-mediqa

- Previous edition: https://sites.google.com/view/mediqa2019 & https://github.com/abachaa/MEDIQA2019 

Tasks & Datasets: 
-------
Task 1 (question summarization): https://github.com/abachaa/MEDIQA2021/tree/main/Task1

Task 2 (multi-answer summarization): https://github.com/abachaa/MEDIQA2021/tree/main/Task2

Task 3 (radiology report summarization): https://github.com/abachaa/MEDIQA2021/tree/main/Task3


Evaluation: 
------------------
- The [AIcrowd platform](https://www.aicrowd.com/challenges/mediqa-2021) will be used for releasing the test sets and submitting runs. 

- [ROUGE](https://www.aclweb.org/anthology/W04-1013.pdf) will be used as the main metric to rank the participating teams, but we will also use several evaluation metrics more adapted to each task such as [HOLMS](https://www.aclweb.org/anthology/2020.coling-main.498.pdf) and [CheXbert](https://arxiv.org/pdf/2004.09167.pdf).   


Registration:
-------------
The registration & data usage agreement form is available under the Resources section of the [AIcrowd projects](https://www.aicrowd.com/challenges/mediqa-2021).
The form covers the three tasks. You can download it from any of the three MEDIQA projects: [QS@AIcrowd](https://www.aicrowd.com/challenges/mediqa-2021/problems/mediqa-2021-question-summarization-qs), [MAS@AIcrowd](https://www.aicrowd.com/challenges/mediqa-2021/problems/mediqa-2021-multi-answer-summarization) & [RRS@AIcrowd](https://www.aicrowd.com/challenges/mediqa-2021/problems/mediqa-2021-radiology-report-summarization).   
To register, you need to complete, sign, and upload the form. When approved, you will be able to download the official test sets and to submit your runs on the AIcrowd submission systems. 


## <h2>License:</h2>
- The MEDIQA 2021 datasets are released under the Creative Commons Attribution 4.0 International License ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)). If you use any of these datasets, please cite our paper:  

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


Organizers: 
------------

- Asma Ben Abacha, NLM/NIH
- Chaitanya Shivade, Amazon
- Yassine Mrabet, NLM/NIH
- Yuhao Zhang, Stanford University
- Curtis Langlotz, Stanford University
- Dina Demner-Fushman, NLM/NIH 
