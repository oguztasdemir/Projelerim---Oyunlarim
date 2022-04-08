from os import link
import time
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import kullanıcı as kb
from selenium.webdriver.common.keys import Keys

a = 1
list = []

class Browser:
   
    def __init__(self,link):
        self.link = link
        Browser.login(self)

    def login(self): #İnstagramı açar.
        print("Gardrops başarılı şekilde açılmıştır.")
        time.sleep(2)
        self.browser = webdriver.Chrome("") #chromedriver yolunuzu giriniz
        self.browser.get(self.link)
        WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
        time.sleep(3)
        Browser.account(self)

    def account(self):
        nick = self.browser.find_element_by_id("e-mail")
        pw = self.browser.find_element_by_id("password")
        nick.send_keys(kb.nickname)
        pw.send_keys(kb.password)
        print("Hesap bilgileri girilmiştir. 15 saniye içerisinde Ben Robot Değilim işlemini yapmanız gerekmektedir.")
        time.sleep(15)
        self.browser.find_element_by_xpath("/html/body/div[2]/div/div[5]/form/div[3]/input").click()
        time.sleep(10)
        self.browser.get("https://www.gardrops.com/{}/followers".format(kb.user))
        WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
        time.sleep(1)
        Browser.Scroll(self)


    def Scroll(self):
        döngü = 0   
        while döngü < 110:  
            döngü += 1 
            page = self.browser.find_element_by_tag_name("html")
            page.send_keys(Keys.END)
            time.sleep(0.1)
        Browser.GetFollowers(self,a)
    
    def GetFollowers(self,a):
        try:   
            print("Kullanıcı ismi çekme kısmına başarılı şekilde ulaşılmıştır.")    
            while a < 3000:
                follow = self.browser.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/div[1]/div[{}]/div/div/div/div[2]".format(a))
                follow = follow.text.replace("+", "")
                if follow != "Takibi Bırak":
                    fw = self.browser.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/div[1]/div[{}]/a/div[2]/div[1]".format(a))                    
                    list.append(fw.text)
                    time.sleep(0.2)
                a += 1
            print("{} adet takip etmediğiniz kullanıcı bulunmuştur.".format(a))
            Browser.GetList(self,list)
        except:
            print("Belirttiğiniz miktarda kullanıcı bulamadınız. Bulunan kullanıcı sayısı: ",a)
            Browser.GetList(self,list)


    def GetList(self,list): #O tur takip atılacak kullanıcıların adını seçer
        dosya = open("Lists/Gardrops_tur.txt","w")
        for i in list:
            dosya.write("{}\n".format(i))
        dosya.close()
        time.sleep(2)
        Browser.CheckList(self)        


    def CheckList(self): #Listeyi kontrol eder ve elemanları takip edilecekler listesine yazar
        print("Liste elemanları düşürülüyor")
        global nick
        takip_sayac = 0
        file = open("Lists/Gardrops_tur.txt" , "r").readlines() #bu tur seçilen kullanıcılar
        file2 = open("Lists/Gardrops_total.txt" , "r").readlines() #tüm kullanıcılar, bunu yapma nedenim bu tur seçilecek kullanıcılar ve total kullanıcılar arasında aynı kişiler varsa onları elemektir
        filecontrol = open("Lists/Gardrops_takip.txt" , "w") #takip atılacaklar kısmı
        count = 0
        nick = []
        for line in file:
            if line not in file2:
                filecontrol.write(line)
                nick.append(line)
                takip_sayac += 1
            else:
                pass
        print("{} adet yeni kullanıcı bulundu. Bu kişilerin profiline gidiliyor.".format(takip_sayac))
        filecontrol.close()
        time.sleep(2)
        Browser.TakipAt(self)

    def TakipAt(self): #Takip Atılacaklar Listesindeki kullanıcılara takip atarlar
     try:
        print("Takip Atma kısmına gelinmiştir.")
        sayac = 1
        followfile = open("Lists/Gardrops_takip.txt" , "r").readlines() #Bu kullanıcılara takip atar
        file3 = open("Lists/Gardrops_total.txt","a") #Takip atılan kullanıcıları toplam listesine ekler
        for i in followfile:
            WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
            time.sleep(1)
            self.browser.get("https://www.gardrops.com/{}".format(i))
            try:
                deneme = self.browser.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[4]/div/div/div")
                deneme = deneme.text.replace("+", "")
                if deneme != "Takibi Bırak":
                    self.browser.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[4]/div").click()
                else:
                    pass
                sayac += 1
                file3.write("{}".format(i))
                time.sleep(1)
            except:
                sayac += 1  
                file3.write("{}".format(i)) 
                time.sleep(1)
        time.sleep(2)
        file3.close()
     except:
        print("Takip edilenler listeye eklenilmiştir.")
