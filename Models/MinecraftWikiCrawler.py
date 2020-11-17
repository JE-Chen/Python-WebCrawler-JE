import requests
from bs4 import BeautifulSoup


class MinecraftWikiCrawler:

    def __init__(self):
        self.Prefix = 'https://minecraft-zh.gamepedia.com/'

    def Search(self, Tag):
        url = self.Prefix + Tag
        res = requests.get(url)
        content = res.content
        soup = BeautifulSoup(content, 'html.parser')
        Total = ''
        for index, data in enumerate(soup.select('#pageWrapper #bodyContent div.mw-parser-output')):
            Total += data.get_text()
        Total = Total.replace("\n"," ")
        return Total
