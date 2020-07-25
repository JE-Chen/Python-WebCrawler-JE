import requests
from bs4 import BeautifulSoup

class WikiCrawler():

    def __init__(self):
        self.Prefix='https://zh.wikipedia.org/wiki/'


    def Search(self,Tag):
        url=self.Prefix+Tag
        res =requests.get(url)
        content=res.content
        soup=BeautifulSoup(content,'html.parser')
        Total=''
        for index,data in enumerate(soup.select('div.mw-body div.mw-body-content div.mw-parser-output p')):
            Total+=(data.get_text())+'\n'
        return Total