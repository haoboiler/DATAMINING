 #!usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( 'utf-8' )
from bs4 import BeautifulSoup
import requests
import re
import os
import csv

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print "new folder"
    else:
        print "folder exit"


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'
}
url1 = 'https://search.51job.com/list/000000,000000,0000,00,9,99,'
job_name = 'java'  #可换成list存职位
param = ',2,'
url_tail = '.html'

file_path = job_name   # if change job_name changed to list, this should be changed
mkdir(file_path)  
f = open(file_path+"/"+job_name+".csv","w")
writer = csv.writer(f)
csv_header = ['job_name','location','salary','job_request']
writer.writerow(csv_header)
for page_num in range(1,20):
    url = url1+job_name+param+str(page_num) + url_tail

    html = requests.get(url, headers=headers).text.encode("iso-8859-1").decode('gbk').encode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    # to get job_link, location, salary
    divs = soup.find_all('div',{'class':'el'})

    for item in divs:
        job_link = item.find('p',{'class':'t1 '})
        if (job_link==None):
            continue

        job_link = job_link.find('a')
        job_title = job_link['title']

        job_link = job_link['href']

        job_html = requests.get(job_link,headers=headers).text.encode("iso-8859-1").decode('gbk').encode('utf8')
        job_soup = BeautifulSoup(job_html,'html.parser')

        job_msg = job_soup.find('div',{'class':"bmsg job_msg inbox"})
        [s.extract() for s in job_msg('div')]  # to filter some gargage imformation
        location = item.find('span',{'class':'t3'}).get_text()

        salary = item.find('span',{'class':'t4'}).get_text()

        data = [job_title,location,str(salary),job_msg.get_text()]
        writer.writerow(data)

f.close()
