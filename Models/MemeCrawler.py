import requests
from bs4 import BeautifulSoup


class MemeCrawler():

    def __init__(self):
        self.Prefix = 'https://memes.tw'
        self.Target_Url = 'https://memes.tw/maker'

    def Get_All_MemeList(self):
        Total = ''
        Title_List = []
        Href_List = []
        try:

            rs = requests.session()
            res = rs.get(self.Target_Url)
            soup = BeautifulSoup(res.text, 'html.parser')

        except Exception as Errr:

            raise Errr

        if res.status_code == 200:

            for index, data in enumerate(soup.select('div.col div.col-6 div.-shadow b')):
                Title_List.append(data.string)

            for index, data in enumerate(soup.select('div.col div.col-6 div.-shadow a')):
                text = self.Prefix + data['href']
                if ('painter' in text or 'template' in text or 'login' in text):
                    pass
                else:
                    Href_List.append(text)

            for index in range(len(Title_List)):
                Total += Title_List[index] + '\n'
                Total += Href_List[index] + '\n'

        return Total
