import random

import requests
from bs4 import BeautifulSoup


class EynyCrawler():

    def __init__(self):
        self.Prefix = 'http://www.eyny.com/'
        self.Taget_Url = [
            # 吹水聊天室
            'http://www.eyny.com/forum-27-1.html',
            # 網友交友區
            'http://www.eyny.com/forum-88-1.html',
            # 靈異鬼故事
            'http://www.eyny.com/forum-30-1.html',
            # 生活百科及冷知識
            'http://www.eyny.com/forum-68-1.html',
            # IQ題猜迷語
            'http://www.eyny.com/forum-102-1.html',
            # 趣味笑話區
            'http://www.eyny.com/forum-54-1.html',
            # 性教育專區
            'http://www.eyny.com/forum-210-1.html',
            # 布袋戲討論
            'http://www.eyny.com/forum-1609-1.html',
            # 知識問與答
            'http://www.eyny.com/forum-1723-1.html',
            # 當兵生活趣談
            'http://www.eyny.com/forum-1758-1.html',
            # 海外生活
            'http://www.eyny.com/forum-1763-1.html',
            # 活動中心
            'http://www.eyny.com/forum-2037-1.html',
            # 投票中心
            'http://www.eyny.com/forum-3181-1.html',
            # 其他興趣討論
            'http://www.eyny.com/forum-1721-1.html',
            # 模型和玩具
            'http://www.eyny.com/forum-152-1.html',
            # 魔術討論區
            'http://www.eyny.com/forum-244-1.html',
            # 攝影交流
            'http://www.eyny.com/forum-383-1.html',
            # 卡牌交流
            'http://www.eyny.com/forum-381-1.html',
            # 棋藝交流
            'http://www.eyny.com/forum-382-1.html',
            # 釣魚交流
            'http://www.eyny.com/forum-455-1.html',
            # 天文地理交流
            'http://www.eyny.com/forum-442-1.html',
            # War Games 交流
            'http://www.eyny.com/forum-456-1.html',
            # 紙藝小築/摺紙手工
            'http://www.eyny.com/forum-502-1.html',
            # 風水玄學及掌相命理
            'http://www.eyny.com/forum-468-1.html',
            # 園藝交流
            'http://www.eyny.com/forum-499-1.html',
            # 巴士迷專區
            'http://www.eyny.com/forum-500-1.html',
            # 舞蹈交流
            'http://www.eyny.com/forum-498-1.html',
            # 機車交流
            'http://www.eyny.com/forum-501-1.html',
            # 藝術及繪畫
            'http://www.eyny.com/forum-504-1.html',
            # 汽車交流
            'http://www.eyny.com/forum-505-1.html',
            # 會員寫作專欄
            'http://www.eyny.com/forum-470-1.html',
            # 大學生活交流
            'http://www.eyny.com/forum-363-1.html',
            # 中學生活交流
            'http://www.eyny.com/forum-162-1.html',
            # 小學生活交流
            'http://www.eyny.com/forum-364-1.html',
            # 各類考試討論
            'http://www.eyny.com/forum-362-1.html',
            # 中國文學
            'http://www.eyny.com/forum-408-1.html',
            # 科學討論
            'http://www.eyny.com/forum-407-1.html',
            # 哲學討論
            'http://www.eyny.com/forum-358-1.html',
            # 心靈小品 (短篇)
            'http://www.eyny.com/forum-89-1.html',
            # 好書推介及閱讀感想
            'http://www.eyny.com/forum-409-1.html',
            # 歷史討論
            'http://www.eyny.com/forum-149-1.html',
            # 宗教討論
            'http://www.eyny.com/forum-221-1.html',
            # 藝術交流
            'http://www.eyny.com/forum-508-1.html',
            # 日本文化
            'http://www.eyny.com/forum-522-1.html',
            # 英語學習坊
            'http://www.eyny.com/forum-1730-1.html',
            # 留學遊學交流
            'http://www.eyny.com/forum-1757-1.html',
            # 神話傳說
            'http://www.eyny.com/forum-1759-1.html',
            # 旅遊風光相簿
            'http://www.eyny.com/forum-202-1.html',
            # 旅遊經驗交流
            'http://www.eyny.com/forum-512-1.html',
            # 世界遊樂園討論區
            'http://www.eyny.com/forum-419-1.html',
            # 中國/澳門/台灣
            'http://www.eyny.com/forum-513-1.html',
            # 日本/韓國
            'http://www.eyny.com/forum-514-1.html',
            # 歐洲/美洲/非洲/其他
            'http://www.eyny.com/forum-515-1.html',
            # 東南亞/澳洲/紐西蘭
            'http://www.eyny.com/forum-516-1.html',
            # 美味食譜
            'http://www.eyny.com/forum-191-1.html',
            # 食店及飲食討論
            'http://www.eyny.com/forum-517-1.html',
            # 健康飲食
            'http://www.eyny.com/forum-518-1.html',
            # 廚藝烹飪
            'http://www.eyny.com/forum-519-1.html',
            # 世界美食討論
            'http://www.eyny.com/forum-1729-1.html',
            # 零食討論
            'http://www.eyny.com/forum-1728-1.html',
            # 品茶茶藝
            'http://www.eyny.com/forum-1727-1.html',
            # 咖啡
            'http://www.eyny.com/forum-1726-1.html',
            # 紅酒白酒及其他酒類
            'http://www.eyny.com/forum-1725-1.html',
            # 婚姻大事
            'http://www.eyny.com/forum-509-1.html',
            # 家居佈置
            'http://www.eyny.com/forum-510-1.html',
            # 置業租屋
            'http://www.eyny.com/forum-511-1.html',
            # 育兒父母區
            'http://www.eyny.com/forum-427-1.html',
            # 家庭生活
            'http://www.eyny.com/forum-1717-1.html',
            # 家事傾訴
            'http://www.eyny.com/forum-1718-1.html',
            # 電玩單機遊戲情報討論
            'http://www.eyny.com/forum-209-1.html',
            # minecraft(當個創世神)
            'http://www.eyny.com/forum-3336-1.html',
            # 戰慄時空之絕對武力(CS)
            'http://www.eyny.com/forum-86-1.html',
            # 絕地求生 PUBG
            'http://www.eyny.com/forum-4438-1.html',
            # Don’t starve
            'http://www.eyny.com/forum-4492-1.html',
            # 邊緣世界
            'http://www.eyny.com/forum-4439-1.html',
            # 榮耀戰魂
            'http://www.eyny.com/forum-4291-1.html',
            # NEKOPARA
            'http://www.eyny.com/forum-4292-1.html',
            # 看門狗 Watch Dogs
            'http://www.eyny.com/forum-4202-1.html',
            # 湯姆克蘭西：全境封鎖
            'http://www.eyny.com/forum-4095-1.html',
            # 上古卷軸 系列(The Elder Scrolls)
            'http://www.eyny.com/forum-3279-1.html',
            # 東方project
            'http://www.eyny.com/forum-1823-1.html',
            # H-game討論區
            'http://www.eyny.com/forum-1946-1.html',
            # 大富翁遊戲系列
            'http://www.eyny.com/forum-2018-1.html',
            # 超次元戰記●戰機少女
            'http://www.eyny.com/forum-4042-1.html',
            # RPG製作大師
            'http://www.eyny.com/forum-4044-1.html',
            # 策略模擬遊戲
            'http://www.eyny.com/forum-1939-1.html',
            # 輕Gal Game
            'http://www.eyny.com/forum-1938-1.html',
            # 射擊競技遊戲
            'http://www.eyny.com/forum-1940-1.html',
            # 角色扮演遊戲
            'http://www.eyny.com/forum-1941-1.html',
            # 運動/競速遊戲
            'http://www.eyny.com/forum-1942-1.html',
            # 格鬥技術遊戲
            'http://www.eyny.com/forum-1987-1.html',
            # 冒險/動作遊戲
            'http://www.eyny.com/forum-2008-1.html',
            # 魔獸爭霸系列
            'http://www.eyny.com/forum-273-1.html',
            # 音樂節奏遊戲
            'http://www.eyny.com/forum-2011-1.html',
            # PC GAME 歷史回憶區
            'http://www.eyny.com/forum-2007-1.html',
            # 電視遊樂器相關討論
            'http://www.eyny.com/forum-387-1.html',
            # 任天堂 Switch
            'http://www.eyny.com/forum-4290-1.html',
            # Wii U 遊戲討論
            'http://www.eyny.com/forum-1701-1.html',
            # Xbox 360 遊戲討論
            'http://www.eyny.com/forum-1702-1.html',
            # PS4 / PlayStation4
            'http://www.eyny.com/forum-388-1.html',
            # PSV/ PlayStation Vita
            'http://www.eyny.com/forum-4135-1.html',
            # NDS / Nintendo DS
            'http://www.eyny.com/forum-386-1.html',
            # iPod / iPhone 綜合遊戲
            'http://www.eyny.com/forum-1950-1.html',
            # ARPG無雙系列
            'http://www.eyny.com/forum-1973-1.html',
            # 俠盜獵車手(GTA)
            'http://www.eyny.com/forum-3915-1.html',
            # 惡靈古堡系列
            'http://www.eyny.com/forum-1971-1.html',
            # 神奇寶貝
            'http://www.eyny.com/forum-1709-1.html',
            # 魔物獵人(M.H.)
            'http://www.eyny.com/forum-1703-1.html',
            # 惡魔獵人
            'http://www.eyny.com/forum-1707-1.html',
            # 時空幻境 系列
            'http://www.eyny.com/forum-1705-1.html',
            # 遊戲王系列
            'http://www.eyny.com/forum-1993-1.html',
            # TV GAME 歷史回憶區
            'http://www.eyny.com/forum-3916-1.html',
            # 英雄聯盟League of Legends
            'http://www.eyny.com/forum-1970-1.html',
            # 暴雪英霸
            'http://www.eyny.com/forum-3887-1.html',
            # 暗黑破壞神3：奪魂之鐮
            'http://www.eyny.com/forum-1710-1.html',
            # 黑色沙漠 BLACK DESERT
            'http://www.eyny.com/forum-4259-1.html',
            # 救世主之樹 Tree of Savior
            'http://www.eyny.com/forum-3969-1.html',
            # 鬥陣特攻 Overwatch
            'http://www.eyny.com/forum-4128-1.html',
            # DMM綜合遊戲
            'http://www.eyny.com/forum-3311-1.html',
            # 新楓之谷 Online
            'http://www.eyny.com/forum-1692-1.html',
            # 流亡黯道 Path of Exile
            'http://www.eyny.com/forum-3503-1.html',
            # A.V.A 戰地之王 Revo
            'http://www.eyny.com/forum-1999-1.html',
            # 天堂 Lineage系列
            'http://www.eyny.com/forum-113-1.html',
            # 戰艦世界World of Warships
            'http://www.eyny.com/forum-3908-1.html',
            # CS Online(絕對武力)
            'http://www.eyny.com/forum-1786-1.html',
            # 艾爾之光
            'http://www.eyny.com/forum-1905-1.html',
            # 爐石戰記：魔獸英雄傳
            'http://www.eyny.com/forum-3702-1.html',
            # 仙境傳說RO系列
            'http://www.eyny.com/forum-31-1.html',
            # 魔獸世界 WOW
            'http://www.eyny.com/forum-294-1.html',
            # 戰車世界 World of Tanks
            'http://www.eyny.com/forum-3573-1.html',
            # 劍靈Blade & Soul
            'http://www.eyny.com/forum-3304-1.html',
            # 新瑪奇英雄傳
            'http://www.eyny.com/forum-3306-1.html',
            # 全民打棒球 2
            'http://www.eyny.com/forum-1633-1.html',
            # Pixiv角色創作專區
            'http://www.eyny.com/forum-3505-1.html',
            # 艦隊提督鎮守府創作區
            'http://www.eyny.com/forum-3909-1.html',
            # 角色扮演類〈MMORPG〉
            'http://www.eyny.com/forum-3910-1.html',
            # 手機/平板遊戲情報特搜
            'http://www.eyny.com/forum-3889-1.html',
            # 網路遊戲情報討論區
            'http://www.eyny.com/forum-139-1.html',
            # 神魔之塔
            'http://www.eyny.com/forum-3577-1.html',
            # 天堂手遊系列
            'http://www.eyny.com/forum-4375-1.html',
            # 龍族拼圖 Puzzle & Dragons
            'http://www.eyny.com/forum-3578-1.html',
            # 超異域公主連結☆ReDive
            'http://www.eyny.com/forum-4495-1.html',
            # 關於我轉生變成史萊姆這檔事
            'http://www.eyny.com/forum-4494-1.html',
            # 在地下城尋求邂逅是否搞錯了什麼
            'http://www.eyny.com/forum-4493-1.html',
            # 碧藍航線
            'http://www.eyny.com/forum-4411-1.html',
            # 崩壞3rd
            'http://www.eyny.com/forum-4565-1.html',
            # Garena 極速領域
            'http://www.eyny.com/forum-4564-1.html',
            # 闇影詩章(Shadowverse)
            'http://www.eyny.com/forum-4315-1.html',
            # 精靈寶可夢 GO
            'http://www.eyny.com/forum-4156-1.html',
            # 白貓Project
            'http://www.eyny.com/forum-3818-1.html',
            # 碧藍幻想
            'http://www.eyny.com/forum-4293-1.html',
            # 偶像大師灰姑娘女孩
            'http://www.eyny.com/forum-4203-1.html',
            # 陰陽師 Onmyoji
            'http://www.eyny.com/forum-4261-1.html',
            # 少女前線
            'http://www.eyny.com/forum-4262-1.html',
            # Garena 傳說對決
            'http://www.eyny.com/forum-4223-1.html',
            # 召喚圖板 Summons Board
            'http://www.eyny.com/forum-4098-1.html',
            # 怪物彈珠
            'http://www.eyny.com/forum-3703-1.html',
            # 鎖鏈戰記 CHAIN CHRONICLE
            'http://www.eyny.com/forum-3777-1.html',
            # Line遊戲系列討論版
            'http://www.eyny.com/forum-3705-1.html',
            # 部落衝突Clash of Clans
            'http://www.eyny.com/forum-3855-1.html',
            # Fate/Grand Order
            'http://www.eyny.com/forum-1954-1.html',
            # 日系手遊討論
            'http://www.eyny.com/forum-3911-1.html',
            # 國產手遊討論
            'http://www.eyny.com/forum-3316-1.html',
            # 其他手遊討論
            'http://www.eyny.com/forum-3317-1.html',
            # 動畫(アニメ)改編討論
            'http://www.eyny.com/forum-1880-1.html',
            # 私服討論區
            'http://www.eyny.com/forum-1631-1.html',
            # 線上遊戲歷史回憶區
            'http://www.eyny.com/forum-2027-1.html',
            # 塔羅及占卜
            'http://www.eyny.com/forum-308-1.html',
            # 星座心理區
            'http://www.eyny.com/forum-56-1.html',
            # 愛情討論區
            'http://www.eyny.com/forum-42-1.html',
            # 心情日記區
            'http://www.eyny.com/forum-40-1.html',
            # 夢想與理想
            'http://www.eyny.com/forum-304-1.html',
            # 小小祈願池
            'http://www.eyny.com/forum-418-1.html',
            # 寵物新資訊
            'http://www.eyny.com/forum-1745-1.html',
            # 其他寵物討論
            'http://www.eyny.com/forum-506-1.html',
            # 狗狗
            'http://www.eyny.com/forum-1740-1.html',
            # 貓貓
            'http://www.eyny.com/forum-1741-1.html',
            # 爬蟲兩棲
            'http://www.eyny.com/forum-1744-1.html',
            # 鼠類/兔類/龍貓類等
            'http://www.eyny.com/forum-1743-1.html',
            # 雀鳥
            'http://www.eyny.com/forum-1742-1.html',
            # 水族養魚樂
            'http://www.eyny.com/forum-503-1.html',
            # 寵物貼圖
            'http://www.eyny.com/forum-160-1.html',
            # NBA籃球大聯盟
            'http://www.eyny.com/forum-236-1.html',
            # ♀㊣白痴１族☆♂
            'http://www.eyny.com/forum-264-1.html',
            # ζˋ緣份網絡ˊζ
            'http://www.eyny.com/forum-282-1.html',
            # 動漫交流の佈告欄
            'http://www.eyny.com/forum-4504-1.html',
            # 動漫新資訊
            'http://www.eyny.com/forum-479-1.html',
            # 綜合動漫討論區
            'http://www.eyny.com/forum-3500-1.html',
            # 新番動漫討論區
            'http://www.eyny.com/forum-1832-1.html',
            # 動漫輕小說
            'http://www.eyny.com/forum-1681-1.html',
            # 銀魂
            'http://www.eyny.com/forum-1682-1.html',
            # 五等分的花嫁
            'http://www.eyny.com/forum-4597-1.html',
            # 刺客守則
            'http://www.eyny.com/forum-4598-1.html',
            # 刀劍神域
            'http://www.eyny.com/forum-3352-1.html',
            # 火影忍者
            'http://www.eyny.com/forum-433-1.html',
            # ONE PIECE 航海王(海賊王)
            'http://www.eyny.com/forum-434-1.html',
            # 食戟之靈
            'http://www.eyny.com/forum-4138-1.html',
            # 名偵探柯南
            'http://www.eyny.com/forum-439-1.html',
            # 國漫系列
            'http://www.eyny.com/forum-4599-1.html',
            # 機械人討論區
            'http://www.eyny.com/forum-440-1.html',
            # Fate系列
            'http://www.eyny.com/forum-3832-1.html',
            # 轉生/穿越系列
            'http://www.eyny.com/forum-4491-1.html',
            # UQ HOLDER!/悠久之風(赤松健作品系列)
            'http://www.eyny.com/forum-1688-1.html',
            # 京都動畫(京阿尼)系列作品
            'http://www.eyny.com/forum-4234-1.html',
            # 聲優園地
            'http://www.eyny.com/forum-525-1.html',
            # 分級萌動學術院
            'http://www.eyny.com/forum-4385-1.html',
            # 綜合討論&新版宣傳
            'http://www.eyny.com/forum-212-1.html',
            # 科幻/魔法類討論
            'http://www.eyny.com/forum-1842-1.html',
            # 戀愛/校園類討論
            'http://www.eyny.com/forum-1843-1.html',
            # 奇幻/冒險類討論
            'http://www.eyny.com/forum-1844-1.html',
            # 推理/靈異類討論
            'http://www.eyny.com/forum-1889-1.html',
            # 運動/競技類討論
            'http://www.eyny.com/forum-1845-1.html',
            # 動漫討論歷史回憶區
            'http://www.eyny.com/forum-3733-1.html',
            # 動漫精品交流
            'http://www.eyny.com/forum-526-1.html',
            # COSPLAY交流
            'http://www.eyny.com/forum-432-1.html',
            # 初音家族Vocaloid
            'http://www.eyny.com/forum-1835-1.html',
            # ACG 動漫隨意貼圖
            'http://www.eyny.com/forum-16-1.html',
            # HCG-H動漫隨意貼圖
            'http://www.eyny.com/forum-150-1.html',
            # 漫畫分享版
            'http://www.eyny.com/forum-1627-1.html',
            # 動漫音樂下載(上傳空間)
            'http://www.eyny.com/forum-207-1.html',
            # 動漫套圖下載區(上傳空間)
            'http://www.eyny.com/forum-4136-1.html',
            # H 動畫下載區(上傳空間)
            'http://www.eyny.com/forum-431-1.html',
            # H 漫畫下載區(上傳空間)
            'http://www.eyny.com/forum-1629-1.html',
            # 中文H漫畫貼圖
            'http://www.eyny.com/forum-349-1.html',
            # 日文H漫畫貼圖
            'http://www.eyny.com/forum-350-1.html',
            # 英文H漫畫貼圖
            'http://www.eyny.com/forum-3208-1.html',
            # 動漫下載求檔&問題區
            'http://www.eyny.com/forum-3707-1.html',
            # 搞笑貼圖區
            'http://www.eyny.com/forum-15-1.html',
            # 網友自拍館
            'http://www.eyny.com/forum-14-1.html',
            # 正妹美眉區
            'http://www.eyny.com/forum-17-1.html',
            # 型男帥哥區
            'http://www.eyny.com/forum-520-1.html',
            # DIY作品貼圖區
            'http://www.eyny.com/forum-521-1.html',
            # 網頁素材區
            'http://www.eyny.com/forum-307-1.html',
            # 電腦桌布分享
            'http://www.eyny.com/forum-359-1.html',
            # BL-GL討論
            'http://www.eyny.com/forum-480-1.html',
            # BL-GL貼圖
            'http://www.eyny.com/forum-482-1.html',
            # BL-GL小說
            'http://www.eyny.com/forum-1676-1.html',
            # BL-GL衍生
            'http://www.eyny.com/forum-523-1.html',
            # BL-GL下載
            'http://www.eyny.com/forum-524-1.html',
            # BL-GL短片
            'http://www.eyny.com/forum-1807-1.html',
            # 音樂新資訊
            'http://www.eyny.com/forum-1680-1.html',
            # 其他音樂討論
            'http://www.eyny.com/forum-378-1.html',
            # 華語樂壇討論
            'http://www.eyny.com/forum-527-1.html',
            # 日韓樂壇討論
            'http://www.eyny.com/forum-528-1.html',
            # 外語樂壇討論
            'http://www.eyny.com/forum-529-1.html',
            # 音樂單曲下載
            'http://www.eyny.com/forum-530-1.html',
            # 音樂專輯下載
            'http://www.eyny.com/forum-203-1.html',
            # 無損音樂下載
            'http://www.eyny.com/forum-4442-1.html',
            # MTV和KTV下載
            'http://www.eyny.com/forum-379-1.html',
            # 樂譜與樂器專區
            'http://www.eyny.com/forum-204-1.html',
            # 歌詞分享
            'http://www.eyny.com/forum-85-1.html',
            # 會員唱作區
            'http://www.eyny.com/forum-531-1.html',
            # 音樂世界求檔&問題區
            'http://www.eyny.com/forum-4012-1.html',
            # 港台明星貼圖
            'http://www.eyny.com/forum-322-1.html',
            # 日韓明星貼圖
            'http://www.eyny.com/forum-321-1.html',
            # 外國明星貼圖
            'http://www.eyny.com/forum-29-1.html',
            # 電視節目討論
            'http://www.eyny.com/forum-444-1.html',
            # 電台節目討論
            'http://www.eyny.com/forum-443-1.html',
            # 電影討論區
            'http://www.eyny.com/forum-410-1.html',
            # 電視連續劇討論區
            'http://www.eyny.com/forum-327-1.html',
            # 美容討論
            'http://www.eyny.com/forum-375-1.html',
            # 化妝討論
            'http://www.eyny.com/forum-374-1.html',
            # 減肥瘦身
            'http://www.eyny.com/forum-279-1.html',
            # 女性用品
            'http://www.eyny.com/forum-1734-1.html',
            # 內衣
            'http://www.eyny.com/forum-1733-1.html',
            # 女人心事
            'http://www.eyny.com/forum-1731-1.html',
            # 珠寶首飾
            'http://www.eyny.com/forum-1732-1.html',
            # 女性健康分享
            'http://www.eyny.com/forum-1735-1.html',
            # 指甲彩繪
            'http://www.eyny.com/forum-1736-1.html',
            # 髮型討論
            'http://www.eyny.com/forum-377-1.html',
            # 鐘錶討論
            'http://www.eyny.com/forum-451-1.html',
            # 球鞋討論
            'http://www.eyny.com/forum-450-1.html',
            # 潮流服飾討論
            'http://www.eyny.com/forum-201-1.html',
            # 牛仔服飾
            'http://www.eyny.com/forum-1738-1.html',
            # 錢包手袋
            'http://www.eyny.com/forum-1737-1.html',
            # 二手衣飾交易
            'http://www.eyny.com/forum-532-1.html',
            # BT體育運動下載區
            'http://www.eyny.com/forum-540-1.html',
            # BT軟件下載區
            'http://www.eyny.com/forum-58-1.html',
            # BT遊戲下載區
            'http://www.eyny.com/forum-62-1.html',
            # BT音樂下載區
            'http://www.eyny.com/forum-141-1.html',
            # BT H遊戲下載區
            'http://www.eyny.com/forum-1630-1.html',
            # BT H動漫下載區
            'http://www.eyny.com/forum-346-1.html',
            # BT日韓成人電影
            'http://www.eyny.com/forum-140-1.html',
            # BT歐美成人電影
            'http://www.eyny.com/forum-345-1.html',
            # BT求檔&問題區
            'http://www.eyny.com/forum-538-1.html',
            # 軟件下載區(上傳空間)
            'http://www.eyny.com/forum-18-1.html',
            # 遊戲下載區(上傳空間)
            'http://www.eyny.com/forum-26-1.html',
            # GalGame遊戲下載區(上傳空間)
            'http://www.eyny.com/forum-3691-1.html',
            # H 遊戲下載區(上傳空間)
            'http://www.eyny.com/forum-48-1.html',
            # 軟件下載區(會員制空間)
            'http://www.eyny.com/forum-4478-1.html',
            # 遊戲下載區(會員制空間)
            'http://www.eyny.com/forum-3523-1.html',
            # 圖文遊戲下載區(會員制空間)
            'http://www.eyny.com/forum-4479-1.html',
            # H 遊戲下載區(會員制空間)
            'http://www.eyny.com/forum-4480-1.html',
            # 電子書下載區
            'http://www.eyny.com/forum-1982-1.html',
            # 小說下載區
            'http://www.eyny.com/forum-3752-1.html',
            # FLASH下載區
            'http://www.eyny.com/forum-36-1.html',
            # 下載分享求檔&問題區
            'http://www.eyny.com/forum-537-1.html',
            # 其他短片
            'http://www.eyny.com/forum-1772-1.html',
            # 搞笑短片
            'http://www.eyny.com/forum-313-1.html',
            # 動漫短片
            'http://www.eyny.com/forum-1771-1.html',
            # 寵物短片
            'http://www.eyny.com/forum-1755-1.html',
            # 音樂短片
            'http://www.eyny.com/forum-1748-1.html',
            # 寶貝BB短片
            'http://www.eyny.com/forum-1749-1.html',
            # 網友自拍短片
            'http://www.eyny.com/forum-1750-1.html',
            # 歌星藝人短片
            'http://www.eyny.com/forum-1754-1.html',
            # 感人熱淚短片
            'http://www.eyny.com/forum-1752-1.html',
            # 汽車機車短片
            'http://www.eyny.com/forum-1753-1.html',
            # 體育運動短片
            'http://www.eyny.com/forum-1751-1.html',
            # 電腦新資訊
            'http://www.eyny.com/forum-390-1.html',
            # 電腦軟體討論
            'http://www.eyny.com/forum-53-1.html',
            # 電腦軟體資訊分享
            'http://www.eyny.com/forum-546-1.html',
            # 電腦硬體討論
            'http://www.eyny.com/forum-389-1.html',
            # 電腦硬體資訊分享
            'http://www.eyny.com/forum-1815-1.html',
            # 電腦萌化版
            'http://www.eyny.com/forum-1964-1.html',
            # 電腦系統 OS 討論
            'http://www.eyny.com/forum-391-1.html',
            # 電腦程式設計
            'http://www.eyny.com/forum-392-1.html',
            # 電腦設計技術交流
            'http://www.eyny.com/forum-393-1.html',
            # 圖像設計及交流
            'http://www.eyny.com/forum-445-1.html',
            # 各類下載工具教學
            'http://www.eyny.com/forum-394-1.html',
            # 寬頻上網討論
            'http://www.eyny.com/forum-555-1.html',
            # 平板電腦/iPad
            'http://www.eyny.com/forum-556-1.html',
            # 數碼相機 DC
            'http://www.eyny.com/forum-557-1.html',
            # 數碼攝錄機 DV
            'http://www.eyny.com/forum-558-1.html',
            # 家庭影音 AV
            'http://www.eyny.com/forum-559-1.html',
            # MP3/耳機
            'http://www.eyny.com/forum-560-1.html',
            # iPod
            'http://www.eyny.com/forum-561-1.html',
            # 手提電腦 NoteBook
            'http://www.eyny.com/forum-562-1.html',
            # PPC 交流
            'http://www.eyny.com/forum-563-1.html',
            # 其他數碼產品
            'http://www.eyny.com/forum-95-1.html',
            # 手機討論
            'http://www.eyny.com/forum-94-1.html',
            # 手機選購 (2G + 3G)
            'http://www.eyny.com/forum-396-1.html',
            # 手機鈴聲(非MP3)
            'http://www.eyny.com/forum-398-1.html',
            # 手機鈴聲(MP3)
            'http://www.eyny.com/forum-397-1.html',
            # 手機主題和桌布
            'http://www.eyny.com/forum-399-1.html',
            # 手機遊戲
            'http://www.eyny.com/forum-400-1.html',
            # 手機影片分享
            'http://www.eyny.com/forum-401-1.html',
            # 手機軟件應用程式
            'http://www.eyny.com/forum-402-1.html',
            # 二手交易
            'http://www.eyny.com/forum-211-1.html',
            # 拍賣廣場
            'http://www.eyny.com/forum-376-1.html',
            # 重要公告區
            'http://www.eyny.com/forum-13-1.html',
            # 贊助問題區
            'http://www.eyny.com/forum-1608-1.html',
            # 版主招募區
            'http://www.eyny.com/forum-43-1.html',
            # 新手教學區
            'http://www.eyny.com/forum-45-1.html',
            # 活動交流區
            'http://www.eyny.com/forum-428-1.html',
            # 伊莉影片區
            'http://www.eyny.com/forum-1817-1.html',
            # 伊莉部落格
            'http://www.eyny.com/forum-1813-1.html',
            # 伊莉百科區
            'http://www.eyny.com/forum-1887-1.html',
            # 投訴及意見
            'http://www.eyny.com/forum-44-1.html',
            # 長篇小說交流園地
            'http://www.eyny.com/forum-1806-1.html',
            # 出版類言情小說
            'http://www.eyny.com/forum-1677-1.html',
            # 玄幻魔法小說
            'http://www.eyny.com/forum-1775-1.html',
            # 武俠修真小說
            'http://www.eyny.com/forum-1776-1.html',
            # 科幻偵探小說
            'http://www.eyny.com/forum-1774-1.html',
            # 原創言情小說
            'http://www.eyny.com/forum-1773-1.html',
            # 都市小說
            'http://www.eyny.com/forum-1983-1.html',
            # 輕小說
            'http://www.eyny.com/forum-1777-1.html',
            # 其他小說
            'http://www.eyny.com/forum-430-1.html',
            # 其他運動討論
            'http://www.eyny.com/forum-1672-1.html',
            # 足球討論
            'http://www.eyny.com/forum-372-1.html',
            # 單車討論
            'http://www.eyny.com/forum-1719-1.html',
            # 籃球討論
            'http://www.eyny.com/forum-365-1.html',
            # 田徑討論
            'http://www.eyny.com/forum-1720-1.html',
            # 棒球討論
            'http://www.eyny.com/forum-105-1.html',
            # 羽毛球討論
            'http://www.eyny.com/forum-366-1.html',
            # 乒乓球討論
            'http://www.eyny.com/forum-452-1.html',
            # 撞球(桌球)討論
            'http://www.eyny.com/forum-566-1.html',
            # 健身運動討論
            'http://www.eyny.com/forum-371-1.html',
            # 武術討論
            'http://www.eyny.com/forum-367-1.html',
            # 爬山及遠足討論
            'http://www.eyny.com/forum-373-1.html',
            # 瑜伽討論
            'http://www.eyny.com/forum-567-1.html',
            # 排球討論
            'http://www.eyny.com/forum-568-1.html',
            # 網球/壁球討論
            'http://www.eyny.com/forum-569-1.html',
            # 高爾夫球討論
            'http://www.eyny.com/forum-570-1.html',
            # 職業摔角討論
            'http://www.eyny.com/forum-564-1.html',
            # 潛水討論
            'http://www.eyny.com/forum-565-1.html',
            # 時事討論
            'http://www.eyny.com/forum-1724-1.html',
            # 明星新聞討論
            'http://www.eyny.com/forum-412-1.html',
            # 有趣新聞
            'http://www.eyny.com/forum-1760-1.html',
            # 企業家管理交流
            'http://www.eyny.com/forum-447-1.html',
            # 金融財經、投資交流
            'http://www.eyny.com/forum-449-1.html',
            # 房地產討論
            'http://www.eyny.com/forum-571-1.html',
            # 股票討論
            'http://www.eyny.com/forum-573-1.html',
            # 基金保險
            'http://www.eyny.com/forum-1762-1.html',
            # 外幣投資
            'http://www.eyny.com/forum-1761-1.html',
            # 租屋資訊
            'http://www.eyny.com/forum-1764-1.html',
            # 環境保護問題探討
            'http://www.eyny.com/forum-1770-1.html',
            # 食物衛生及用品安全
            'http://www.eyny.com/forum-1769-1.html',
            # 軍事討論
            'http://www.eyny.com/forum-572-1.html',
            # 上班樂與怒
            'http://www.eyny.com/forum-303-1.html',
            # 工作薪酬討論
            'http://www.eyny.com/forum-467-1.html',
            # 創業討論區
            'http://www.eyny.com/forum-446-1.html',
            # 網路賺錢
            'http://www.eyny.com/forum-574-1.html',
            # 各行各業
            'http://www.eyny.com/forum-575-1.html',
            # 求職者交流
            'http://www.eyny.com/forum-1765-1.html',
            # 兼職工讀交流
            'http://www.eyny.com/forum-1767-1.html',
            # 人力銀行(提供職位資訊)
            'http://www.eyny.com/forum-1768-1.html',
            # 兩性討論
            'http://www.eyny.com/forum-156-1.html',
            # 夜遊討論
            'http://www.eyny.com/forum-335-1.html',
            # 成人交友
            'http://www.eyny.com/forum-336-1.html',
            # 成人貼圖
            'http://www.eyny.com/forum-577-1.html',
            # 成人電影(上傳空間)
            'http://www.eyny.com/forum-576-1.html',
            # 成人小說
            'http://www.eyny.com/forum-6-1.html',
            # 足球投注
            'http://www.eyny.com/forum-351-1.html',
            # 虛擬足球投注站
            'http://www.eyny.com/forum-606-1.html',
            # 香港賽馬
            'http://www.eyny.com/forum-354-1.html',
            # 賭場討論
            'http://www.eyny.com/forum-355-1.html',
            # 麻雀耍樂
            'http://www.eyny.com/forum-357-1.html',
            # 撲克交流
            'http://www.eyny.com/forum-356-1.html'
        ]

    # ----------------------------------------------------------------------------------------------
    # 通用的Eyny板貼文取得格式
    def Normal_Get(self, Index):
        Total = ''

        try:

            rs = requests.session()
            res = rs.get(self.Taget_Url[Index], verify=False,
                         cookies={'613e55XbD_e8d7_agree': '1', '613e55XbD_e8d7_indexview': 'all',
                                  '613e55XbD_e8d7_videoadult': '1', '613e55XbD_e8d7_visitedfid': '150D4044D1741D1970'})
            print(rs.cookies.get_dict())
            soup = BeautifulSoup(res.text, 'html.parser')

        except Exception as Errr:
            raise Errr

        if res.status_code == 200:
            for index, data in enumerate(soup.select('div.bm_c tbody th.new a.xst')):
                if ('lastpost' not in data['href'] and 'typeid=' not in data['href']):
                    Total += (data.string) + '\n'
                    Total += (self.Prefix + data['href']) + '\n'
        return Total

    # 通用的Eyny板貼文取得格式
    def Normal_Get_URL(self, URL):
        Total = ''

        try:

            rs = requests.session()
            res = rs.get(URL, verify=False,
                         cookies={'613e55XbD_e8d7_agree': '1', '613e55XbD_e8d7_indexview': 'all',
                                  '613e55XbD_e8d7_videoadult': '1', '613e55XbD_e8d7_visitedfid': '150D4044D1741D1970'})
            print(rs.cookies.get_dict())
            soup = BeautifulSoup(res.text, 'html.parser')

        except Exception as Errr:
            raise Errr

        if res.status_code == 200:

            for index, data in enumerate(soup.select('div.bm_c tbody th.new a.xst')):
                if ('lastpost' not in data['href'] and 'typeid=' not in data['href']):
                    Total += (data.string) + '\n'
                    Total += (self.Prefix + data['href']) + '\n'

        return Total

    # ----------------------------------------------------------------------------------------------
    # 取得所有版的連結
    def Get_All_URL(self):
        Total = ''

        try:

            Get_All_Url = 'http://www.eyny.com/forum.php'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
            rs = requests.session()
            res = rs.get(Get_All_Url, cookies={'613e55XbD_e8d7_agree': '1', '613e55XbD_e8d7_indexview': 'all',
                                               '613e55XbD_e8d7_videoadult': '1',
                                               '613e55XbD_e8d7_visitedfid': '150D4044D1741D1970'})
            print(rs.cookies.get_dict())
            soup = BeautifulSoup(res.text, 'html.parser')

        except Exception as Errr:
            raise Errr

        if res.status_code == 200:

            for index, data in enumerate(soup.select('div.wp.cl div.mn li.li_blue a')):
                Total += (data.string) + '\n'
                Total += (self.Prefix + data['href']) + '\n'

        return Total

    # ----------------------------------------------------------------------------------------------
    # 吹水聊天室
    def Eyny_Chat(self):
        return self.Normal_Get(0)

    # 網友交友區
    def Eyny_InternetFriend(self):
        return self.Normal_Get(1)

    # 靈異鬼故事
    def Eyny_GhostStory(self):
        return self.Normal_Get(2)

    # 生活百科及冷知識
    def Eyny_LifeEncyclopedia(self):
        return self.Normal_Get(3)

    # IQ題猜迷語
    def Eyny_IQPuzzle(self):
        return self.Normal_Get(4)

    # 趣味笑話區
    def Eyny_Joke(self):
        return self.Normal_Get(5)

    # 性教育專區
    def Eyny_SexEducation(self):
        return self.Normal_Get(6)

    # 布袋戲討論
    def Eyny_PuppetShow(self):
        return self.Normal_Get(7)

    # 知識問與答
    def Eyny_KnowledgeQA(self):
        return self.Normal_Get(8)

    # 當兵生活趣談
    def Eyny_ArmyJoke(self):
        return self.Normal_Get(9)

    # 海外生活
    def Eyny_ForeignLife(self):
        return self.Normal_Get(10)

    # 活動中心
    def Eyny_ActivityCenter(self):
        return self.Normal_Get(11)

    # 投票中心
    def Eyny_Poll(self):
        return self.Normal_Get(12)

    # 其他興趣討論
    def Eyny_AnotherInterest(self):
        return self.Normal_Get(13)

    # 模型和玩具
    def Eyny_ModelToy(self):
        return self.Normal_Get(14)

    # 魔術討論區
    def Eyny_Magic(self):
        return self.Normal_Get(15)

    # 攝影交流
    def Eyny_Photography(self):
        return self.Normal_Get(16)

    # 卡牌交流
    def Eyny_Card(self):
        return self.Normal_Get(17)

    # 棋藝交流
    def Eyny_Chess(self):
        return self.Normal_Get(18)

    # 釣魚交流
    def Eyny_Fishing(self):
        return self.Normal_Get(19)

    # 天文地理交流
    def Eyny_Astronomy_And_Geography(self):
        return self.Normal_Get(20)

    # War Games 交流
    def Eyny_WarGames(self):
        return self.Normal_Get(21)

    # 紙藝小築/摺紙手工
    def Eyny_PaperArt(self):
        return self.Normal_Get(22)

    # 風水玄學及掌相命理
    def Eyny_Numerology(self):
        return self.Normal_Get(23)

    # 園藝交流
    def Eyny_Gardening(self):
        return self.Normal_Get(24)

    # 巴士迷專區
    def Eyny_Bus(self):
        return self.Normal_Get(25)

    # 舞蹈交流
    def Eyny_Dance(self):
        return self.Normal_Get(26)

    # 機車交流
    def Eyny_Motorcycle(self):
        return self.Normal_Get(27)

    # 藝術及繪畫
    def Eyny_ArtPaint(self):
        return self.Normal_Get(28)

    # 汽車交流
    def Eyny_Car(self):
        return self.Normal_Get(29)

    # 會員寫作專欄
    def Eyny_Write(self):
        return self.Normal_Get(30)

    # 大學生活交流
    def Eyny_University(self):
        return self.Normal_Get(31)

    # 中學生活交流
    def Eyny_HighSchool(self):
        return self.Normal_Get(32)

    # 小學生活交流
    def Eyny_PrimarySchool(self):
        return self.Normal_Get(33)

    # 各類考試討論
    def Eyny_Exam(self):
        return self.Normal_Get(34)

    # 中國文學
    def Eyny_Chinese_Literature(self):
        return self.Normal_Get(35)

    # 科學討論
    def Eyny_Technology(self):
        return self.Normal_Get(36)

    # 哲學討論
    def Eyny_Philosophy(self):
        return self.Normal_Get(37)

    # 心靈小品 (短篇)
    def Eyny_EmpathyBook(self):
        return self.Normal_Get(38)

    # 好書推介及閱讀感想
    def Eyny_GoodBook(self):
        return self.Normal_Get(39)

    # 歷史討論
    def Eyny_History(self):
        return self.Normal_Get(40)

    # 宗教討論
    def Eyny_Religion(self):
        return self.Normal_Get(41)

    # 藝術交流
    def Eyny_ArtChat(self):
        return self.Normal_Get(42)

        # 日本文化

    def Eyny_JapanCulture(self):
        return self.Normal_Get(43)

    # 英語學習坊
    def Eyny_EnglishLearn(self):
        return self.Normal_Get(44)

    # 留學遊學交流
    def Eyny_StudyAbroad(self):
        return self.Normal_Get(45)

    # 神話傳說
    def Eyny_LegendaryStory(self):
        return self.Normal_Get(46)

    # 旅遊風光相簿
    def Eyny_TravelPicture(self):
        return self.Normal_Get(47)

    # 旅遊經驗交流
    def Eyny_TravelExperience(self):
        return self.Normal_Get(48)

    # 世界遊樂園討論區
    def Eyny_AmusementPark(self):
        return self.Normal_Get(49)

    # 中國/澳門/台灣
    def Eyny_China_Macao_Taiwan(self):
        return self.Normal_Get(50)

    # 日本/韓國
    def Eyny_Japan_Korea(self):
        return self.Normal_Get(51)

    # 歐洲/美洲/非洲/其他
    def Eyny_EU_USA_AF(self):
        return self.Normal_Get(52)

    # 東南亞/澳洲/紐西蘭
    def Eyny_SoutheastAsia_Australia_NewZealand(self):
        return self.Normal_Get(53)

    # 美味食譜
    def Eyny_Recipe(self):
        return self.Normal_Get(54)

    # 食店及飲食討論
    def Eyny_Restaurant(self):
        return self.Normal_Get(55)

    # 健康飲食
    def Eyny_HealthyDiet(self):
        return self.Normal_Get(56)

    # 廚藝烹飪
    def Eyny_Cook(self):
        return self.Normal_Get(57)

    # 世界美食討論
    def Eyny_WorldCuisine(self):
        return self.Normal_Get(58)

    # 零食討論
    def Eyny_Snacks(self):
        return self.Normal_Get(59)

    # 品茶茶藝
    def Eyny_Tea(self):
        return self.Normal_Get(60)

    # 咖啡
    def Eyny_Coffee(self):
        return self.Normal_Get(61)

    # 紅酒白酒及其他酒類
    def Eyny_Wine(self):
        return self.Normal_Get(62)

    # 婚姻大事
    def Eyny_Marriage(self):
        return self.Normal_Get(63)

    # 家居佈置
    def Eyny_Decorate(self):
        return self.Normal_Get(64)

    # 置業租屋
    def Eyny_RentHouse(self):
        return self.Normal_Get(65)

    # 育兒父母區
    def Eyny_Parents(self):
        return self.Normal_Get(66)

    # 家庭生活
    def Eyny_FamilyLife(self):
        return self.Normal_Get(67)

    # 家事傾訴
    def Eyny_FamilyChat(self):
        return self.Normal_Get(68)

    # 電玩單機遊戲情報討論
    def Eyny_AloneGame(self):
        return self.Normal_Get(69)

    # minecraft(當個創世神)
    def Eyny_Minecragt(self):
        return self.Normal_Get(70)

    # 戰慄時空之絕對武力(CS)
    def Eyny_CS(self):
        return self.Normal_Get(71)

    # 絕地求生 PUBG
    def Eyny_PUBG(self):
        return self.Normal_Get(72)

    # Don’t starve
    def Eyny_DST(self):
        return self.Normal_Get(73)

    # 邊緣世界
    def Eyny_RimWorld(self):
        return self.Normal_Get(74)

    # 榮耀戰魂
    def Eyny_ForHonor(self):
        return self.Normal_Get(75)

    # NEKOPARA
    def Eyny_NEKOPARA(self):
        return self.Normal_Get(76)

    # 看門狗 Watch Dogs
    def Eyny_WatchDogs(self):
        return self.Normal_Get(77)

    # 湯姆克蘭西：全境封鎖
    def Eyny_TomClancy_TheDivision(self):
        return self.Normal_Get(78)

    # 上古卷軸 系列(The Elder Scrolls)
    def Eyny_The_ElderScrolls(self):
        return self.Normal_Get(79)

    # 東方project
    def Eyny_TouhouProject(self):
        return self.Normal_Get(80)

    # H-game討論區
    def Eyny_HGame(self):
        return self.Normal_Get(81)

    # 大富翁遊戲系列
    def Eyny_Monopoly(self):
        return self.Normal_Get(82)

    # 超次元戰記●戰機少女
    def Eyny_HyperdimensionNeptune(self):
        return self.Normal_Get(83)

    # RPG製作大師
    def Eyny_RPGMaker(self):
        return self.Normal_Get(84)

    # 策略模擬遊戲
    def Eyny_RTS(self):
        return self.Normal_Get(85)

    # 輕Gal Game
    def Eyny_GalGame(self):
        return self.Normal_Get(86)

    # 射擊競技遊戲
    def Eyny_ShootingGame(self):
        return self.Normal_Get(87)

    # 角色扮演遊戲
    def Eyny_RPG(self):
        return self.Normal_Get(88)

    # 運動/競速遊戲
    def Eyny_SportsGame(self):
        return self.Normal_Get(89)

    # 格鬥技術遊戲
    def Eyny_FightGame(self):
        return self.Normal_Get(90)

    # 冒險/動作遊戲
    def Eyny_ActionGame(self):
        return self.Normal_Get(91)

    # 魔獸爭霸系列
    def Eyny_Warcraft(self):
        return self.Normal_Get(92)

    # 音樂節奏遊戲
    def Eyny_MusicGame(self):
        return self.Normal_Get(93)

    # PC GAME 歷史回憶區
    def Eyny_PCGAMEStory(self):
        return self.Normal_Get(94)

    # 電視遊樂器相關討論
    def Eyny_TVGame(self):
        return self.Normal_Get(95)

    # 任天堂 Switch
    def Eyny_Switch(self):
        return self.Normal_Get(96)

    # Wii U 遊戲討論
    def Eyny_Wii(self):
        return self.Normal_Get(97)

    # Xbox 360 遊戲討論
    def Eyny_Xbox(self):
        return self.Normal_Get(98)

    # PS4 / PlayStation4
    def Eyny_PlayStation4(self):
        return self.Normal_Get(99)

    # PSV/ PlayStation Vita
    def Eyny_PlayStationVita(self):
        return self.Normal_Get(100)

    # NDS / Nintendo DS
    def Eyny_NDS(self):
        return self.Normal_Get(101)

    # iPod / iPhone 綜合遊戲
    def Eyny_iPod(self):
        return self.Normal_Get(102)

    # ARPG無雙系列
    def Eyny_ARPG(self):
        return self.Normal_Get(103)

    # 俠盜獵車手(GTA)
    def Eyny_GTA(self):
        return self.Normal_Get(104)

    # 惡靈古堡系列
    def Eyny_ResidentEvil(self):
        return self.Normal_Get(105)

    # 神奇寶貝
    def Eyny_Pokemon(self):
        return self.Normal_Get(106)

    # 魔物獵人(M.H.)
    def Eyny_MH(self):
        return self.Normal_Get(107)

    # 惡魔獵人
    def Eyny_DevilHunter(self):
        return self.Normal_Get(108)

    # 時空幻境 系列
    def Eyny_Tales(self):
        return self.Normal_Get(109)

    # 遊戲王系列
    def Eyny_Yugioh(self):
        return self.Normal_Get(110)

    # TV GAME 歷史回憶區
    def Eyny_TVGameStory(self):
        return self.Normal_Get(111)

    # 英雄聯盟League of Legends
    def Eyny_LOL(self):
        return self.Normal_Get(112)

    # 暴雪英霸
    def Eyny_HOS(self):
        return self.Normal_Get(113)

    # 暗黑破壞神3：奪魂之鐮
    def Eyny_D3(self):
        return self.Normal_Get(114)

    # 黑色沙漠 BLACK DESERT
    def Eyny_BLACKDESERT(self):
        return self.Normal_Get(115)

    # 救世主之樹 Tree of Savior
    def Eyny_TreeofSavior(self):
        return self.Normal_Get(116)

    # 鬥陣特攻 Overwatch
    def Eyny_Overwatch(self):
        return self.Normal_Get(117)

    # DMM綜合遊戲
    def Eyny_DMMGame(self):
        return self.Normal_Get(118)

    # 新楓之谷 Online
    def Eyny_MapleStoryOnline(self):
        return self.Normal_Get(119)

    # 流亡黯道 Path of Exile
    def Eyny_POE(self):
        return self.Normal_Get(120)

    # A.V.A 戰地之王 Revo
    def Eyny_AVA(self):
        return self.Normal_Get(121)

    # 天堂 Lineage系列
    def Eyny_Lineage(self):
        return self.Normal_Get(122)

    # 戰艦世界World of Warships
    def Eyny_WarOfWarships(self):
        return self.Normal_Get(123)

    # CS Online(絕對武力)
    def Eyny_CSO(self):
        return self.Normal_Get(124)

    # 艾爾之光
    def Eyny_Elsworld(self):
        return self.Normal_Get(125)

    # 爐石戰記：魔獸英雄傳
    def Eyny_HOH(self):
        return self.Normal_Get(126)

    # 仙境傳說RO系列
    def Eyny_RO(self):
        return self.Normal_Get(127)

    # 魔獸世界 WOW
    def Eyny_WOW(self):
        return self.Normal_Get(128)

    # 戰車世界 World of Tanks
    def Eyny_WorldofTanks(self):
        return self.Normal_Get(129)

    # 劍靈Blade & Soul
    def Eyny_BladeSoul(self):
        return self.Normal_Get(130)

    # 新瑪奇英雄傳
    def Eyny_Vindictus(self):
        return self.Normal_Get(131)

    # 全民打棒球 2
    def Eyny_BB2(self):
        return self.Normal_Get(132)

    # Pixiv角色創作專區
    def Eyny_Pixiv(self):
        return self.Normal_Get(133)

    # 艦隊提督鎮守府創作區
    def Eyny_Admiral(self):
        return self.Normal_Get(134)

    # 角色扮演類〈MMORPG〉
    def Eyny_MMORPG(self):
        return self.Normal_Get(135)

    # 手機/平板遊戲情報特搜
    def Eyny_Phone(self):
        return self.Normal_Get(136)

    # 網路遊戲情報討論區
    def Eyny_InternetGame(self):
        return self.Normal_Get(137)

    # 神魔之塔
    def Eyny_TowerofSaviors(self):
        return self.Normal_Get(138)

    # 天堂手遊系列
    def Eyny_LineageMobile(self):
        return self.Normal_Get(139)

    # 龍族拼圖 Puzzle & Dragons
    def Eyny_PuzzleDragons(self):
        return self.Normal_Get(140)

    # 超異域公主連結☆ReDive
    def Eyny_ReDive(self):
        return self.Normal_Get(141)

    # 關於我轉生變成史萊姆這檔事
    def Eyny_Reincarnated_As_A_Slime(self):
        return self.Normal_Get(142)

    # 在地下城尋求邂逅是否搞錯了什麼
    def Eyny_Girls_in_a_Dungeon(self):
        return self.Normal_Get(143)

    # 碧藍航線
    def Eyny_Azur_Lane(self):
        return self.Normal_Get(144)

    # 崩壞3rd
    def Eyny_HonkaiImpact3rd(self):
        return self.Normal_Get(145)

    # Garena 極速領域
    def Eyny_SpeedDrifters(self):
        return self.Normal_Get(146)

    # 闇影詩章(Shadowverse)
    def Eyny_Shadowverse(self):
        return self.Normal_Get(147)

    # 精靈寶可夢 GO
    def Eyny_PokemonGO(self):
        return self.Normal_Get(148)

    # 白貓Project
    def Eyny_WhiteCatProject(self):
        return self.Normal_Get(149)

    # 碧藍幻想
    def Eyny_GRANBLUEFANTASY(self):
        return self.Normal_Get(150)

    # 偶像大師灰姑娘女孩
    def Eyny_CINDERELLAGIRLS(self):
        return self.Normal_Get(151)

    # 陰陽師 Onmyoji
    def Eyny_Onmyoji(self):
        return self.Normal_Get(152)

    # 少女前線
    def Eyny_GirlFrontline(self):
        return self.Normal_Get(153)

    # Garena 傳說對決
    def Eyny_ArenaofValor(self):
        return self.Normal_Get(154)

    # 召喚圖板 Summons Board
    def Eyny_SummonsBoard(self):
        return self.Normal_Get(155)

    # 怪物彈珠
    def Eyny_MonsterStrike(self):
        return self.Normal_Get(156)

    # 鎖鏈戰記 CHAIN CHRONICLE
    def Eyny_CHAINCHRONICLE(self):
        return self.Normal_Get(157)

    # Line遊戲系列討論版
    def Eyny_LineGame(self):
        return self.Normal_Get(158)

    # 部落衝突Clash of Clans
    def Eyny_COC(self):
        return self.Normal_Get(159)

    # Fate/Grand Order
    def Eyny_FGO(self):
        return self.Normal_Get(160)

    # 日系手遊討論
    def Eyny_JapanMobileGame(self):
        return self.Normal_Get(161)

    # 國產手遊討論
    def Eyny_TaiwanMobileGame(self):
        return self.Normal_Get(162)

    # 其他手遊討論
    def Eyny_AnotherMobileGame(self):
        return self.Normal_Get(163)

    # 動畫(アニメ)改編討論
    def Eyny_AnimeAdaptation(self):
        return self.Normal_Get(164)

    # 私服討論區
    def Eyny_PrivateServer(self):
        return self.Normal_Get(165)

    # 線上遊戲歷史回憶區
    def Eyny_OnlineGameStory(self):
        return self.Normal_Get(166)

    # 塔羅及占卜
    def Eyny_Divination(self):
        return self.Normal_Get(167)

    # 星座心理區
    def Eyny_Constellation(self):
        return self.Normal_Get(168)

    # 愛情討論區
    def Eyny_Love(self):
        return self.Normal_Get(169)

    # 心情日記區
    def Eyny_Mooddiary(self):
        return self.Normal_Get(170)

    # 夢想與理想
    def Eyny_Dream(self):
        return self.Normal_Get(171)

    # 小小祈願池
    def Eyny_WishPool(self):
        return self.Normal_Get(172)

    # 寵物新資訊
    def Eyny_PetInformation(self):
        return self.Normal_Get(173)

    # 其他寵物討論
    def Eyny_PetChat(self):
        return self.Normal_Get(174)

    # 狗狗
    def Eyny_Dog(self):
        return self.Normal_Get(175)

    # 貓貓
    def Eyny_Cat(self):
        return self.Normal_Get(176)

    # 爬蟲兩棲
    def Eyny_Reptile(self):
        return self.Normal_Get(177)

    # 鼠類/兔類/龍貓類等
    def Eyny_Mouse(self):
        return self.Normal_Get(178)

    # 雀鳥
    def Eyny_Bird(self):
        return self.Normal_Get(179)

    # 水族養魚樂
    def Eyny_Fish(self):
        return self.Normal_Get(180)

    # 寵物貼圖
    def Eyny_PetSticker(self):
        return self.Normal_Get(181)

    # NBA籃球大聯盟
    def Eyny_NBA(self):
        return self.Normal_Get(182)

    # ♀㊣白痴１族☆♂
    def Eyny_Idiot(self):
        return self.Normal_Get(183)

    # ζˋ緣份網絡ˊζ
    def Eyny_Fate(self):
        return self.Normal_Get(184)

    # 動漫交流の佈告欄
    def Eyny_AnimeBulletinBoard(self):
        return self.Normal_Get(185)

    # 動漫新資訊
    def Eyny_AnimeInformation(self):
        return self.Normal_Get(186)

    # 綜合動漫討論區
    def Eyny_MixAnimeChat(self):
        return self.Normal_Get(187)

    # 新番動漫討論區
    def Eyny_NewAnimeChat(self):
        return self.Normal_Get(188)

    # 動漫輕小說
    def Eyny_AnimeNovelChat(self):
        return self.Normal_Get(189)

    # 銀魂
    def Eyny_GinTama(self):
        return self.Normal_Get(190)

    # 五等分的花嫁
    def Eyny_Quintuplets(self):
        return self.Normal_Get(191)

    # 刺客守則
    def Eyny_AssassinsPride(self):
        return self.Normal_Get(192)

    # 刀劍神域
    def Eyny_SAO(self):
        return self.Normal_Get(193)

    # 火影忍者
    def Eyny_NARUTO(self):
        return self.Normal_Get(194)

    # ONE PIECE 航海王(海賊王)
    def Eyny_ONEPIECE(self):
        return self.Normal_Get(195)

    # 食戟之靈
    def Eyny_Shokugeki_no_Soma(self):
        return self.Normal_Get(196)

    # 名偵探柯南
    def Eyny_DetectiveConan(self):
        return self.Normal_Get(197)

    # 國漫系列
    def Eyny_SelfComic(self):
        return self.Normal_Get(198)

    # 機械人討論區
    def Eyny_RobotChat(self):
        return self.Normal_Get(199)

    # Fate系列
    def Eyny_FateChat(self):
        return self.Normal_Get(200)

    # 轉生/穿越系列
    def Eyny_ReincarnatedChat(self):
        return self.Normal_Get(201)

    # UQ HOLDER!/悠久之風(赤松健作品系列)
    def Eyny_UQHOLDER(self):
        return self.Normal_Get(202)

    # 京都動畫(京阿尼)系列作品
    def Eyny_Kyoto(self):
        return self.Normal_Get(203)

    # 聲優園地
    def Eyny_Seiyuu(self):
        return self.Normal_Get(204)

    # 分級萌動學術院
    def Eyny_CuteChat(self):
        return self.Normal_Get(205)

    # 綜合討論&新版宣傳
    def Eyny_MixChat(self):
        return self.Normal_Get(206)

    # 科幻/魔法類討論
    def Eyny_TechorMagicChat(self):
        return self.Normal_Get(207)

    # 戀愛/校園類討論
    def Eyny_CampusLove(self):
        return self.Normal_Get(208)

    # 奇幻/冒險類討論
    def Eyny_Fantasy_Adventure(self):
        return self.Normal_Get(209)

    # 推理/靈異類討論
    def Eyny_Reasoning_Singularity(self):
        return self.Normal_Get(210)

    # 運動/競技類討論
    def Eyny_Sports_Athletics(self):
        return self.Normal_Get(211)

    # 動漫討論歷史回憶區
    def Eyny_AnimeStory(self):
        return self.Normal_Get(212)

    # 動漫精品交流
    def Eyny_AnimeBoutiques(self):
        return self.Normal_Get(213)

    # COSPLAY交流
    def Eyny_COSPLAY(self):
        return self.Normal_Get(214)

    # 初音家族Vocaloid
    def Eyny_Vocaloid(self):
        return self.Normal_Get(215)

    # ACG 動漫隨意貼圖
    def Eyny_ACGSticker(self):
        return self.Normal_Get(216)

    # HCG-H動漫隨意貼圖
    def Eyny_HCGSticker(self):
        return self.Normal_Get(217)

    # 漫畫分享版
    def Eyny_ComicShare(self):
        return self.Normal_Get(218)

    # 動漫音樂下載(上傳空間)
    def Eyny_AnimeMusicDownloader(self):
        return self.Normal_Get(219)

    # 動漫套圖下載區(上傳空間)
    def Eyny_AnimePictureDownload(self):
        return self.Normal_Get(220)

    # H 動畫下載區(上傳空間)
    def Eyny_HanimeDownload(self):
        return self.Normal_Get(221)

    # H 漫畫下載區(上傳空間)
    def Eyny_HComicDownload(self):
        return self.Normal_Get(222)

    # 中文H漫畫貼圖
    def Eyny_ZhHComicStickerDownload(self):
        return self.Normal_Get(223)

    # 日文H漫畫貼圖
    def Eyny_JapanHComicStickerDownload(self):
        return self.Normal_Get(224)

    # 英文H漫畫貼圖
    def Eyny_EngHComicStickerDownload(self):
        return self.Normal_Get(225)

    # 動漫下載求檔&問題區
    def Eyny_(self):
        return self.Normal_Get(226)

    # 搞笑貼圖區
    def Eyny_JokeSticker(self):
        return self.Normal_Get(227)

    # 網友自拍館
    def Eyny_Selfie(self):
        return self.Normal_Get(228)

    # 正妹美眉區
    def Eyny_Beauty(self):
        return self.Normal_Get(229)

    # 型男帥哥區
    def Eyny_Handsome(self):
        return self.Normal_Get(230)

    # DIY作品貼圖區
    def Eyny_DIY(self):
        return self.Normal_Get(231)

    # 網頁素材區
    def Eyny_PageMaterial(self):
        return self.Normal_Get(232)

    # 電腦桌布分享
    def Eyny_Wallpaper(self):
        return self.Normal_Get(233)

    # BL-GL討論
    def Eyny_BLChat(self):
        return self.Normal_Get(234)

    # BL-GL貼圖
    def Eyny_BLSticker(self):
        return self.Normal_Get(235)

    # BL-GL小說
    def Eyny_BLNovel(self):
        return self.Normal_Get(236)

    # BL-GL衍生
    def Eyny_BLDerivative(self):
        return self.Normal_Get(237)

    # BL-GL下載
    def Eyny_BLDownload(self):
        return self.Normal_Get(238)

    # BL-GL短片
    def Eyny_BLShortVideo(self):
        return self.Normal_Get(239)

    # 音樂新資訊
    def Eyny_NewMusic(self):
        return self.Normal_Get(240)

    # 其他音樂討論
    def Eyny_AnotherMusicChat(self):
        return self.Normal_Get(241)

    # 華語樂壇討論
    def Eyny_ZhmusicChat(self):
        return self.Normal_Get(242)

    # 日韓樂壇討論
    def Eyny_JapanKoreadMusciChat(self):
        return self.Normal_Get(243)

    # 外語樂壇討論
    def Eyny_EngMusicChat(self):
        return self.Normal_Get(244)

    # 音樂單曲下載
    def Eyny_MusicDownload(self):
        return self.Normal_Get(245)

    # 音樂專輯下載
    def Eyny_MusicAlbumDownload(self):
        return self.Normal_Get(246)

    # 無損音樂下載
    def Eyny_LosslessMusicDownload(self):
        return self.Normal_Get(247)

    # MTV和KTV下載
    def Eyny_KTVDownload(self):
        return self.Normal_Get(248)

    # 樂譜與樂器專區
    def Eyny_InstrumentChat(self):
        return self.Normal_Get(249)

    # 歌詞分享
    def Eyny_LyricsShare(self):
        return self.Normal_Get(250)

    # 會員唱作區
    def Eyny_MemberSongMake(self):
        return self.Normal_Get(251)

    # 音樂世界求檔&問題區
    def Eyny_MusicWorld(self):
        return self.Normal_Get(252)

    # 港台明星貼圖
    def Eyny_TaiwanHKCelebritySticker(self):
        return self.Normal_Get(253)

    # 日韓明星貼圖
    def Eyny_JapanKoreaCelebrity(self):
        return self.Normal_Get(254)

    # 外國明星貼圖
    def Eyny_EngCelebrity(self):
        return self.Normal_Get(255)

    # 電視節目討論
    def Eyny_TVShowChat(self):
        return self.Normal_Get(256)

    # 電台節目討論
    def Eyny_RadioChat(self):
        return self.Normal_Get(257)

    # 電影討論區
    def Eyny_MovieChat(self):
        return self.Normal_Get(258)

    # 電視連續劇討論區
    def Eyny_TVSeriesChat(self):
        return self.Normal_Get(259)

    # 美容討論
    def Eyny_BeautyChat(self):
        return self.Normal_Get(260)

    # 化妝討論
    def Eyny_MakeUpChat(self):
        return self.Normal_Get(261)

    # 減肥瘦身
    def Eyny_LoseWeightChat(self):
        return self.Normal_Get(262)

    # 女性用品
    def Eyny_FemaleHygienicAid(self):
        return self.Normal_Get(263)

    # 內衣
    def Eyny_Underwear(self):
        return self.Normal_Get(264)

    # 女人心事
    def Eyny_WomanMind(self):
        return self.Normal_Get(265)

    # 珠寶首飾
    def Eyny_Jewellery(self):
        return self.Normal_Get(266)

    # 女性健康分享
    def Eyny_WomanHealthy(self):
        return self.Normal_Get(267)

    # 指甲彩繪
    def Eyny_NailArt(self):
        return self.Normal_Get(268)

    # 髮型討論
    def Eyny_Hairstyle(self):
        return self.Normal_Get(269)

    # 鐘錶討論
    def Eyny_Timepiece(self):
        return self.Normal_Get(270)

    # 球鞋討論
    def Eyny_Sneakers(self):
        return self.Normal_Get(271)

    # 潮流服飾討論
    def Eyny_StylishClothes(self):
        return self.Normal_Get(272)

    # 牛仔服飾
    def Eyny_CowboyClothes(self):
        return self.Normal_Get(273)

    # 錢包手袋
    def Eyny_Wallet(self):
        return self.Normal_Get(274)

    # 二手衣飾交易
    def Eyny_Second_Hand_Clothes(self):
        return self.Normal_Get(275)

    # BT體育運動下載區
    def Eyny_BTSports(self):
        return self.Normal_Get(276)

    # BT軟件下載區
    def Eyny_BTSoftware(self):
        return self.Normal_Get(277)

    # BT遊戲下載區
    def Eyny_BTGame(self):
        return self.Normal_Get(278)

    # BT音樂下載區
    def Eyny_BTMusic(self):
        return self.Normal_Get(279)

    # BT H遊戲下載區
    def Eyny_BTHGame(self):
        return self.Normal_Get(280)

    # BT H動漫下載區
    def Eyny_HAnime(self):
        return self.Normal_Get(281)

    # BT日韓成人電影
    def Eyny_BTJapanKoreaAdultMovie(self):
        return self.Normal_Get(282)

    # BT歐美成人電影
    def Eyny_BTEngAdultMovie(self):
        return self.Normal_Get(283)

    # BT求檔&問題區
    def Eyny_BTFileProblem(self):
        return self.Normal_Get(284)

    # 軟件下載區(上傳空間)
    def Eyny_SoftwareDownload(self):
        return self.Normal_Get(285)

    # 遊戲下載區(上傳空間)
    def Eyny_GameDownload(self):
        return self.Normal_Get(286)

    # GalGame遊戲下載區(上傳空間)
    def Eyny_GalGameDownload(self):
        return self.Normal_Get(287)

    # H 遊戲下載區(上傳空間)
    def Eyny_HGameDownload(self):
        return self.Normal_Get(288)

    # 軟件下載區(會員制空間)
    def Eyny_MemberSoftware(self):
        return self.Normal_Get(289)

    # 遊戲下載區(會員制空間)
    def Eyny_MemberGameDownload(self):
        return self.Normal_Get(290)

    # 圖文遊戲下載區(會員制空間)
    def Eyny_MemberPictureGameDownload(self):
        return self.Normal_Get(291)

    # H 遊戲下載區(會員制空間)
    def Eyny_MemberHGameDownload(self):
        return self.Normal_Get(292)

    # 電子書下載區
    def Eyny_EBookDownload(self):
        return self.Normal_Get(293)

    # 小說下載區
    def Eyny_NovelDownload(self):
        return self.Normal_Get(294)

    # FLASH下載區
    def Eyny_FlashDownload(self):
        return self.Normal_Get(295)

    # 下載分享求檔&問題區
    def Eyny_DownloadShareProblem(self):
        return self.Normal_Get(296)

    # 其他短片
    def Eyny_AnotherShortVideo(self):
        return self.Normal_Get(297)

    # 搞笑短片
    def Eyny_FunnyShortVideo(self):
        return self.Normal_Get(298)

    # 動漫短片
    def Eyny_AnimeShort(self):
        return self.Normal_Get(299)

    # 寵物短片
    def Eyny_PetShortVideo(self):
        return self.Normal_Get(300)

    # 音樂短片
    def Eyny_MusicShort(self):
        return self.Normal_Get(301)

    # 寶貝BB短片
    def Eyny_BBShortVideo(self):
        return self.Normal_Get(302)

    # 網友自拍短片
    def Eyny_SelfieShortVideo(self):
        return self.Normal_Get(303)

    # 歌星藝人短片
    def Eyny_SongStarShortVideo(self):
        return self.Normal_Get(304)

    # 感人熱淚短片
    def Eyny_MovingShortVideo(self):
        return self.Normal_Get(305)

    # 汽車機車短片
    def Eyny_CarMotorcycleShortVideo(self):
        return self.Normal_Get(306)

    # 體育運動短片
    def Eyny_SportsShortVideo(self):
        return self.Normal_Get(307)

    # 電腦新資訊
    def Eyny_ComputerInformation(self):
        return self.Normal_Get(308)

    # 電腦軟體討論
    def Eyny_SoftwareChat(self):
        return self.Normal_Get(309)

    # 電腦軟體資訊分享
    def Eyny_SoftwareInfromationShare(self):
        return self.Normal_Get(310)

    # 電腦硬體討論
    def Eyny_ComputerHardwareChat(self):
        return self.Normal_Get(311)

    # 電腦硬體資訊分享
    def Eyny_ComputerHardware(self):
        return self.Normal_Get(312)

    # 電腦萌化版
    def Eyny_ComputerCute(self):
        return self.Normal_Get(313)

    # 電腦系統 OS 討論
    def Eyny_ComputerSystemChat(self):
        return self.Normal_Get(314)

    # 電腦程式設計
    def Eyny_Programming(self):
        return self.Normal_Get(315)

    # 電腦設計技術交流
    def Eyny_ComputerDesign(self):
        return self.Normal_Get(316)

    # 圖像設計及交流
    def Eyny_GraphicsChat(self):
        return self.Normal_Get(317)

    # 各類下載工具教學
    def Eyny_ToolDownload(self):
        return self.Normal_Get(318)

    # 寬頻上網討論
    def Eyny_InternetChat(self):
        return self.Normal_Get(319)

    # 平板電腦/iPad
    def Eyny_iPad(self):
        return self.Normal_Get(320)

    # 數碼相機 DC
    def Eyny_DC(self):
        return self.Normal_Get(321)

    # 數碼攝錄機 DV
    def Eyny_DV(self):
        return self.Normal_Get(322)

    # 家庭影音 AV
    def Eyny_FamilyAV(self):
        return self.Normal_Get(323)

    # MP3/耳機
    def Eyny_NP3(self):
        return self.Normal_Get(324)

    # iPod
    def Eyny_iPod(self):
        return self.Normal_Get(325)

    # 手提電腦 NoteBook
    def Eyny_NoteBook(self):
        return self.Normal_Get(326)

    # PPC 交流
    def Eyny_PPC(self):
        return self.Normal_Get(327)

    # 其他數碼產品
    def Eyny_AnotherDigitalProduct(self):
        return self.Normal_Get(328)

    # 手機討論
    def Eyny_PhoneChat(self):
        return self.Normal_Get(329)

    # 手機選購 (2G + 3G)
    def Eyny_BuyPhoneChat(self):
        return self.Normal_Get(330)

    # 手機鈴聲(非MP3)
    def Eyny_PhoneRingNotMP3(self):
        return self.Normal_Get(331)

    # 手機鈴聲(MP3)
    def Eyny_PhoneRingMP3(self):
        return self.Normal_Get(332)

    # 手機主題和桌布
    def Eyny_PhoneWallpaper(self):
        return self.Normal_Get(333)

    # 手機遊戲
    def Eyny_MobileGame(self):
        return self.Normal_Get(334)

    # 手機影片分享
    def Eyny_MobileVideo(self):
        return self.Normal_Get(335)

    # 手機軟件應用程式
    def Eyny_MobileApp(self):
        return self.Normal_Get(336)

    # 二手交易
    def Eyny_Second_Hand_Transaction(self):
        return self.Normal_Get(337)

    # 拍賣廣場
    def Eyny_AuctionPlaza(self):
        return self.Normal_Get(338)

    # 重要公告區
    def Eyny_ImportantNotice(self):
        return self.Normal_Get(339)

    # 贊助問題區
    def Eyny_Sponsor(self):
        return self.Normal_Get(340)

    # 版主招募區
    def Eyny_Host(self):
        return self.Normal_Get(341)

    # 新手教學區
    def Eyny_Newbie(self):
        return self.Normal_Get(342)

    # 活動交流區
    def Eyny_Activity(self):
        return self.Normal_Get(343)

    # 伊莉影片區
    def Eyny_EynyVideo(self):
        return self.Normal_Get(344)

    # 伊莉部落格
    def Eyny_EynyBlog(self):
        return self.Normal_Get(345)

    # 伊莉百科區
    def Eyny_EynyEncyclopedia(self):
        return self.Normal_Get(346)

    # 投訴及意見
    def Eyny_Complaints(self):
        return self.Normal_Get(347)

    # 長篇小說交流園地
    def Eyny_LongNovel(self):
        return self.Normal_Get(348)

    # 出版類言情小說
    def Eyny_RomanceNovel(self):
        return self.Normal_Get(349)

    # 玄幻魔法小說
    def Eyny_MagicNovel(self):
        return self.Normal_Get(350)

    # 武俠修真小說
    def Eyny_MartialNovel(self):
        return self.Normal_Get(351)

    # 科幻偵探小說
    def Eyny_TechNovel(self):
        return self.Normal_Get(352)

    # 原創言情小說
    def Eyny_OriginRomanceNovel(self):
        return self.Normal_Get(353)

    # 都市小說
    def Eyny_CityNovel(self):
        return self.Normal_Get(354)

    # 輕小說
    def Eyny_LightNovel(self):
        return self.Normal_Get(355)

    # 其他小說
    def Eyny_AnotherNovel(self):
        return self.Normal_Get(356)

    # 其他運動討論
    def Eyny_AnotherSportsChat(self):
        return self.Normal_Get(357)

    # 足球討論
    def Eyny_FootBallChat(self):
        return self.Normal_Get(358)

    # 單車討論
    def Eyny_BicycleChat(self):
        return self.Normal_Get(359)

    # 籃球討論
    def Eyny_BasketBallChat(self):
        return self.Normal_Get(360)

    # 田徑討論
    def Eyny_RaceChat(self):
        return self.Normal_Get(361)

    # 棒球討論
    def Eyny_BaseBallChat(self):
        return self.Normal_Get(362)

    # 羽毛球討論
    def Eyny_BadmintonChat(self):
        return self.Normal_Get(363)

    # 乒乓球討論
    def Eyny_PingPongChat(self):
        return self.Normal_Get(364)

    # 撞球(桌球)討論
    def Eyny_BilliardBallChat(self):
        return self.Normal_Get(365)

    # 健身運動討論
    def Eyny_FitnessChat(self):
        return self.Normal_Get(366)

    # 武術討論
    def Eyny_MartialChat(self):
        return self.Normal_Get(367)

    # 爬山及遠足討論
    def Eyny_ClimbingChat(self):
        return self.Normal_Get(368)

    # 瑜伽討論
    def Eyny_YogaChat(self):
        return self.Normal_Get(369)

    # 排球討論
    def Eyny_VolleyBallChat(self):
        return self.Normal_Get(370)

    # 網球/壁球討論
    def Eyny_TennisChat(self):
        return self.Normal_Get(371)

    # 高爾夫球討論
    def Eyny_GolfChat(self):
        return self.Normal_Get(372)

    # 職業摔角討論
    def Eyny_WrestlingChat(self):
        return self.Normal_Get(373)

    # 潛水討論
    def Eyny_DivingChat(self):
        return self.Normal_Get(374)

    # 時事討論
    def Eyny_CurrentEventsChat(self):
        return self.Normal_Get(375)

    # 明星新聞討論
    def Eyny_StarNews(self):
        return self.Normal_Get(376)

    # 有趣新聞
    def Eyny_InterestingNews(self):
        return self.Normal_Get(377)

    # 企業家管理交流
    def Eyny_EntrepreneurChat(self):
        return self.Normal_Get(378)

        # 金融財經、投資交流

    def Eyny_InvestmentChat(self):
        return self.Normal_Get(379)

    # 房地產討論
    def Eyny_EstateChat(self):
        return self.Normal_Get(380)

    # 股票討論
    def Eyny_StockChat(self):
        return self.Normal_Get(381)

    # 基金保險
    def Eyny_FundChat(self):
        return self.Normal_Get(382)

    # 外幣投資
    def Eyny_Exchange(self):
        return self.Normal_Get(383)

    # 租屋資訊
    def Eyny_Rent_a_house_Information(self):
        return self.Normal_Get(384)

    # 環境保護問題探討
    def Eyny_EnvironmentalProtection(self):
        return self.Normal_Get(385)

    # 食物衛生及用品安全
    def Eyny_FoodSanitation(self):
        return self.Normal_Get(386)

    # 軍事討論
    def Eyny_MilitaryChat(self):
        return self.Normal_Get(387)

    # 上班樂與怒
    def Eyny_WorkChat(self):
        return self.Normal_Get(388)

    # 工作薪酬討論
    def Eyny_SalaryChat(self):
        return self.Normal_Get(389)

    # 創業討論區
    def Eyny_EntrepreneurshipChat(self):
        return self.Normal_Get(390)

    # 網路賺錢
    def Eyny_MakeMoneyOnline(self):
        return self.Normal_Get(391)

    # 各行各業
    def Eyny_Industry(self):
        return self.Normal_Get(392)

    # 求職者交流
    def Eyny_JobSeeker(self):
        return self.Normal_Get(393)

    # 兼職工讀交流
    def Eyny_PartTime(self):
        return self.Normal_Get(394)

    # 人力銀行(提供職位資訊)
    def Eyny_JobBank(self):
        return self.Normal_Get(395)

    # 兩性討論
    def Eyny_GenderChat(self):
        return self.Normal_Get(396)

    # 夜遊討論
    def Eyny_NightTourChat(self):
        return self.Normal_Get(397)

    # 成人交友
    def Eyny_AudltFriendChat(self):
        return self.Normal_Get(398)

    # 成人貼圖
    def Eyny_AdultSticker(self):
        return self.Normal_Get(399)

    # 成人電影(上傳空間)
    def Eyny_AdultMovie(self):
        return self.Normal_Get(400)

    # 成人小說
    def Eyny_AdultNovel(self):
        return self.Normal_Get(401)

    # 足球投注
    def Eyny_FootballBetting(self):
        return self.Normal_Get(402)

    # 虛擬足球投注站
    def Eyny_VirtualFootballBetting(self):
        return self.Normal_Get(403)

    # 香港賽馬
    def Eyny_HKHorserace(self):
        return self.Normal_Get(404)

    # 賭場討論
    def Eyny_CasinoChat(self):
        return self.Normal_Get(405)

    # 麻雀耍樂
    def Eyny_Sparrow(self):
        return self.Normal_Get(406)

    # 撲克交流
    def Eyny_Poker(self):
        return self.Normal_Get(407)

    # ----------------------------------------------------------------------------------------------
    # 取得隨機版連結
    def Get_Random_Board(self):
        return random.choice(self.Taget_Url)

    # 隨機版的貼文
    def Get_Random_Post(self):
        return self.Normal_Get_URL(self.Get_Random_Board())
