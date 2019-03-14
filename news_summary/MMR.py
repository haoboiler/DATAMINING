# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import re
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import operator

###global weight 
weight = 1
#0. read stopwords from file
stopwords=[]
cfp=open('stopwords.txt','r+')  
for line in cfp:
    for word in line.split():
        stopwords.append(word)
cfp.close()

 # 1.read the key words from file
f = open('data/keyword2.txt')
lines = f.read()
keywords = lines.split('\n')
for i in range(0,len(keywords)):
    keywords[i] = keywords[i].split('\t')[0]


# remove stopwords
def cleanData(name):
    setlast = jieba.lcut(name)
    wordlist_N = []
    for word in setlast:
        if word not in stopwords:
            if word != '\n'  and word != '―' and word!=' ' and word!='\u200b'  and word!='##':
                wordlist_N.append(word)
    return " ".join(wordlist_N)
 
#calculate the similarity between sentences and sentences
def calculateSimilarity(sentence, doc):
    if doc == []:
        return 0

    vocab = {}
    for word in sentence.split():
        vocab[word] = 0
    
    docInOneSentence = '';
    for t in doc:
        docInOneSentence += (t + ' ')
        for word in t.split():
            vocab[word]=0   
    
    cv = CountVectorizer(vocabulary=vocab.keys())
 
    docVector = cv.fit_transform([docInOneSentence])
    sentenceVector = cv.fit_transform([sentence])
    return cosine_similarity(docVector, sentenceVector)[0][0]

#calculate the similarity between the key words and sentence
def calculatesimi(sentence, sentences_length): 
    word_score = 0.0
    vocab = sentence.split()

    for word in vocab:
        if word in keywords:
            #print word
            word_score += 1.0/(len(vocab)+ int(sentences_length/5)) #add 5 for the short sentences
    
    return word_score * weight

if __name__ == '__main__':

    data=open("single_article.txt", 'r')
    texts = data.readlines()
    texts=[i[:-1] if i[-1]=='\n' else i for i in texts] 
    
    sentences_length = 0
    clean = []
    original_Sentence = {}


    #2.Data cleansing
    for line in texts:
        sentences = re.split('。|！|？',line)[:-1] #split the lines

        for sentence in sentences:
            clean_sentence = cleanData(sentence)
            sentences_length +=1 
            clean.append(clean_sentence) 
            original_Sentence[clean_sentence] = sentence 
    
    setClean = set(clean) 

    #3.calculate Similarity score each sentence with whole documents 

    scores = {}
    for data in clean:

        temp_doc = setClean - set([data])
        score = calculateSimilarity(data, list(temp_doc))
        scores[data] = score

     
     
    #calculate MMR
    n = 20 * sentences_length / 100 #摘要的比例大小
    if n > 5:
        n = 5
    alpha = 0.7
    summarySet = []

    while n > 0:
        mmr = {}
        for sentence in scores.keys():
            if not sentence in summarySet:
                mmr[sentence] = alpha * scores[sentence] - (1-alpha) * (calculateSimilarity(sentence, summarySet)) + calculatesimi(sentence,sentences_length)   
                print calculatesimi(sentence,sentences_length)
                print mmr[sentence]
        selected = max(mmr.items(), key=operator.itemgetter(1))[0]  #sort by the score
        summarySet.append(selected)
    #   print (summarySet)
        n -= 1
     

        
    print ('Summary:\n')
    for sentence in summarySet:
        print (original_Sentence[sentence].lstrip(' '))
    print ('\nOriginal Passages:\n')
