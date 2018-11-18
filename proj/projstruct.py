#-*- coding:utf-8 –*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import nltk
import jieba
import codecs 
from nltk import FreqDist
class node():
    """docstring for node"""
    def __init__(self, name,len):
        self.name = name
        self.qinmilist = []
        for i in range(0,len):
            self.qinmilist.append(0)
    def qinmi(self,num):
        self.qinmilist[num] += 1
listb = []
f = codecs.open('withoutstopwords.txt','r',encoding ='utf-8',errors ='ignore')
string = f.read()
lista = string.split('\n')
f.close()
for i in range(0,len(lista)):
    lista[i] = lista[i].split('\t')
    p = node(lista[i][0],len(lista))
    lista[i] = lista[i][0]
    listb.append(p)

g = open('java/java.csv','r')
stopwords=[]
cfp=open('stopwords.txt','r+')  
for line in cfp:
    for word in line.split():
        stopwords.append(word)
cfp.close()
# source = g.read()
# source = source.split('\n\n')
# for i in range(0,len(source)):
#     for j in range(0,len(lista)):
#         lista[j][0].qinmi(str(source[i]),lista)
line = g.readline()
while line: 
    if line != '\n':
        tokens = jieba.lcut(line)
        wordlist_N = []
        for word in tokens:
            if word not in stopwords:
                if word != '\n'  and word != '―' and word!=' ' and word!='\u200b' and word!='\n' and word!='##':
                    wordlist_N.append(word)

#generate a frequency dictionary for wordlist_N
        freq = FreqDist(wordlist_N)
        sorted_freq = sorted(freq.items(),key = lambda k:k[1], reverse = True)
#write result into .txt file
        # with open ('list2.txt','w+') as f:
        #     for line in freq:
        #         f.write(str(line[0])+'\t'+str(line[1])+'\n')
        for rline in sorted_freq:
            if str(rline[0]) in lista:
                num = lista.index(str(rline[0]))
                for i in range(0,len(listb)):
                    
                    if line.find(listb[i].name) != -1:
                        listb[i].qinmi(num)

    #print(line, end = '')　      # 在 Python 3 中使用 
    line = g.readline() 

g.close()
with open ('list.txt','w+') as f:
    f.write(str(len(lista))+'\n')
    for i in range(0,len(listb)):
        f.write(str(listb[i].name)+','+ str(listb[i].qinmilist) + '\n')