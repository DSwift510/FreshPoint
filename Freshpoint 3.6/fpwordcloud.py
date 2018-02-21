# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 01:29:21 2018

@author: Dasani
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import mysql.connector
import re


dbconnect = mysql.connector.connect(host='localhost',port='3309',database='ufoods',user='root',password='aggi3pride')
cursor = dbconnect.cursor(buffered=True)

results=""
textcloud=""
statement = "SELECT description FROM ufoods.complete_freshpoint;"
word_list = ('slice','diced','chopped','slices','chop','shred','sli','crushed','cuts','clipped','shredded','stemless','sliced','bagged','lioid','cut','spears','sdlss','seedless','clean','cleaned')
cursor.execute(statement)

description = cursor.fetchall()
#print (description)
text = str([x for x in description])
#print (text)
words = str([x for x in text.split("'")])
word = re.findall(r"[\w]+",words)

wc = [x for x in word]
for w in wc:
    results += " " + w
results = results[1:]    
    

pattern = re.compile('(' + '|'.join(word_list) + ')', re.IGNORECASE)
forcloud = pattern.findall(results)

for w in forcloud:
    textcloud += " " + w
textcloud = textcloud[1:]
print (textcloud)
word_cloud = WordCloud(collocations = False).generate(textcloud)
plt.figure(figsize=(16,8))
plt.imshow(word_cloud)
plt.axis("off")
plt.show()