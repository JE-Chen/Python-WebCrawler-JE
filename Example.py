import requests
import random
from bs4 import BeautifulSoup
from WebCrawlerCore import WebCrawlerCore

CrawlerCore=WebCrawlerCore()
print(CrawlerCore.MemeCrawler.Get_All_MemeList())


'''
Prefix='https://rule34.paheal.net'
target_url = 'https://rule34.paheal.net/tags'
rs = requests.session()
res = rs.get(target_url)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.select('div.blockbody a'))
for index,data in enumerate(soup.select('div.blockbody a')):
    if('starts_with' in data['href'] or 'tags' in data['href']):
        continue
    print('\''+Prefix+data['href']+'\', #'+str(index)+'個 A Tag')
'''

'''
Prefix='http://www.eyny.com/'
target_url = 'http://www.eyny.com/forum-1672-1.html'
rs = requests.session()
res = rs.get(target_url, verify=False)
soup = BeautifulSoup(res.text, 'html.parser')
for index,data in enumerate(soup.select('div.bm_c tbody th.new a.xst')):
    if('lastpost' not in data['href'] and 'typeid=' not in data['href']):
        print(data.string)
        print(Prefix+data['href'])
'''


