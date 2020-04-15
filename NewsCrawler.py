import requests
from bs4 import BeautifulSoup
class NewsCrawler():

    def __init__(self):
        pass

# ----------------------------------------------------------------------------------------------
    # 蘋果新聞
    def apple_news(self):
        target_url = 'https://tw.appledaily.com/new/realtime'
        print('Start parsing appleNews....')
        rs = requests.session()
        res = rs.get(target_url, verify=False)
        soup = BeautifulSoup(res.text, 'html.parser')
        content = ""
        for index, data in enumerate(soup.select('.rtddt a'), 0):
            if index == 5:
                return content
            link = data['href']
            content += '{}\n\n'.format(link)
        return content

# ----------------------------------------------------------------------------------------------

    # 得到Yahoo 頭條新聞
    def Yahoo_News(self):
        res = requests.get('https://tw.yahoo.com/')
        if res.status_code == requests.codes.ok:
            soup = BeautifulSoup(res.text, 'html.parser')
            News = soup.find_all('a', class_='story-title')
            Total = ''
            for new in News:
                Total += ("標題：" + new.text)
                Total += ("網址：" + new.get('href')) + '\n\n'
            return Total
# ----------------------------------------------------------------------------------------------
    # 科技新報
    def technews(self):
        target_url = 'https://technews.tw/'
        print('Start parsing movie ...')
        rs = requests.session()
        res = rs.get(target_url, verify=False)
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
    def panx(self):
        target_url = 'https://panx.asia/'
        print('Start parsing anx.asia hot....')
        rs = requests.session()
        res = rs.get(target_url, verify=False)
        soup = BeautifulSoup(res.text, 'html.parser')
        content = ""
        for data in soup.select('div.container div.row div.desc_wrap h2 a'):
            title = data.text
            link = data['href']
            content += '{}\n{}\n\n'.format(title, link)
        return content


# ----------------------------------------------------------------------------------------------
