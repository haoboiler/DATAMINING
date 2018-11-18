import nltk
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.text import TextCollection
#read file from local 
f = open('article.txt','rU')
raw = f.read()

raw = raw.replace('\n',' ') 
raw = raw.decode('utf8') #decode raw text by utf-8

tokens = nltk.word_tokenize(raw)
#change all tokens into lower case 
words1 = [w.lower() for w in tokens]   #list comprehension 
#only keep text words, no numbers 
words2 = [w for w in words1 if w.isalpha()]

stopwords = stopwords.words('english') #use the NLTK stopwords

#only keep the words that not in nltk stopwords word list
words_nostopwords = [w for w in words2 if w not in stopwords]
#generate a frequency dictionary for all tokens 
#freq_nostw = FreqDist(words_nostopwords)
#sort the frequency list in decending order
porter = nltk.PorterStemmer()
stem1 = [porter.stem(w) for w in words_nostopwords]
#Encode with utf-8
stem1 = [w.encode('utf8') for w in stem1]
#Get the frequency distribution 
freq1 = FreqDist(stem1)


sorted_freq1 = sorted(freq1.items(),key = lambda k:k[1], reverse = True)

#write result into .txt file
with open ('step2.txt','w+') as outfile:
    for line in sorted_freq1:
        if line[1] > 10:
            outfile.write(str(line[0])+'\t'+str(line[1]) +'\n')
