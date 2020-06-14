# Emotion-SO

This is the source code repo for my personal research on leveraging [IBM Watson Natural Language Understanding](https://cloud.ibm.com/catalog/services/natural-language-understanding) (NLU) for analysing developer's emotion of question posts in Stack Overflow targeting state-of-the-art cross-platform mobile development technologies: Flutter, React-native, angularjs, Cordova, Xamarin, ionic-framework and vue.js.  (Ideally, you can use the code to exploring any technical topic in Stack Overflow)

## Prerequisites

- Python (version 3.7 is recommended)
- An IBM Cloud account with NLU service: https://cloud.ibm.com/catalog/services/natural-language-understanding
- IBM Watson services Python library (https://github.com/watson-developer-cloud/python-sdk
), to install: `````pip install --upgrade ibm-watson`````

## Usage ##

- Run get_posts.sql on StackExchange data explorer: https://data.stackexchange.com/stackoverflow/query/new , Change the tag name when needed.  Alternatively, check https://drive.google.com/drive/folders/1Mc1vDUfF4UVdqSFLjfI8oynRg60aAzGH?usp=sharing for downloaded raw data and pre-processed data.
- Run pre_processing.py on downloaded csv file, change the file name for storing the results (e.g. 'flutter.txt')
- Run analysis_emotion.py on pre-processed file (e.g. 'flutter.txt'), replace the api and url with your own [credential](https://cloud.ibm.com/docs/cloud-object-storage/iam?topic=cloud-object-storage-service-credentials).

## Just wanna see the results? ##

- download 'flutter full.csv' from https://drive.google.com/drive/folders/1Mc1vDUfF4UVdqSFLjfI8oynRg60aAzGH?usp=sharing
- run sendRandomPosts.py on 'flutter full.csv', remember to change file path and replace the api and url with your own [credential](https://cloud.ibm.com/docs/cloud-object-storage/iam?topic=cloud-object-storage-service-credentials)
- check the printed results on the screen, you should get something like this one [sample results](https://github.com/rudongsu/Emotion-SO/blob/master/sample%20results/sample%20analysis%20result.txt)

## Built With

* [IBM Watson Nature Language Understanding](https://cloud.ibm.com/apidocs/natural-language-understanding) 
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 

## Authors

 **Rudong SU** : *rudongsu@gmail.com*

## Acknowledgments

* the project is taken as the main assignment in Research Methods in Software Engineering & Computer Science course during my Master of Software Engineering program at University of Adelaide.
