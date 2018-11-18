#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import nltk
import jieba
from nltk import FreqDist

#read file from local 
s = raw_input("job_name:")  
f = open("java/"+s+".csv","r")

raw = f.read()

#generate tokens by jieba
tokens = jieba.lcut(raw)

#load chinese stop words
stopwords=[]
cfp=open('stopwords.txt','r+')  
for line in cfp:
    for word in line.split():
        stopwords.append(word)
cfp.close()

# remove characters in chinese stop words
wordlist_N = []
for word in tokens:
    if word not in stopwords:
        if word != '\n'  and word != '―' and word!=' ' and word!='\u200b' and word!='\n' and word!='##':
            wordlist_N.append(word)

#generate a frequency dictionary for wordlist_N
freq = FreqDist(wordlist_N)

#sort the frequency list in descending order
sorted_freq = sorted(freq.items(),key = lambda k:k[1], reverse = True)

#write result into .txt file
with open ('withoutstopwords.txt','w+') as f:
    for line in sorted_freq:
        f.write(str(line[0])+'\t'+str(line[1])+'\n')
