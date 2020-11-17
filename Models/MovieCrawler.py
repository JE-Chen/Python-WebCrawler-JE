import requests
from bs4 import BeautifulSoup


class MovieCrawler():

    def __init__(self):
        pass

    # ----------------------------------------------------------------------------------------------
    # atmovies
    def Movie(self):
        content = ""

        try:

            target_url = 'http://www.atmovies.com.tw/movie/next/0/'
            rs = requests.session()
            res = rs.get(target_url)
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.text, 'html.parser')

        except Exception as Errr:
            raise Errr

        if res.status_code == 200:

            count = 0
            for index, data in enumerate(soup.select('ul.filmListAll a')):
                if (count % 2 != 0):
                    title = data.text.replace('\t', '').replace('\r', '')
                    link = "http://www.atmovies.com.tw" + data['href']
                    content += '{}\n{}\n'.format(title, link)
                count += 1
        return content
# ----------------------------------------------------------------------------------------------
