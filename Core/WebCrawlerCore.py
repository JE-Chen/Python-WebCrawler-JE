import datetime

from Models.EynyCrawler import EynyCrawler
from Models.GoogleSearchCrawler import GoogleSearchCrawler
from Models.Google_Image_Crawler import Google_Image_Crawler
from Models.MemeCrawler import MemeCrawler
from Models.MinecraftWikiCrawler import MinecraftWikiCrawler
from Models.MovieCrawler import MovieCrawler
from Models.NewsCrawler import NewsCrawler
from Models.OilCrawler import OilCrawler
from Models.PTT_Crawler import PTT_Crawler
from Models.Rule34Crawler import Rule34Crawler
from Models.StockCrawler import StockCrawler
from Models.WeatherCrawler import WeatherCrawler
from Models.WikiCrawler import WikiCrawler
from Models.Youtube_Crawler import Youtube_Crawler


class WebCrawlerCore():

    def __init__(self):
        try:
            self.EynyCrawler = EynyCrawler()
            self.Google_Image_Crawler = Google_Image_Crawler()
            self.GoogleSearchCrawler = GoogleSearchCrawler()
            self.MovieCrawler = MovieCrawler()
            self.NewsCrawler = NewsCrawler()
            self.OilCrawler = OilCrawler()
            self.PTT_Crawler = PTT_Crawler()
            self.WeatherCrawler = WeatherCrawler()
            self.Youtube_Crawler = Youtube_Crawler()
            self.StockCrawler = StockCrawler()
            self.WikiCrawler = WikiCrawler()
            self.Rule34Crawler = Rule34Crawler()
            self.MemeCrawler = MemeCrawler()
            self.MinecraftWikiCrawler = MinecraftWikiCrawler()
        except Exception as Errr:
            raise Errr
        print(datetime.datetime.now(), self.__class__, 'Ready', sep=' ')
