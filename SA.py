import csv
import re
from textblob import TextBlob
data=open("data.csv",'r')
file=csv.DictReader(data)
text=[]
sentiment=[]

for col in file:
    text.append(col['review'])
    sentiment.append(col['sentiment'])
print(len(text))
for i in text:
    i=i.casefold()
for i in text:
        # i=demojize(i)
        i=i.lower()
        i=i.casefold()
        i=" ".join([w for w in i.split() if w.isalnum()])
        i= " ".join([w for w in i.split() if w.isalpha()])
        i= re.sub(r"[^A-Za-z0-9\s]+", "",i)
print(text)
print(sentiment)
