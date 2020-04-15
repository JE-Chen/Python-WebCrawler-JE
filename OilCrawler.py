import requests
from bs4 import BeautifulSoup

class OilCrawler():

    # 油價
    def Taiwan_Oil_Price(self):
        target_url = 'https://www2.moeaboe.gov.tw/oil102/oil2017/A01/A0108/tablesprices.asp'
        print('Start parsing Taiwan_Oil_Price....')
        rs = requests.session()
        res = rs.get(target_url)
        res.encoding = 'big5'
        soup = BeautifulSoup(res.text, 'html.parser')
        content = ''
        count = 0
        pass_count = 0
        for titleURL in soup.select('.rwd-table tr td'):
            if (pass_count < 12):
                pass_count += 1
                continue
            title = titleURL.text
            data = '{}  '.format(title)
            count += 1
            if (count < 7):
                if (count == 1):
                    content += data
                elif (count == 2):
                    content += '98無鉛汽油 ' + data
                elif (count == 3):
                    content += '95無鉛汽油 ' + data
                elif (count == 4):
                    content += '92無鉛汽油 ' + data
                elif (count == 5):
                    content += '超(高)級柴油 ' + data
                elif (count == 6):
                    content += '計價單位 ' + data
            else:
                content += data + '\n'
                count = 0
        return content

# ----------------------------------------------------------------------------------------------
