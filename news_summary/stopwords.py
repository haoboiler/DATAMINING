#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import nltk
import jieba
from nltk import FreqDist

###the article file name
filename = 'test_article.txt'

def read_files():
    f = open(filename,"r")
    lines = f.read()
    lines = lines.split('***')
   
    count = 0
    for line in lines:
        tokens = jieba.lcut(line)

        #load chinese stop words
        stopwords=[]
        cfp=open('stopwords.txt','r+')  
        for line in cfp:
            for word in line.split():
                stopwords.append(word)
        cfp.close()
        #append idf in sorted words
        cfp=open('idf.txt','r+')  
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
        with open ('data/keyword' + str(count) + '.txt','w') as g:
            word_num = 0
            for lines in sorted_freq:

                if word_num > 6:
                    break
                elif lines[1] < 3:
                    continue
                else:
                    g.write(str(lines[0])+'\t'+str(lines[1])+'\n')
                    word_num+=1
        g.close()
        count += 1
    f.close()

####calculate the word frequency for all files
def read_all(): 
    f = open(filename,"r")
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
    with open ('withoutstopwords.txt','w') as f:
        for line in sorted_freq:
            if line[1] > 5:
                f.write(str(line[0])+'\t'+str(line[1])+'\n')
    f.close()

##Calculate the tf_idf of the words
def tf_idf():
    #read files
    article = open(filename,'r')
    words = open('withoutstopwords.txt','r')
    #init the article list
    article_list = article.read().split('\n')
    word_list = words.read().split('\n')
    for i in range(len(word_list)):
        word_list[i] = [word_list[i].split('\t')[0],0.0]

    
    for j in range(len(article_list)):
        #count the appear number
        for i in range(len(word_list)):
            if article_list[j].find(word_list[i][0]) == -1:
                continue
            else:
                word_list[i][1] += 1.0/len(article_list)
    
    sort_idf= sorted(word_list,key = lambda k:k[1], reverse = True)
    with open ('idf.txt','w') as f:
        #choose the biggest idf word
        for i in range(0, 10):
            #f.write(str(sort_idf[i][0])+'\t'+str(sort_idf[i][1])+'\n')
            f.write(str(sort_idf[i][0] + '\n'))
    
    f.close()
    article.close()
    words.close()

if __name__ == '__main__':

    read_all()
    tf_idf()
    read_files()


