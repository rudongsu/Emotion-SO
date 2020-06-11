from bs4 import BeautifulSoup
import lxml
import pandas as pd
import re
df = pd.read_csv('react-native.csv')

print(df.head())

#content = df['body'].tolist()

###
  ### read body as a single string
### 
content = df['body'].str.cat(sep=',')

print(len(content))

soup = BeautifulSoup(content, "lxml")

###
  ### remove any code snippets and HTML tags
### 
for tag in soup.find_all(['code', 'a', 'pre']):
    tag.decompose()

###
  ### remove common English stop words and non-alphanumeric characters
### 
text = soup.get_text(strip=True).replace("."," ").replace(","," ").replace("is "," ").replace("a "," ").replace("the "," ")

  ### remove digits
text = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", text)

#print(len(text))

  ### remove duplicate spaces
text = " ".join(text.split())
print(len(text))

#######################################################################################
 
  ### save output as text file, be sure encode as utf-8
### 
textfile = open('react-native.txt', 'w', encoding='utf-8')
textfile.write(text)
textfile.close()
