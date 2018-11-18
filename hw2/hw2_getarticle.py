import sys
reload(sys)
sys.setdefaultencoding( 'utf-8' )
from bs4 import BeautifulSoup
import requests
from weibo import APIClient
import webbrowser  # python
import csv

cookie = '__cfduid=d598a1972671ede561a105c408bd21f151531386080; BMAID=7276311a-3c94-45fc-8544-22e29a02e2af; CoreID6=22356172561715313860926&ci=50200000|IBM_GlobalMarketing_52640000|IBM_GlobalMarketing; cvo_sid1=925XFBKWQ4EC; PHPSESSID=n87gld92fqaengem13l2684kd4; _pk_ses.4661.180e=*; cmTPSet=Y; notice_behavior=implied|eu; CMAVID=none; CoreM_State=58~-1~-1~-1~-1~3~3~5~3~3~7~7~|~~|~~|~~|~||||||~|~~|~~|~~|~~|~~|~~|~~|~; CoreM_State_Content=6~|~~|~|; _hjIncludedInSample=1; _pk_id.4661.180e=a9bfb6957d7c0948.1531386092.2.1531572929.1531572669.; OPTOUTMULTI=0:0%7Cc1:1%7Cc2:0%7Cc3:0; _uetsid=_uet2447a5b6; utag_main=v_id:01648db957310038213d29b8249c04069002506100bd0$_sn:2$_ss:0$_st:1531574729913$is_country_member_of_eu:false$dc_visit:2$ses_id:1531572668886%3Bexp-session$_pn:2%3Bexp-session$mm_sync:1%3Bexp-session$dc_event:2%3Bexp-session$dc_region:ap-northeast-1%3Bexp-session; cvo_tid1=AnhAUYtDy6M|1531386095|1531572930|0; 50200000_clogin=l=48429441531572669877&v=1&e=1531574731586; 52640000_clogin=l=23758451531572669882&v=1&e=1531574731592; __atuvc=3%7C28; __atuvs=5b49f1bcb867c134001'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0',
    'cookie': cookie
}
urls = 'http://newsroom.ibm.com/announcements?o='
review=[]  # create an empty list to store new reviews
getart = input("the number of pages(article/10) you want to get:")
jindu = 0
fenge = '****************'
#print soup.prettify()
for num in range(0,getart):
    url = urls + str(num) + '0' #get 3 pages of articles
    #print url
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    #print soup.prettify()
    #print num 
    for i in soup.find_all('div',{'class':'wd_title'}): #get each article's url
        url1 = (i.a).get('href')
        html1 = requests.get(url1, headers=headers).text
        soup1 = BeautifulSoup(html1, 'html.parser')
        #print soup1.prettify()
        for j in soup1.find_all('p'):
            e = j.get_text()  #get the main article
            review.append(e)
        review.append(fenge)
        jindu = jindu + 10.00/getart
        sys.stdout.write("\r" + str(round(jindu,1)) + "%")
        sys.stdout.flush()
sys.stdout.write("\rsuccessfully get " + str(getart*10) +" articles.\n")
sys.stdout.flush()
New_review=[]  # create an empty list to store new reviews
for each in review:
    new_each=each.replace(r':','') #remove ':' 
    #print new_each
    New_review.append(new_each)
#print New_review
#print len(New_review)

with open('article.txt','w+') as f:
    for each in New_review:
         f.write(each+'\n')  

