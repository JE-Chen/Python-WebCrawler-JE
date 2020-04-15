import datetime
import sys
from EynyCrawler import EynyCrawler
from Facebook_Crawler import Facebook_Crawler
from Google_Image_Crawler import Google_Image_Crawler
from GoogleSearchCrawler import GoogleSearchCrawler
from MovieCrawler import MovieCrawler
from NewsCrawler import NewsCrawler
from OilCrawler import OilCrawler
from PTT_Crawler import PTT_Crawler
from WeatherCrawler import WeatherCrawler
from Youtube_Crawler import Youtube_Crawler

class WebCrawlerCore():

    def __init__(self):
        try:
            self.EynyCrawler=EynyCrawler()
            self.Facebook_Crawler=Facebook_Crawler()
            self.Google_Image_Crawler=Google_Image_Crawler()
            self.GoogleSearchCrawler=GoogleSearchCrawler()
            self.MovieCrawler=MovieCrawler()
            self.NewsCrawler=NewsCrawler()
            self.OilCrawler=OilCrawler()
            self.PTT_Crawler=PTT_Crawler()
            self.WeatherCrawler=WeatherCrawler()
            self.Youtube_Crawler=Youtube_Crawler()
        except Exception as Errr:
            print(Errr)
            sys.exit()
        print(datetime.datetime.now(),'WebCrawlerCore Ready',sep=' ')





