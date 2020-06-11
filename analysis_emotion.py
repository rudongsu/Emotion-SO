import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions, KeywordsOptions, EntitiesOptions

##
 ### open pre-processed plain text
 
#files = []
#for word in open('test.txt', encoding='utf-8'):
#    files.append(word.rstrip('\n'))

#plaintext = " ".join(
#  [str(item) 
#    for var in files 
#             for item in var])

#print('file loading done')
#print(len(plaintext))

##
 ### firing IBM natural language understanding cloud service 
 
authenticator = IAMAuthenticator('api')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('url')

response = natural_language_understanding.analyze(
#    text= plaintext,
    html = 'Flutter.html',
    features=Features(
        emotion=EmotionOptions(document=True),
        sentiment=SentimentOptions(document=True)
        ),
        language='en'
        ).get_result()
        
print('retrieving results from IBM .......')
print(json.dumps(response, indent=2))
