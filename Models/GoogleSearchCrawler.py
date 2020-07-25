from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import threading

class GoogleSearchCrawler(threading.Thread):

    def __init__(self):
        super().__init__()

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

    def Open_Browser(self):
        self.browser = webdriver.Chrome(options=self.options)
        self.browser.get('https://www.google.com')


# ----------------------------------------------------------------------------------------------
    #搜尋關鍵字
    def Search_Keyword(self,Element_Name='q',KeyWord='六合夜市'):
        self.Open_Browser()
        q=self.browser.find_element_by_name(Element_Name)
        q.send_keys(KeyWord)
        q.submit()

# ----------------------------------------------------------------------------------------------
    #得到搜尋的關鍵字的標題
    def Get_Search_Title(self,File_Format='lxml',Select='#rso h3'):
        soup=BeautifulSoup(self.browser.page_source,File_Format)
        for ele in soup.select(Select):
            if(ele.text=='影片'):
                continue
            print(ele.text)

# ----------------------------------------------------------------------------------------------
    #得到搜尋的連結
    def Get_Search_Link(self,Selector='div.r a[href]:first-child',Attribute_Format='href'):
        elems = self.browser.find_elements_by_css_selector(Selector)
        links=[]
        for elem in elems:
            links.append(elem.get_attribute(Attribute_Format))
        print(links)

# ----------------------------------------------------------------------------------------------
    #下一頁
    def Next_Page(self):
        self.browser.find_element_by_link_text('下一頁').click()

# ----------------------------------------------------------------------------------------------
    #關閉瀏覽器
    def Close(self):
        self.browser.close()
