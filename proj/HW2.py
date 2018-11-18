#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import nltk
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import csv

corpus = []
for i in range(20):
    with open(str(i+1)+'.txt','r') as f:
        raw = f.read()
        raw = raw.replace('\n',' ')
        raw = raw.decode('utf8') 
        tokens = nltk.word_tokenize(raw)
        mystopwords = stopwords.words('english')
        words = [w.lower() for w in tokens if w.isalpha() if w.lower()not in mystopwords]
        porter = nltk.PorterStemmer()
        stem1 = [porter.stem(w) for w in words]
        words3 = [w.encode('utf8') for w in stem1]
        corpus.append(' '.join(words3))
vectorizer = CountVectorizer()
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
freq=[]
word = vectorizer.get_feature_names() 
weight = tfidf.toarray()             

for j in range(len(weight)):
    freq1 = []
    f2 = open('result'+str(j+1)+'.csv','w+')
    my_writer = csv.writer(f2)
    for k in range(len(word)):
        freq1.append((word[k],weight[j][k]))
        sorted_freq1 = sorted(freq1,key= lambda k:k[1], reverse = True)
        freq.append((word[k],weight[j][k])) #word and tf-idf without sorted
        for con1 in sorted_freq1:
            if con1[1] != 0:
                my_writer.writerow([con1[0],con1[1]])

    f2.close()
sorted_freq = sorted(freq,key= lambda k:k[1], reverse = True)
with open ('final_reslut.txt','w') as f3:
    for con in sorted_freq:
        f3.write(con[0]+'   '+str(con[1])+'\n')

for k in range(20):
    ff = open('r'+str(k+1)+'.txt','w')
    with open ('result'+str(k+1)+'.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        col = [row for row in reader]
        sorted_freq = sorted(col, key = lambda k:k[1], reverse = True)
        for (word,weight) in sorted_freq:
            ff.write(str(word)+'\t'+str(weight)+'\n')
    ff.close()
