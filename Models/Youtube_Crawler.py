import requests
from bs4 import BeautifulSoup
from pytube import YouTube


class Youtube_Crawler:

    def __init__(self, Have_Progress_Bar=True):
        self.Have_Progress_Bar = Have_Progress_Bar
        self.Set_Search()

    # ----------------------------------------------------------------------------------------------
    # 設置Url
    def Set_Url(self, Url='https://www.youtube.com/watch?v=IKei6O_vstQ'):
        self.Url = Url

        if (self.Have_Progress_Bar):
            self.yt = YouTube(self.Url, on_progress_callback=self.progress_function)
        else:
            self.yt = YouTube(self.Url)

    # 改變下載Url
    def Change_Url(self, Url='https://www.youtube.com/watch?v=IKei6O_vstQ'):
        self.Url = Url
        if (self.Have_Progress_Bar):
            self.yt = YouTube(self.Url, on_progress_callback=self.progress_function)
        else:
            self.yt = YouTube(self.Url)

    # ----------------------------------------------------------------------------------------------
    # 進度條
    def progress_function(self, stream, chunk, bytes_remaining):
        print(round((1 - bytes_remaining / self.video.filesize) * 100, 3), '% done...')

    # 是否擁有Progress_Bar
    def Change_Have_Progress_Bar(self, Have_Progress_Bar=True):
        self.Have_Progress_Bar = Have_Progress_Bar

    # ----------------------------------------------------------------------------------------------
    # 開始下載
    def Download(self):
        self.video = self.yt.streams.first()
        self.video.download()

    # ----------------------------------------------------------------------------------------------
    # 初始並設置要搜的Youtuber
    def Set_Search(self, Search_KeyWord='Martin Garrix'):
        self.Name_url = 'https://www.youtube.com/results?search_query=' + Search_KeyWord
        self.request = requests.get(self.Name_url)
        self.content = self.request.content
        self.soup = BeautifulSoup(self.content, "html.parser")

    # 秀出搜尋到的Video
    def Show_Video(self):
        for all_mv in self.soup.select(".yt-lockup-video"):
            data = all_mv.select("a[rel='spf-prefetch']")
            # 印出標題
            print(data[0].get("title"))
            # 印出連結
            print("連結 " + "https://www.youtube.com{}".format(data[0].get("href")))
            # 印出圖片連結
            img = all_mv.select("img")
            if img[0].get("src") != "/yts/img/pixel-vfl3z5WfW.gif":
                print("圖片連結 " + img[0].get("src"))

            else:
                print(img[0].get("data-thumb"))
            data = all_mv.select(".yt-lockup-meta-info")
            print(data[0].get_text())
            print("-----------------------------------------------------------")
        return data[0].get_text()
# ----------------------------------------------------------------------------------------------
