import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

#Google 圖片爬蟲
class Google_Image_Crawler:

    def __init__(self,Keyword='Discord'):

        self.options = Options()
        # 關閉瀏覽器跳出訊息
        prefs = {
            'profile.default_content_setting_values':
                {
                    'notifications': 2
                }
        }
        self.options.add_experimental_option('prefs', prefs)
        #options.add_argument("--headless")  # 不開啟實體瀏覽器背景執行
        self.options.add_argument("--incognito")  # 開啟無痕模式
        # define url using search term
        self.Keyword=Keyword
        #get img and url
        self.Img_Url = []


    def Start_Browser(self):
        # create webdriver
        browser = webdriver.Chrome(options=self.options)
        self.browser=browser

# ----------------------------------------------------------------------------------------------

    #開始搜尋Google
    def Scrape_Pic_NoSave(self):
        try:
            self.Click_Button()
            self.Scroll_Down()
            self.Click_Button()
            self.Scroll_Down()
            Return_Url=self.Find_Image_NoSave()
        except:
            self.Click_Button()
            self.Scroll_Down()
            self.Click_Button()
            self.Scroll_Down()
            Return_Url=self.Find_Image_NoSave()

        try:
            self.browser.quit()
            # close driver
            self.browser.close()
        except:
            pass
        return Return_Url

# ----------------------------------------------------------------------------------------------
    # 開始搜尋Google
    def Scrape_Pic_Save(self):
        try:
            self.Click_Button()
            self.Scroll_Down()
            self.Click_Button()
            self.Scroll_Down()
            Return_Url = self.Find_Image_Save()
        except:
            self.Click_Button()
            self.Scroll_Down()
            self.Click_Button()
            self.Scroll_Down()
            Return_Url = self.Find_Image_Save()

        try:
            self.browser.quit()
            # close driver
            self.browser.close()
        except:
            pass
        return Return_Url

# ----------------------------------------------------------------------------------------------
    #往下滑
    def Scroll_Down(self,roll=7):
        for i in range(roll):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(3)

# ----------------------------------------------------------------------------------------------
    #點擊更多圖片按鈕
    def Click_Button(self):
        time.sleep(1)
        button = self.browser.find_element_by_class_name(u"mye4qd")
        self.browser.implicitly_wait(1)
        if (button.is_displayed()):
            ActionChains(self.browser).move_to_element(button).click(button).perform()
        else:
           pass

# ----------------------------------------------------------------------------------------------
    #取得BSoup
    def Get_Soup(self):
        html_source = self.browser.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        return soup

# ----------------------------------------------------------------------------------------------
    #取得圖片並存檔連結與圖片
    def Find_Image_Save(self):
        count = 0
        for img in (self.Get_Soup().find_all('img')):
            try:
                self.Img_Url.append(img['src'])
            except:
                pass

        #取得所有img標籤的元素
        for item in (self.Get_Soup().find_all('img')):

            if (str(item.get('src')).startswith('http')):
                # 取得圖片 並判斷是不是http開頭

                if(count==len(self.Img_Url)-1):
                    print('此無更多圖片可抓')
                    break
                else:
                    # 印出取得的圖片網址
                    print(item.get('src'))
                    html = requests.get(item.get('src'))
                    img_name = str(count + 1) + '.png'

                    with open(img_name, 'wb') as file:
                        file.write(html.content)

                        file.flush()

                    file.close()  # close file
                    if(item.get('src')!=None and html.content!=None):
                        print('第 %d 張' % (count + 1))
                    count += 1
            # return list of all img urls found in page
            output = open('Image_Url.txt', 'w', encoding='utf-8')
            for x in range(len(self.Img_Url)):
                output.write(str(self.Img_Url[x]) + '\n')
            output.close()
        print('結束抓圖 已被偵測')
        self.browser.close()
        return self.Img_Url

# ----------------------------------------------------------------------------------------------
    #取得圖片連結 不存檔
    def Find_Image_NoSave(self):
        count = 0
        for img in (self.Get_Soup().find_all('img')):
            try:
                if (str(img.get('src')).startswith('http')):
                    self.Img_Url.append(img['src'])
            except:
                pass

        #取得所有img標籤的元素
        for item in (self.Get_Soup().find_all('img')):

            if (str(item.get('src')).startswith('http')):
                # 取得圖片 並判斷是不是http開頭

                if(count==len(self.Img_Url)-1):
                    print('此無更多圖片可抓')
                    break
                else:
                    # 印出取得的圖片網址
                    print(item.get('src'))
                    html = requests.get(item.get('src'))
                    img_name = str(count + 1) + '.png'
                    if(item.get('src')!=None and html.content!=None):
                        print('第 %d 張' % (count + 1))
                    count += 1
            # return list of all img urls found in page
        print('結束抓圖 已被偵測')
        self.browser.close()
        return self.Img_Url

# ----------------------------------------------------------------------------------------------
    #設置Keyword
    def Set_Keyword(self,Keyword):
        self.Keyword=Keyword
# ----------------------------------------------------------------------------------------------
    #呼叫上面搜尋
    def Start_Crawler(self,Mode=1):
        self.Start_Browser()
        searchUrl = "https://www.google.com/search?q={}&site=webhp&tbm=isch".format(self.Keyword)
        # get url
        self.browser.get(searchUrl)
        if(Mode==1):
            Return_Url=self.Scrape_Pic_NoSave()
        else:
            Return_Url=self.Scrape_Pic_Save()
        return Return_Url



