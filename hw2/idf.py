import sys
reload(sys)
sys.setdefaultencoding( 'utf-8' )
from bs4 import BeautifulSoup
import requests
from weibo import APIClient
import webbrowser  # python
import csv
import codecs 

f = codecs.open('article.txt','r',encoding ='ascii',errors ='ignore')
article = f.read()
article = article.split('****************')

i = codecs.open('idf.txt','r',encoding ='ascii',errors ='ignore')
word = i.read()
word = word.split('\n')

output = []
for i in range(0,len(word)-1):
    output.append([])
    output[i].append(word[i])
    output[i].append(0)
    for j in range(0,len(article)):
        if article[j].find(word[i]) == -1:
            continue
        else:
            output[i][1] = output[i][1] + 1.0

sorted_output= sorted(output,key = lambda k:k[1], reverse = True)
for i in range(0,len(word)-1):
    print(word[i] + '\t' + str( sorted_output[i][1]/(len(article)-1) ))
