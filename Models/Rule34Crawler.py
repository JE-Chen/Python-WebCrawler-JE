import requests
import random
from bs4 import BeautifulSoup
class Rule34Crawler():

    def __init__(self):
        self.Prefix='https://rule34.paheal.net'
        self.Target_Tag_URL=[
            'https://rule34.paheal.net/tags', #取得所有Tag網址 跟 A TAG 0
            'https://rule34.paheal.net/tags?starts_with=.', #. Tag 1
            'https://rule34.paheal.net/tags?starts_with=%2F', #/ Tag 2
            'https://rule34.paheal.net/tags?starts_with=%3A', #: Tag 3
            'https://rule34.paheal.net/tags?starts_with=%40',  #@ Tag 4
            'https://rule34.paheal.net/tags?starts_with=%5B',  #[ Tag 5
            'https://rule34.paheal.net/tags?starts_with=0',  #0 Tag 6
            'https://rule34.paheal.net/tags?starts_with=1',  #1 Tag 7
            'https://rule34.paheal.net/tags?starts_with=2',  #2 Tag 8
            'https://rule34.paheal.net/tags?starts_with=3',  #3 Tag 9
            'https://rule34.paheal.net/tags?starts_with=4',  #4 Tag 10
            'https://rule34.paheal.net/tags?starts_with=5',  #5 Tag 11
            'https://rule34.paheal.net/tags?starts_with=6',  #6 Tag 12
            'https://rule34.paheal.net/tags?starts_with=7',  #7 Tag 13
            'https://rule34.paheal.net/tags?starts_with=8',  #8 Tag 14
            'https://rule34.paheal.net/tags?starts_with=9',  #9 Tag 15
            'https://rule34.paheal.net/tags?starts_with=a',  #A Tag 16
            'https://rule34.paheal.net/tags?starts_with=b',  #B Tag 17
            'https://rule34.paheal.net/tags?starts_with=c',  #C Tag 18
            'https://rule34.paheal.net/tags?starts_with=d',  #D Tag 19
            'https://rule34.paheal.net/tags?starts_with=e',  #E Tag 20
            'https://rule34.paheal.net/tags?starts_with=f',  #F Tag 21
            'https://rule34.paheal.net/tags?starts_with=g',  #G Tag 22
            'https://rule34.paheal.net/tags?starts_with=h',  #H Tag 23
            'https://rule34.paheal.net/tags?starts_with=i',  #I Tag 24
            'https://rule34.paheal.net/tags?starts_with=k',  #J Tag 25
            'https://rule34.paheal.net/tags?starts_with=k',  #K Tag 26
            'https://rule34.paheal.net/tags?starts_with=l',  #L Tag 27
            'https://rule34.paheal.net/tags?starts_with=m',  #M Tag 28
            'https://rule34.paheal.net/tags?starts_with=n',  #N Tag 29
            'https://rule34.paheal.net/tags?starts_with=o',  #O Tag 30
            'https://rule34.paheal.net/tags?starts_with=p',  #P Tag 31
            'https://rule34.paheal.net/tags?starts_with=q',  #Q Tag 32
            'https://rule34.paheal.net/tags?starts_with=r',  #R Tag 33
            'https://rule34.paheal.net/tags?starts_with=s',  #S Tag 34
            'https://rule34.paheal.net/tags?starts_with=t',  #T Tag 35
            'https://rule34.paheal.net/tags?starts_with=u',  #U Tag 36
            'https://rule34.paheal.net/tags?starts_with=v',  #V Tag 37
            'https://rule34.paheal.net/tags?starts_with=w',  #W Tag 38
            'https://rule34.paheal.net/tags?starts_with=x',  #X Tag 39
            'https://rule34.paheal.net/tags?starts_with=y',  #Y Tag 40
            'https://rule34.paheal.net/tags?starts_with=z',  #Z Tag 41
        ]

# ----------------------------------------------------------------------------------------------
    #取得Start_with 裡的 Tag 返回 String
    def Get_Tag_Content_String(self):
        Total=''

        try :

            Target_URL = self.Target_Tag_URL[0]
            rs = requests.session()
            res = rs.get(Target_URL)
            soup = BeautifulSoup(res.text, 'html.parser')

        except Exception as Errr:
            raise Errr

        if res.status_code==200:

            for index, data in enumerate(soup.select('div.blockbody a')):
                if ('starts_with' in data['href'] or 'tags' in data['href']
                    or 'bad_ads' in data['href'] or 'wiki/rules' in data['href'] or'hentaikey' in data['href']
                or 'idzone=' in data['href'] or 'palcomix' in data['href'] or data['href'].endswith('list')):
                    continue
                Total+=(self.Prefix + data['href'])+'\n'

        return Total

    #取得Start_with 裡的 Tag 返回List
    def Get_Tag_Content_List(self):
        Total = []

        try:

            Target_URL = self.Target_Tag_URL[0]
            rs = requests.session()
            res = rs.get(Target_URL)
            soup = BeautifulSoup(res.text, 'html.parser')

        except Exception as Errr:
            raise Errr

        if res.status_code==200:

            for index, data in enumerate(soup.select('div.blockbody a')):
                if ('starts_with' in data['href'] or 'tags' in data['href']
                    or 'bad_ads' in data['href'] or 'wiki/rules' in data['href'] or'hentaikey' in data['href']
                or 'idzone=' in data['href'] or 'palcomix' in data['href'] or data['href'].endswith('list')):
                    continue
                Total.append((self.Prefix + data['href']))

        return Total

# ----------------------------------------------------------------------------------------------
    #取得照片連結
    def Get_Photo(self,URL):
        Total=''

        try:

            rs = requests.session()
            res = rs.get(URL)
            soup = BeautifulSoup(res.text, 'html.parser')

        except Exception as Errr:
            raise Errr

        if res.status_code==200:
            for index, data in enumerate(soup.select('div.blockbody div.shm-image-list a.shm-thumb-link')):
                Total+=(self.Prefix + data['href'])+'\n'

        return Total


