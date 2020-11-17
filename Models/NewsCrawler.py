import requests
from bs4 import BeautifulSoup


class NewsCrawler():

    def __init__(self):
        pass

    # ----------------------------------------------------------------------------------------------
    # 蘋果新聞
    # Need to fix
    def Apple_news(self):
        Link_List = []
        Title_List = []
        Total = ''

        try:

            target_url = 'https://tw.appledaily.com/new/realtime'
            rs = requests.session()
            res = rs.get(target_url)
            soup = BeautifulSoup(res.text, 'html.parser')

        except Exception as Errr:
            raise Errr

        if res.status_code == requests.codes.ok:

            for index, data in enumerate(soup.select('div.main-content-container a')):
                Link_List.append(data['href'])

            for index, data in enumerate(soup.select('div.box--margin-top storycard-blurb text_greyish-brown-two')):
                Title_List.append(data.string)

            for index in range(len(Title_List)):
                Total += (Title_List[index]) + '\n'
                Total += (Link_List[index]) + '\n'

        return Total

    # ----------------------------------------------------------------------------------------------

    # 得到Yahoo 頭條新聞
    def Yahoo_News(self):
        Total = ''
        try:
            res = requests.get('https://tw.yahoo.com/')
        except Exception as Errr:
            raise Errr

        if res.status_code == requests.codes.ok:
            soup = BeautifulSoup(res.text, 'html.parser')
            News = soup.find_all('a', class_='story-title')
            for new in News:
                Total += ("標題：" + new.text)
                Total += ("網址：" + new.get('href')) + '\n\n'
            return Total

    # ----------------------------------------------------------------------------------------------
    # 科技新報
    def Technews(self):
        target_url = 'https://technews.tw/'
        print('Start parsing movie ...')
        rs = requests.session()
        res = rs.get(target_url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        content = ""

        for index, data in enumerate(soup.select('article div h1.entry-title a')):
            if index == 12:
                return content
            title = data.text
            link = data['href']
            content += '{}\n{}\n\n'.format(title, link)
        return content

    # ----------------------------------------------------------------------------------------------

    # 泛科技
    def Panx(self):
        target_url = 'https://panx.asia/'
        print('Start parsing anx.asia hot....')
        rs = requests.session()
        res = rs.get(target_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        content = ""
        for data in soup.select('div.container div.row div.desc_wrap h2 a'):
            title = data.text
            link = data['href']
            content += '{}\n{}\n\n'.format(title, link)
        return content

# ----------------------------------------------------------------------------------------------
