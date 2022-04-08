from os import link
from bs4 import BeautifulSoup
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import kullanıcı as kb
from selenium.webdriver.common.keys import Keys
import smtplib,requests,time,sys

a = 1
list = []
a_total = 0
takip_sayac_total = 0
ts_total = 0
sayac_total = 0
class Browser:
   
    def __init__(self,link):
        self.link = link
        Browser.login(self)

    def login(self): #Gardropsu açar
        print("Gardrops başarılı şekilde açılmıştır.")
        time.sleep(2)
        self.browser = webdriver.Chrome("") #chromedriver yolunuzu giriniz
        self.browser.get(self.link)
        WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
        time.sleep(3)
        Browser.Profiller(self)

    def Profiller(self):
        global user_list
        dosya = open("Lists/Gardrops_follow_atilan.txt", "r").readlines()
        dosya2 = open("Lists/Gardrops_user_list.txt", "r").readlines()
        user_list = []
        follow = []
        sayac = 0
        for i in  dosya2:
            i = i.replace("\n","")
            follow.append(i)

        for j in dosya:
            j = j.replace("\n","")
            if j not in follow:
                user_list.append(j)
                sayac += 1
                if sayac == 100:
                    break
        print("Profillerine bakılacak kullanıcılar listesi: {}".format(user_list))        
        Browser.Kullanicilar(self)


    def Kullanicilar(self): #User_list kısmındaki kullanıcının profiline gider
        dosya = open("Lists/Gardrops_user_list.txt","a")
        self.browser.get("https://www.gardrops.com/{}/followers".format(user_list[kb.hesap_sayac]))
        WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
        time.sleep(1)
        print("{} adlı kullanıcının takipçileri kontrol ediliyor.".format(user_list[kb.hesap_sayac]))
        dosya.write("{}\n".format(user_list[kb.hesap_sayac]))
        dosya.close()
        time.sleep(1)
        kb.hesap_sayac += 1
        Browser.Scroll(self)


    def Scroll(self): #Sayfayı aşağı indirir
        time.sleep(1)
        WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
        time.sleep(1)
        döngü = 0   
        while döngü < kb.scroll:  
            döngü += 1 
            page = self.browser.find_element_by_tag_name("html")
            page.send_keys(Keys.END)
            self.browser.execute_script("window.scrollTo(0, window.scrollY - 1000)")
            time.sleep(0.4)
        Browser.GetFollowers(self)
    
    def GetFollowers(self): #Listeye ekleme yapar
        global a
        try:   
            sayfa = self.browser.page_source
            soup = BeautifulSoup(sayfa, "html.parser")
            takipciler = soup.find_all("div",attrs={"class":"details"})
            for takip in takipciler:
                kisi = takip.find("div", attrs={"class":"username"}).text
                list.append(kisi)
                a += 1
            print("Toplam {} adet kullanıcı bulunmuştur.".format(a))
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
        global nick,takip_sayac
        takip_sayac = 0
        file = open("Lists/Gardrops_tur.txt" , "r").readlines() #bu tur seçilen kullanıcılar
        file2 = open("Lists/Gardrops_total.txt" , "r").readlines() #tüm kullanıcılar, bunu yapma nedenim bu tur seçilecek kullanıcılar ve total kullanıcılar arasında aynı kişiler varsa onları elemektir
        filecontrol = open("Lists/Gardrops_gt.txt" , "a") #takip atılacaklar kısmı
        nick = []
        for line in file:
            if line not in file2:
                filecontrol.write(line)
                nick.append(line)
                takip_sayac += 1
            else:
                pass
        print("{} adet yeni kullanıcı bulundu. Listeye ekleme başlatılıyor...".format(takip_sayac))
        filecontrol.close()
        time.sleep(2)
        Browser.Update_list(self,nick)
    
    def Update_list(self,nick):
        print("Gardrops_Total listesi güncelleniyor...")
        file = open("Lists/Gardrops_total.txt", "a")
        for i in nick:
            file.write(i)
        file.close()
        Browser.Kullanici_atla(self)

    def Kullanici_atla(self): #User_list kısmındaki diğer kullanıcıya geçiş yapmanızı sağlar
        global a_total,takip_sayac_total,ts_total,sayac_total,a
        takip_sayac_total += takip_sayac
        a_total += a
        time.sleep(1)
        try:
            self.browser.find_element_by_xpath("/html/body/header/div[2]/div/div/div[7]/div[1]")
            if kb.hesap_sayac <= (kb.hesap_sayac + kb.hesap) - 1:
                print("Diğer kullanıcının takipçilerine bakılıyor.")
                a = 1
                time.sleep(10)
                Browser.Kullanicilar(self)
            elif kb.hesap_sayac > (kb.hesap_sayac + kb.hesap) - 1:
                print("Takip edilenler listeye eklenilmiştir.")
                Browser.Toplam()      
        except:
            print("Bota erişim kesilmiştir.") 
            Browser.Toplam() 

    def Toplam(): #Python chat bildirimi
        global say
        say = 1
        followfiletotal = open("Lists/Gardrops_total.txt" , "r").readlines() #Bu kullanıcılara takip atar
        for i in followfiletotal:
            say += 1
        print("""Merhaba Oğuz Taşdemir, ben Amoyt Bot. Gardrops botunuz başarıyla tamamlanmıştır
        {} adet kullanıcı bulunmuştur.
        {} adet yeni kullanıcı bulunmustur.
        Amoyt Bot sayesinde şuana kadar toplam {} adet yeni kullanıcı bulunmuştur.""".format(a_total,takip_sayac_total,say))
        Browser.GetMail()

    def GetMail(): #Gmail bildirimi
        print("Mail gönderme işlemi başarıyla tamamlanmıştır.")
        content = """Merhaba Oguz Tasdemir, ben Amoyt Bot. Gardrops botunuz basariyla tamamlanmistir
        {} adet kullanici bulunmustur.
        {} adet yeni kullanici bulunmustur.
        Amoyt Bot sayesinde suana kadar toplam {} adet yeni kullanici bulunmustur.""".format(a_total,takip_sayac_total,say)
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("GÖNDEREN KİŞİNİN MAİL ADRESİ","GÖNDEREN KİŞİNİN MAİL ADRESİNİN ŞİFRESİ")
        mail.sendmail("GÖNDEREN KİŞİNİN MAİL ADRESİ","GÖNDERİLECEK KİŞİNİN MAİL ADRESİ",content)
        time.sleep(1)
        #Browser.GetMobile()
        Browser.End()

    def GetMobile(): #telefon bildirimi
        print("Telefona bildirim gönderme işlemi başarıyla tamamlanmıştır.")
        endpoint = 'https://api.mynotifier.app'
        apikey = '' #api keyinizi buraya yazın
        message = "Amoyt Bot"

        description = """Merhaba Oğuz Taşdemir, ben Amoyt Bot. Gardrops botunuz başarıyla tamamlanmıştır
        {} adet kullanıcı bulunmuştur.
        {} adet yeni kullanıcı bulunmustur.
        Amoyt Bot sayesinde şuana kadar toplam {} adet yeni kullanıcı bulunmuştur.""".format(a_total,takip_sayac_total,say)
        requests.post(endpoint,{
            "apiKey": apikey,
            "message": message,
            "description": description,
            "type": "success",
        })
        Browser.End()

    def End():
        try:
            print("Bot tamamlanmıştır. Sistemden çıkış yapılıyor...")
        except:
            print("Bot tamamlanmıştır. Sistemden çıkış yapılıyor...")
        finally:
            sys.exit()
            time.sleep(10000) #ekstra bir durumdan dolayı botumuz sonlanmazsa diye bu time kısmını ekleyerek botumuzu manuel kapatabilmemiz için gereken süreyi sağlar