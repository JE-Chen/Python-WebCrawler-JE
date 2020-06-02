import pandas as pd
import re, time, requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


class Facebook_Crawler:

    def __init__(self):

        self.options = Options()
        # 關閉瀏覽器跳出訊息
        prefs = {
            'profile.default_content_setting_values':
                {
                    'notifications': 2
                }
        }
        self.options.add_experimental_option('prefs', prefs)
        # options.add_argument("--headless") #不開啟實體瀏覽器背景執行
        self.options.add_argument("--incognito")  # 開啟無痕模式

    def Open_Browser(self):
        self.driver = webdriver.Chrome(options=self.options)

# ----------------------------------------------------------------------------------------------
    #找出貼文連結
    def FindLinks(self, url='https://www.facebook.com/liouhe/', n=3):
        Links = []
        self.driver.get(url)
        for i in range(n):
            time.sleep(2)
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        # 這裡跳出要登入的大畫面，找到「稍後再說」的按鈕並點擊
        self.driver.find_element_by_xpath('//a[@id="expanding_cta_close_button"]').click()
        soup = BeautifulSoup(self.driver.page_source, features="html.parser")
        posts = soup.findAll('div', {'class': 'clearfix y_c3pyo2ta3'})
        for i in posts:
            Links.append('https://www.facebook.com' + i.find('a', {'class': '_5pcq'}).attrs['href'].split('?', 2)[0])
        return Links

# ----------------------------------------------------------------------------------------------

    #抓取留言 表情等
    def expand(self, url):
        self.driver.get(url)
        try:
            self.driver.find_element_by_xpath('//a[@lang="en_US"]').click()
        except:
            pass
            #print("Now is in EN_US")
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        # 點擊「comments」，藉以展開留言
        try:
            self.driver.find_element_by_xpath(
                '//div[@class="_5pcr userContentWrapper"]//a[@data-testid="UFI2CommentsCount/root"]').click()
            time.sleep(1)
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(1)
            self.driver.find_element_by_id('expanding_cta_close_button').click()
        except:
            pass
            #print('There is no comment!')
        k = 1
        while k != 0:
            k = 0
            for i in self.driver.find_elements_by_xpath(
                    '//div[@class="_5pcr userContentWrapper"]//div[@data-testid="UFI2CommentsList/root_depth_0"]//a[@role="button"]'):
                # 反覆偵測是否有「看更多留言」、「看更多回覆」與「看完整貼文內容」等按鈕，若有擇點擊
                if bool(re.search('comment|More|Repl', i.text)) == True:
                    self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    time.sleep(2)
                    try:
                        self.driver.find_element_by_xpath(
                            '//div[@style="display: block;"]//a[@id="expanding_cta_close_button"]').click()
                    except:
                        print('No pupup!')
                    try:
                        i.click()
                    except:
                        print('Nothing')
                    time.sleep(2)
                    k += 1

# ----------------------------------------------------------------------------------------------

    # 文章內容與互動摘要
    def PostContent(self,soup):
        # po文區塊
        userContent = soup.find('div', {'class': '_5pcr userContentWrapper'})
        # po文人資訊區塊
        PosterInfo = userContent.find('div', {'class': 'l_c3pyo2v0u i_c3pynyi2f clearfix'})
        # 互動摘要區(讚、留言與分享)
        feedback = soup.find('form', {'class': 'commentable_item collapsed_comments'})
        # 名稱
        Name = PosterInfo.find('img').attrs['aria-label']
        # ID
        ID = \
        PosterInfo.find('a', {'class': '_5pb8 o_c3pynyi2g _8o _8s lfloat _ohe'}).attrs['href'].split('/?', 2)[0].split('/',
                                                                                                                       -1)[
            -1]
        # 網址
        Link = self.driver.current_url
        # 發文時間
        try:
            Time = PosterInfo.find('abbr').attrs['title']
        except:
            Time = PosterInfo.find('div', {'class': '_1atc fsm fwn fcg'}).text
        # 文章內容
        try:
            Content = userContent.find('div', {'class': '_5pbx userContent _3576'}).text
        except:
            Content = ""
        # Like
        try:
            Like = feedback.find('span', {'data-testid': 'UFI2TopReactions/tooltip_LIKE'}).find('a').attrs['aria-label']
        except:
            Like = '0'
            # Angry
        try:
            ANGER = feedback.find('span', {'data-testid': 'UFI2TopReactions/tooltip_ANGER'}).find('a').attrs['aria-label']
        except:
            ANGER = '0'
        # HAHA
        try:
            HAHA = feedback.find('span', {'data-testid': 'UFI2TopReactions/tooltip_HAHA'}).find('a').attrs['aria-label']
        except:
            HAHA = '0'
        # 留言
        try:
            commentcount = feedback.find('a', {'data-testid': 'UFI2CommentsCount/root'}).text
        except:
            commentcount = '0'
            # 分享
        try:
            share = feedback.find('span', {'class': '_355t _4vn2'}).text
        except:
            share = '0'
        return pd.DataFrame(
            data=[{'Name': Name,
                   'ID': ID,
                   'Link': Link,
                   'Time': Time,
                   'Content': Content,
                   'Like': Like,
                   'ANGER': ANGER,
                   "HAHA": HAHA,
                   'commentcount': commentcount,
                   'share': share}],
            columns=['Name', 'ID', 'Time', 'Content', 'Like', 'ANGER', 'HAHA', 'commentcount', 'share', 'Link'])

# ----------------------------------------------------------------------------------------------

    # 留言
    def CrawlComment(self,soup):
        Comments = pd.DataFrame()
        # po文區塊
        userContent = soup.find('div', {'class': '_5pcr userContentWrapper'})
        # 用戶留言區
        userContent = soup.find('div', {'class': '_5pcr userContentWrapper'})
        # 回應貼文的留言
        for i in userContent.findAll('div', {'data-testid': 'UFI2Comment/root_depth_0'}):
            try:
                CommentContent = i.find('span', {'dir': 'ltr'}).text
            except:
                CommentContent = 'Sticker'
            Comment = pd.DataFrame(
                data=[{'CommentID': i.find('a', {'class': ' _3mf5 _3mg0'}).attrs['data-hovercard'].split('id=', 2)[1],
                       'CommentName': i.find('img').attrs['alt'],
                       'CommentTime': i.find('abbr', {'class': 'livetimestamp'}).attrs['data-tooltip-content'],
                       'CommentContent': CommentContent,
                       'Link': self.driver.current_url}],
                columns=['CommentID', 'CommentName', 'CommentTime', 'CommentContent', 'Link'])
            Comments = pd.concat([Comments, Comment], ignore_index=True)
    
        # 回應留言的留言
        for i in userContent.findAll('div', {'data-testid': 'UFI2Comment/root_depth_1'}):
            try:
                CommentContent = i.find('span', {'dir': 'ltr'}).text
            except:
                CommentContent = 'Sticker'
            Comment = pd.DataFrame(
                data=[{'CommentID': i.find('a', {'class': ' _3mf5 _3mg1'}).attrs['data-hovercard'].split('id=', 2)[1],
                       'CommentName': i.find('img').attrs['alt'],
                       'CommentTime': i.find('abbr', {'class': 'livetimestamp'}).attrs['data-tooltip-content'],
                       'CommentContent': CommentContent,
                       'Link': self.driver.current_url}],
                columns=['CommentID', 'CommentName', 'CommentTime', 'CommentContent', 'Link'])
            Comments = pd.concat([Comments, Comment], ignore_index=True)
        return Comments

# ----------------------------------------------------------------------------------------------
    #取得專頁貼文連結 n決定抓取數
    def Get_Page_Link(self, url='https://www.facebook.com/liouhe/', n=3):
        self.Open_Browser()
        Links = self.FindLinks(url=url,n=n)

        # 抓下來所有留言
        #PostsInformation = pd.DataFrame()
        #PostsComments = pd.DataFrame()

        for i in Links:
            print('取得貼文 : ' + i)
            '''
            try:
                self.expand(i)
            except:
                pass
                # print('Load Failed: ' + i)
            '''
        self.driver.close()

# ----------------------------------------------------------------------------------------------

    #取得粉絲專頁讚數
    def Get_Like(self,url='https://www.facebook.com/liouhe/?epa=SEARCH_BOX'):
        target_url = url
        print('Start parsing FB Like...')
        rs = requests.session()
        res = rs.get(target_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        content = ""
        Continue_count = 0
        for data in (soup.select('.clearfix div._57dz div._3-95 div._1xnd div._2pi9 div._4bl9')):
            if (Continue_count >= 2):
                continue
            Continue_count += 1
            like = data.text
            content += like + '\n'
        return (content)
