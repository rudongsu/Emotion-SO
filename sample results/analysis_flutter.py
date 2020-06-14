import pandas as pd
import re
from bs4 import BeautifulSoup, Tag
import random
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions, KeywordsOptions, EntitiesOptions, SentimentOptions

## change the directory to your path
df = pd.read_csv('flutter.csv')

content = df['body'].tolist()

## select 100 random posts from the list without repeating
random_posts = random.sample(content, 100)

##  make it string
text_before_processing = ''.join(random_posts)
print(len(text_before_processing))

soup = BeautifulSoup(text_before_processing, "lxml")

### remove any code snippets and HTML tags
for tag in soup.find_all(['code', 'a', 'pre']):
    tag.decompose()

### remove common English stop words and non-alphanumeric characters
text = soup.get_text(strip=True).replace("."," ").replace(","," ").replace("is "," ").replace("a "," ").replace("the "," ")
print(len(text))

### remove digits
text = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", text)
print(len(text))

text_to_send =  " ".join(text.split())

print(len(text_to_send))

authenticator = IAMAuthenticator('API.key')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('url')

print('calling IBM server.....')

response = natural_language_understanding.analyze(
    text= text_to_send,
    #url='http://emotionanalysis.s3-website-ap-southeast-2.amazonaws.com/',
    features=Features(
        #entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
        emotion=EmotionOptions(document=True),
        sentiment=SentimentOptions(document=True)
        ),
        language='en',
        #return_analyzed_text = True
        ).get_result()
print('retrieving results from IBM .......')
print(json.dumps(response, indent=2))
