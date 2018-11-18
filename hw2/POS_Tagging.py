import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import nltk 
import codecs 
from nltk.corpus import stopwords
from nltk import FreqDist

f = codecs.open('article.txt','r',encoding ='ascii',errors ='ignore')
raw = f.read()
raw = raw.replace('\n',' ')
raw = raw.replace('@',' ')
raw = raw.replace('IBM',' ')
raw = raw.replace('SOURCE  IBM',' ')
raw = raw.replace('%',' ')
raw = raw.replace('****************',' ')
raw = raw.replace('data',' ')
raw = raw.replace('Health',' ')
raw = raw.replace('Cloud',' ')
raw = raw.replace('Watson',' ')
raw = raw.replace('business',' ')
#Tokenization
tokens = nltk.word_tokenize(raw)


#POS Tagging
POS_tags = nltk.pos_tag(tokens) #use unprocessed 'tokens', not 'words'

#Generate a list of POS tags
POS_tag_list = [(word,tag) for (word,tag) in POS_tags if tag.startswith('N')]

#Generate a frequency distribution of all the POS tags
tag_freq = nltk.FreqDist(POS_tag_list)
#Sort the result 
sorted_tag_freq = sorted(tag_freq.items(), key = lambda k:k[1], reverse = True)

#write result into .txt file
with open('step4.txt','w+') as f:
    for (word,tag),frequency in sorted_tag_freq:
        if frequency > 10:
            f.write(str(word)+'\t'+str(tag)+'\t'+str(frequency)+'\n')
