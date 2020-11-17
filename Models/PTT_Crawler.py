import requests
from bs4 import BeautifulSoup


class PTT_Crawler:
    '''
        'https://www.ptt.cc//bbs/',  # 總版
        'https://www.ptt.cc//about.html',  # ptt 關於資訊
        'https://www.ptt.cc//contact.html',  # ptt 聯絡資訊
        'https://www.ptt.cc//bbs/hotboards.html',  # 連至總版 網址不同
        'https://www.ptt.cc//cls/1',  # 群組
    '''

    Ptt_Link = [
        'https://www.ptt.cc//bbs/Gossiping/index.html',  # 無法 Fix
        'https://www.ptt.cc//bbs/C_Chat/index.html',  # C_Chat版
        'https://www.ptt.cc//bbs/Stock/index.html',  # Stock版
        'https://www.ptt.cc//bbs/Lifeismoney/index.html',  # Lifeismoney版
        'https://www.ptt.cc//bbs/NSwitch/index.html',  # NSwitch版
        'https://www.ptt.cc//bbs/LoL/index.html',
        'https://www.ptt.cc//bbs/sex/index.html',  # 無法 Fix
        'https://www.ptt.cc//bbs/NBA/index.html',
        'https://www.ptt.cc//bbs/Baseball/index.html',
        'https://www.ptt.cc//bbs/movie/index.html',
        'https://www.ptt.cc//bbs/car/index.html',
        'https://www.ptt.cc//bbs/KoreaDrama/index.html',
        'https://www.ptt.cc//bbs/Beauty/index.html',  # 無法
        'https://www.ptt.cc//bbs/MobileComm/index.html',
        'https://www.ptt.cc//bbs/WomenTalk/index.html',
        'https://www.ptt.cc//bbs/BabyMother/index.html',
        'https://www.ptt.cc//bbs/e-shopping/index.html',
        'https://www.ptt.cc//bbs/Boy-Girl/index.html',
        'https://www.ptt.cc//bbs/AllTogether/index.html',
        'https://www.ptt.cc//bbs/Tech_Job/index.html',
        'https://www.ptt.cc//bbs/PlayStation/index.html',
        'https://www.ptt.cc//bbs/TW_Entertain/index.html',
        'https://www.ptt.cc//bbs/joke/index.html',
        'https://www.ptt.cc//bbs/home-sale/index.html',
        'https://www.ptt.cc//bbs/ToS/index.html',
        'https://www.ptt.cc//bbs/Steam/index.html',
        'https://www.ptt.cc//bbs/PC_Shopping/index.html',
        'https://www.ptt.cc//bbs/AnimalForest/index.html',
        'https://www.ptt.cc//bbs/KR_Entertain/index.html',
        'https://www.ptt.cc//bbs/iOS/index.html',
        'https://www.ptt.cc//bbs/japanavgirls/index.html',  # 無法
        'https://www.ptt.cc//bbs/TaiwanDrama/index.html',
        'https://www.ptt.cc//bbs/marriage/index.html',
        'https://www.ptt.cc//bbs/Tainan/index.html',
        'https://www.ptt.cc//bbs/HatePolitics/index.html',  # 無法
        'https://www.ptt.cc//bbs/KoreaStar/index.html',
        'https://www.ptt.cc//bbs/marvel/index.html',
        'https://www.ptt.cc//bbs/BeautySalon/index.html',
        'https://www.ptt.cc//bbs/creditcard/index.html',
        'https://www.ptt.cc//bbs/Gamesale/index.html',
        'https://www.ptt.cc//bbs/MakeUp/index.html',
        'https://www.ptt.cc//bbs/Kaohsiung/index.html',
        'https://www.ptt.cc//bbs/CFantasy/index.html',
        'https://www.ptt.cc//bbs/TaichungBun/index.html',
        'https://www.ptt.cc//bbs/EAseries/index.html',
        'https://www.ptt.cc//bbs/HardwareSale/index.html',
        'https://www.ptt.cc//bbs/ONE_PIECE/index.html',
        'https://www.ptt.cc//bbs/Japandrama/index.html',
        'https://www.ptt.cc//bbs/basketballTW/index.html',
        'https://www.ptt.cc//bbs/StupidClown/index.html',
        'https://www.ptt.cc//bbs/Hearthstone/index.html',
        'https://www.ptt.cc//bbs/PokemonGO/index.html',
        'https://www.ptt.cc//bbs/China-Drama/index.html',
        'https://www.ptt.cc//bbs/Salary/index.html',
        'https://www.ptt.cc//bbs/YuanChuang/index.html',
        'https://www.ptt.cc//bbs/CVS/index.html',
        'https://www.ptt.cc//bbs/SportLottery/index.html',  # 無法
        'https://www.ptt.cc//bbs/AC_In/index.html',  # 無法
        'https://www.ptt.cc//bbs/Hsinchu/index.html',
        'https://www.ptt.cc//bbs/AzurLane/index.html',
        'https://www.ptt.cc//bbs/Japan_Travel/index.html',
        'https://www.ptt.cc//bbs/mobilesales/index.html',
        'https://www.ptt.cc//bbs/biker/index.html',
        'https://www.ptt.cc//bbs/Brand/index.html',  # 無法
        'https://www.ptt.cc//bbs/MuscleBeach/index.html',
        'https://www.ptt.cc//bbs/Food/index.html',
        'https://www.ptt.cc//bbs/Headphone/index.html',
        'https://www.ptt.cc//bbs/BuyTogether/index.html',  # 無法
        'https://www.ptt.cc//bbs/GetMarry/index.html',
        'https://www.ptt.cc//bbs/CarShop/index.html',
        'https://www.ptt.cc//bbs/Palmar_Drama/index.html',
        'https://www.ptt.cc//bbs/cookclub/index.html',
        'https://www.ptt.cc//bbs/forsale/index.html',
        'https://www.ptt.cc//bbs/PCReDive/index.html',
        'https://www.ptt.cc//bbs/PathofExile/index.html',
        'https://www.ptt.cc//bbs/TWICE/index.html',
        'https://www.ptt.cc//bbs/Wanted/index.html',
        'https://www.ptt.cc//bbs/MH/index.html',
        'https://www.ptt.cc//bbs/feminine_sex/index.html',  # 無法
        'https://www.ptt.cc//bbs/MacShop/index.html',
        'https://www.ptt.cc//bbs/FATE_GO/index.html',
        'https://www.ptt.cc//bbs/PuzzleDragon/index.html',
        'https://www.ptt.cc//bbs/WOW/index.html',
        'https://www.ptt.cc//bbs/BabyProducts/index.html',
        'https://www.ptt.cc//bbs/KoreanPop/index.html',
        'https://www.ptt.cc//bbs/E-appliance/index.html',
        'https://www.ptt.cc//bbs/Elephants/index.html',
        'https://www.ptt.cc//bbs/watch/index.html',
        'https://www.ptt.cc//bbs/Bank_Service/index.html',
        'https://www.ptt.cc//bbs/GBF/index.html',
        'https://www.ptt.cc//bbs/lesbian/index.html',
        'https://www.ptt.cc//bbs/MobilePay/index.html',
        'https://www.ptt.cc//bbs/Soft_Job/index.html',
        'https://www.ptt.cc//bbs/JP_Entertain/index.html',
        'https://www.ptt.cc//bbs/gay/index.html',
        'https://www.ptt.cc//bbs/Finance/index.html',
        'https://www.ptt.cc//bbs/cat/index.html',
        'https://www.ptt.cc//bbs/Examination/index.html',
        'https://www.ptt.cc//bbs/SuperJunior/index.html',
        'https://www.ptt.cc//bbs/Aviation/index.html',
        'https://www.ptt.cc//bbs/ArenaOfValor/index.html',
        'https://www.ptt.cc//bbs/DSLR/index.html',
        'https://www.ptt.cc//bbs/Gov_owned/index.html',
        'https://www.ptt.cc//bbs/HelpBuy/index.html',
        'https://www.ptt.cc//bbs/graduate/index.html',
        'https://www.ptt.cc//bbs/medstudent/index.html',
        'https://www.ptt.cc//bbs/NBA_Film/index.html',
        'https://www.ptt.cc//bbs/hypermall/index.html',
        'https://www.ptt.cc//bbs/part-time/index.html',
        'https://www.ptt.cc//bbs/give/index.html',
        'https://www.ptt.cc//bbs/BB-Love/index.html',  # 無法
        'https://www.ptt.cc//bbs/DC_SALE/index.html',
        'https://www.ptt.cc//bbs/book/index.html',
        'https://www.ptt.cc//bbs/nb-shopping/index.html',
        'https://www.ptt.cc//bbs/SuperBike/index.html',  # 無法
        'https://www.ptt.cc//bbs/PublicServan/index.html',
        'https://www.ptt.cc//bbs/Key_Mou_Pad/index.html',
        'https://www.ptt.cc//bbs/CN_Entertain/index.html',
        'https://www.ptt.cc//bbs/Taoyuan/index.html',
        'https://www.ptt.cc//bbs/Nogizaka46/index.html',
        'https://www.ptt.cc//bbs/KanColle/index.html',
        'https://www.ptt.cc//bbs/Mobile-game/index.html',
        'https://www.ptt.cc//bbs/FITNESS/index.html',
        'https://www.ptt.cc//bbs/Foreign_Inv/index.html',
        'https://www.ptt.cc//bbs/studyabroad/index.html',
        'https://www.ptt.cc//bbs/Option/index.html',
        'https://www.ptt.cc//bbs/facelift/index.html',
        'https://www.ptt.cc//bbs/BB_Online/index.html'
    ]

    # ----------------------------------------------------------------------------------------------

    # 取得有幾篇
    def Get_Page_Number(self, content):
        start_index = content.find('index')
        end_index = content.find('.html')
        page_number = content[start_index + 5: end_index]
        return (len(page_number) + 1)

    # 取得連結的陣列表
    def Get_Ptt_Link(self):
        return self.Ptt_Link

    # 取得連結
    def Get_Ptt_Link_index(self, index):
        return self.Ptt_Link[index]

    # ----------------------------------------------------------------------------------------------

    '''依照ptt版的url 搜尋文章  低於 push_rate 評分的不出現
    title : 標題
    url : 連結
    rate : 推文
    回傳 {    'title':title,  'url':url,  'rate':rate }
    '''

    def Craw_Page_Rate(self, url='https://www.ptt.cc/bbs/C_Chat/index.html', push_rate=10):
        print('Start parsing \t' + url)
        rs = requests.session()
        res = rs.get(url, cookies={'over18': '1'})
        soup_ = BeautifulSoup(res.text, 'lxml')
        article_seq = []
        for r_ent in soup_.find_all(class_="r-ent"):
            try:
                # 先得到每篇文章的篇url
                link = r_ent.find('a')['href']
                if link:
                    # 確定得到url再去抓 標題 以及 推文數
                    title = r_ent.find(class_="title").text.strip()
                    rate = r_ent.find(class_="nrec").text
                    url = 'https://www.ptt.cc' + link
                    if rate:
                        rate = 100 if rate.startswith('爆') else rate
                        rate = -1 * int(rate[1]) if rate.startswith('X') else rate
                    else:
                        rate = 0
                    # 比對推文數
                    if int(rate) >= push_rate:
                        article_seq.append({
                            'title': title,
                            'url': url,
                            'rate': rate,
                        })
            except Exception as e:
                # print('crawPage function error:',r_ent.find(class_="title").text.strip())
                print('本文已被刪除', e)
        Total = ''
        for i in range(len(article_seq)):
            Total += article_seq[i]['title'] + '\n'
            Total += (article_seq[i]['url']) + '\n'
            Total += ('推文數 : ' + article_seq[i]['rate']) + '\n'
            Total += ('-----------------------------------------------------') + '\n'
        return Total

    # ----------------------------------------------------------------------------------------------
    # 依照ptt版的url 搜尋文章
    def Crawl_Page(self, url='https://www.ptt.cc/bbs/C_Chat/index.html'):
        print('Start parsing \t' + url)
        rs = requests.session()
        res = rs.get(url, cookies={'over18': '1'})
        soup = BeautifulSoup(res.text, 'lxml')
        article_gossiping_seq = []
        for r_ent in soup.find_all(class_="r-ent"):
            try:
                # 先得到每篇文章的篇url
                link = r_ent.find('a')['href']

                if link:
                    # 確定得到url再去抓 標題 以及 推文數
                    title = r_ent.find(class_="title").text.strip()
                    url = 'https://www.ptt.cc' + link
                    article_gossiping_seq.append({
                        'url': url,
                        'title': title
                    })

            except Exception as e:
                # print u'crawPage function error:',r_ent.find(class_="title").text.strip()
                # print('本文已被刪除')
                print('delete', e)
        Total = ''
        for i in range(len(article_gossiping_seq)):
            Total += article_gossiping_seq[i]['title'] + '\n'
            Total += (article_gossiping_seq[i]['url']) + '\n'
            Total += ('-----------------------------------------------------') + '\n'
        return Total

    # ----------------------------------------------------------------------------------------------
    # ptt 熱門
    def Ptt_Hot(self):
        target_url = 'http://disp.cc/b/PttHot'
        print('Start parsing Ptt_Hot....')
        rs = requests.session()
        res = rs.get(target_url, cookies={'over18': '1'})
        soup = BeautifulSoup(res.text, 'lxml')
        content = ""
        for data in soup.select('#list div.row2 div span.listTitle'):
            title = data.text
            link = "http://disp.cc/b/" + data.find('a')['href']
            if data.find('a')['href'] == "796-59l9":
                break
            content += '{}\n{}\n\n'.format(title, link)
        return content

    # ----------------------------------------------------------------------------------------------
    # 取得每一個版的連結
    def Get_All_Ptt_Board(self):
        url = 'https://www.ptt.cc/bbs/index.html'
        print('Start parsing \t' + url)
        rs = requests.session()
        res = rs.get(url, cookies={'over18': '1'})
        soup = BeautifulSoup(res.text, 'lxml')
        Total = ''
        for b in soup.find_all('a'):
            x = b.get_text().split()
            if (len(x) < 2):
                continue
            else:
                count = 0
                for add in x:
                    if (count == 0):
                        Total += '版名: ' + add + ' '
                    if (count == 1):
                        Total += '今日文章數: ' + add + ' '
                    if (count == 2):
                        Total += '分類: ' + add + ' '
                    if (count == 3):
                        Total += '公告: ' + add + ' '
                    elif (count > 3):
                        Total += add + ' '
                    count += 1
                Total += '\n'
            Total += ('https://www.ptt.cc/' + b.get('href')) + '\n'
        return Total

    # 取得 控制頁面選項: 最舊/上頁/下頁/最新
    def Get_Page_Options(self, url='https://www.ptt.cc/bbs/C_Chat/index.html'):
        url = url
        rs = requests.session()
        res = rs.get(url, cookies={'over18': '1'})
        soup = BeautifulSoup(res.text, 'lxml')
        # 控制頁面選項: 最舊/上頁/下頁/最新
        Page_Options = []
        for controls in soup.select('.action-bar a.btn.wide'):
            link = str(controls.get('href'))
            Page_Options.append('https://www.ptt.cc' + link)
        return Page_Options

    # ----------------------------------------------------------------------------------------------
    '''依照ptt版的url 搜尋文章  低於 push_rate 評分的不出現
    title : 標題
    url : 連結
    rate : 推文
    author : 作者
    date : 日期
    回傳 {title':title,  'url':url,  'rate':rate ,'author':author ,'date': date}
    '''

    def Craw_Page_All_Data(self, url='https://www.ptt.cc/bbs/C_Chat/index.html', push_rate=10):
        print('Start parsing \t' + url)
        rs = requests.session()
        res = rs.get(url, cookies={'over18': '1'})
        soup_ = BeautifulSoup(res.text, 'lxml')
        article_seq = []
        for r_ent in soup_.find_all(class_="r-ent"):
            try:
                # 先得到每篇文章的篇url
                link = r_ent.find('a')['href']
                if link:
                    # 確定得到url再去抓 標題 以及 推文數
                    title = r_ent.find(class_="title").text.strip()
                    rate = r_ent.find(class_="nrec").text
                    url = 'https://www.ptt.cc' + link
                    author = r_ent.find(class_="author").text
                    date = r_ent.find(class_="date").text
                    if rate:
                        rate = 100 if rate.startswith('爆') else rate
                        rate = -1 * int(rate[1]) if rate.startswith('X') else rate
                    else:
                        rate = 0
                    # 比對推文數
                    if int(rate) >= push_rate:
                        article_seq.append({
                            'title': title,
                            'url': url,
                            'rate': rate,
                            'author': author,
                            'date': date
                        })
            except Exception as e:
                # print('crawPage function error:',r_ent.find(class_="title").text.strip())
                print('本文已被刪除', e)
        Total = ''
        for i in range(len(article_seq)):
            Total += article_seq[i]['title'] + '\n'
            Total += (article_seq[i]['url']) + '\n'
            Total += ('推文數 : ' + article_seq[i]['rate']) + '\n'
            Total += ('作者 : ' + article_seq[i]['author']) + '\n'
            Total += ('日期 : ' + article_seq[i]['date']) + '\n'
            Total += ('-----------------------------------------------------') + '\n'
        return Total
# ----------------------------------------------------------------------------------------------
