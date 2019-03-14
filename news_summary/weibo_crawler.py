import sys
reload(sys)
sys.setdefaultencoding( 'utf-8' )
from bs4 import BeautifulSoup
import requests
from weibo import APIClient
import webbrowser  # python
import csv
#cookie = 'BAIDUID=38D567D75EED64AB8631663BDECF37C2:FG=1; BIDUPSID=38D567D75EED64AB8631663BDECF37C2; PSTM=1521966750; BDUSS=lhzN1RXNmtTRkN5LUoyTTJFVzVpdmNjZUU0MW00bmJVTGtSMDRBMH5GbEtNRjFiQVFBQUFBJCQAAAAAAAAAAAEAAADkoZsrX19fX19f2LzBotX9AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEqjNVtKozVbM; MCITY=-289%3A; BD_UPN=123353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; delPer=0; BD_CK_SAM=1; PSINO=1; shifen[88648696309_94669]=1551427668; shifen[101944078167_14315]=1551427700; shifen[80487064858_64816]=1551427702; BCLID=7906015953098787299; BDSFRCVID=HaPOJeC62AcHohT9fyQguRprB2zRHNJTH6ao5Cx_Lh9YJwJzy6TNEG0PDU8g0Ku-fT5pogKK0eOTHkAF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJAqVIKhtCt3fP36q4rf-J0_-q30etJXf5bNLl7F5l8-hC3dW6850jFE2JQR-ljj-euHXfodBqcxOKQphpCaXxI8yPnW0x5x3GLq5qON3KJmjRL9bT3v5tj0-4Ke2-biWbR-2Mbd2hjP_IoG2Mn8M4bb3qOpBtQmJeTxoUtbWDFahKK6jTKBjTPW5ptX5toE2TTKX4K8Kb7Vbp6YXMnkbfJBD4Qq0h5xKJ5hXxjYbxo2ql_42l51XxI7yajK2-vtfgJJ04nYJRb0El3_ypjpQT8rMlAOK5Oib4jw3D_Xab3vOIJNXpO1MU_zBN5thURB2DkO-4bCWJ5TMl5jDh05y6TyjH8OtTkOf5vfL5r_24OofJvNq4bohjPn-J39BtQmJJrC3hnO2U-Be4ThbnoCKbDYDl6NBU6ZQg-q3RAa0-nr8bPwWf6byRI-jROw0x-jLgnPVn0MW-KVex-GK-nJyUnQbtnnBPnC3H8HL4nv2JcJbM5m3x6qLTKkQN3TJMIEK5r2SCKyJIDa3H; H_PS_645EC=fa6fFJrhCn5%2BpdbTAjklBQZfwW4gB9TDbBn6Z9ABGrukrA0c5uhRzb90nZ4; H_PS_PSSID=26525_1450_21087_28585_28558_28518_28414_22158; sugstore=0'
#cookie = 'SCF=AgCIp4c5XS8cemEbzp8ZSGoGSF-aHTlQQeJ9pRMgnkqDcIx8ccUySb9Ey8ZTU8bW2km71z-L2vyPmcyPIwZLA0A.; SUB=_2A25xfJNBDeRhGeVP4lMZ8i_OyzmIHXVSnj0JrDV6PUJbkdANLULukW1NTSbkCoSGqBaeb2C8Qmxiu0olmahwDQ5z; SUHB=0oU4AxGbMazgPD; SSOLoginState=1551426321; MLOGIN=1; _T_WM=89e3c2b0fff9ba45d2ec6c80c17cad88; WEIBOCN_FROM=1110006030; XSRF-TOKEN=b59ac8; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E4%25B8%25AD%25E5%259B%25BD%25E9%2587%2591%25E8%259E%258D%25E6%2596%25B0%25E9%2597%25BB%25E7%25BD%2591%26oid%3D4341023859400821%26fid%3D1005052699543161%26uicode%3D10000011'
headers = {
    #'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    #'cookie': cookie
}
#url1 = 'https://www.baidu.com/s?ie=UTF-8&wd=requests.get%20python'
#url1 = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%23DOTA2%23&sort=hot&page='
#url1 = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%23LOL%23&sort=hot&page='
#url1 = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%23LPL%23&sort=hot&page='
#url1 = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%23KPL%23&sort=hot&page='
#url1 = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%23KPL%23&sort=hot&page='
url1 = 'http://finance.eastmoney.com/a/cgnjj'
review=[]  # create an empty list to store new reviews

for i in range(1,24):
    #print i
    url = url1 + '_' + str(i) + '.html1'
    html = requests.get(url, headers=headers,verify=False).text
    #print html
    soup = BeautifulSoup(html, 'html.parser')
    for i in soup.find_all('div', {'class':'text text-no-img'}): #read the content
        #print i
        for j in i.find_all('a'):
            url2 = j.get('href') + '1'
            html2 = requests.get(url2,headers=headers).text
            soup2 =soup2 = BeautifulSoup(html2, 'html.parser') 
            #print soup2.prettify()
            g = soup2.find('div',{'class':'Body'})
            review.append(g.get_text())
    with open('article.txt','a') as f:
        for each in review:
            f.write(str(each)+'\n***\n')
    f.close()
    print('123')
    review = []        
        

#print review
#print len(review) 


# New_review=[]  # create an empty list to store new reviews
# for each in lastreview:
#     new_each=each.replace(r':','') #remove ':' 
#     print new_each
#     New_review.append(new_each)
# #print New_review
# print len(New_review)


