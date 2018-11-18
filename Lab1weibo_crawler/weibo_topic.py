import sys
reload(sys)
sys.setdefaultencoding( 'utf-8' )
from bs4 import BeautifulSoup
import requests
from weibo import APIClient
import webbrowser  # python
import csv

cookie = '_T_WM=b806bb881de8330b42334c27bb700865; ALF=1533577510; SCF=AgCIp4c5XS8cemEbzp8ZSGoGSF-aHTlQQeJ9pRMgnkqDcIx8ccUySb9Ey8ZTU8bW2km71z-L2vyPmcyPIwZLA0A.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFsGwwYZRi7-WSF1U9f6ThP5JpX5K-hUgL.Foep1K2Reo2Eeh-2dJLoI7DzqgvkqJvDdsHE; SUB=_2A252RWK0DeRhGeVP4lMZ8i_OyzmIHXVVxg78rDV6PUJbkdAKLUSskW1NTSbkCmVYBnaMMXXdidvHGiWZch_SLJSr; SUHB=0A0Z2OsqV42kWy; SSOLoginState=1530991332'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0',
    'cookie': cookie
}
#url1 = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%23TI8%23&sort=hot&page='
#url1 = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%23DOTA2%23&sort=hot&page='
#url1 = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%23LOL%23&sort=hot&page='
#url1 = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%23LPL%23&sort=hot&page='
#url1 = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%23KPL%23&sort=hot&page='
url1 = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%23KPL%23&sort=hot&page='
review=[]  # create an empty list to store new reviews
nextreview = [] # create an empty list to store new reviews
lastreview = []
for i in range(11,20):
    url = url1 + str(i+1)
    html = requests.get(url, headers=headers).text

    soup = BeautifulSoup(html, 'html.parser')
    print soup.prettify()
    for i in soup.find_all('a',{'class':'nk'}):
        url2 = i.get('href')  #get the url of this people's homepage
        html2 = requests.get(url2,headers=headers).text
        soup2 = BeautifulSoup(html2, 'html.parser') 
        #print soup2.prettify()
        g = soup2.find('span',{'class':'ctt'}).text #get the name and place
        list2 = g.split()
        e = list2[0] + "," + list2[1][2:]
        #print e
        #print i.get_text()    
        review.append(e)
    flag = 0
    for i in soup.find_all('a', {'class':'cc'}): #read the number of comments
        j = i.get_text()
        m = review[flag] + "," + j[3:-1]
        flag = flag + 1
        #print m;
        nextreview.append(m)
    flag = 0
    for i in soup.find_all('span', {'class':'ctt'}): #read the content
        #print i.get_text()
        n = nextreview[flag] + "," + i.get_text()
        flag = flag + 1
        #print n;
        lastreview.append(n)
    review = [] #empty the review
    nextreview = []  
#print review
#print len(review) 


New_review=[]  # create an empty list to store new reviews
for each in lastreview:
    new_each=each.replace(r':','') #remove ':' 
    print new_each
    New_review.append(new_each)
#print New_review
print len(New_review)

with open('article.txt','a') as f:
    for each in New_review:
         f.write(each+'\n')  

