import re
import requests
from bs4 import BeautifulSoup

class EynyCrawler():

    def __init__(self):
        pass

    # ----------------------------------------------------------------------------------------------
    Movie_patterns = [
        'mega', 'mg', 'mu', 'ＭＥＧＡ', 'ＭＥ', 'ＭＵ',
        'ｍｅ', 'ｍｕ', 'ｍｅｇａ', 'GD', 'MG', 'google',
    ]

    Game_patterns = [
        'PC'
    ]

    # ----------------------------------------------------------------------------------------------
    def pattern_mega(self, text, Patterns):

        for pattern in Patterns:
            # re.IGNORECASE 忽略大小寫
            '''
            re.search(pattern, string, flags=0)
            函数参数說明
            参数	描述
            pattern	匹配的正则表达式
            string	要匹配的字符串。
            flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
            '''
            # 當 Patterns 裡  有匹配text的字串
            if re.search(pattern, text, re.IGNORECASE):
                return True

    # ----------------------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------------------

    # 伊莉遊戲
    def eyny_Game(self):
        target_url = 'http://www.eyny.com/forum.php?mod=forumdisplay&fid=3523'
        print('Start parsing eynyGame....')
        rs = requests.session()
        res = rs.get(target_url, verify=False)
        soup = BeautifulSoup(res.text, 'html.parser')
        content = ''
        for titleURL in soup.select('.bm_c tbody .xst'):
            if self.pattern_mega(titleURL.text, self.Game_patterns):
                title = titleURL.text
                if 'thread-262777-1-30' in titleURL['href']:
                    continue
                link = 'http://www.eyny.com/' + titleURL['href']
                data = '{}\n{}\n\n'.format(title, link)
                content += data
        return content


''' 已死去
    #伊莉電影
    def eyny_movie(self):
        target_url = 'http://www.eyny.com/forum-205-1.html'
        print('Start parsing eynyMovie....')
        rs = requests.session()
        res = rs.get(target_url, verify=False)
        soup = BeautifulSoup(res.text, 'html.parser')
        content = ''
        for titleURL in soup.select('.bm_c tbody .xst'):
            if self.pattern_mega(titleURL.text,self.Movie_patterns):
                title = titleURL.text
                if '11379780-1-3' in titleURL['href']:
                    continue
                link = 'http://www.eyny.com/' + titleURL['href']
                data = '{}\n{}\n\n'.format(title, link)
                content += data
        return content
'''

# ----------------------------------------------------------------------------------------------