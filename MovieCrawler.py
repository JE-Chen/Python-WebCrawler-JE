import requests
from bs4 import BeautifulSoup
class MovieCrawler():

    def __init__(self):
        pass

# ----------------------------------------------------------------------------------------------
    # atmovies
    def movie(self):
        target_url = 'http://www.atmovies.com.tw/movie/next/0/'
        print('Start parsing movie ...')
        rs = requests.session()
        res = rs.get(target_url, verify=False)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        content = ""
        for index, data in enumerate(soup.select('ul.filmNextListAll a')):
            if index == 20:
                return content
            title = data.text.replace('\t', '').replace('\r', '')
            link = "http://www.atmovies.com.tw" + data['href']
            content += '{}\n{}\n'.format(title, link)
        return content
# ----------------------------------------------------------------------------------------------