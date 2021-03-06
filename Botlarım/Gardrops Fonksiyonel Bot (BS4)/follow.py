from os import link
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import kullanıcı as kb
from selenium.webdriver.common.keys import Keys
import smtplib,requests,time,sys

hesap_sayac = 0
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

    def login(self): #Gardropsu açar.
        print("Gardrops başarılı şekilde açılmıştır.")
        time.sleep(2)
        self.browser = webdriver.Chrome("") #chromedriver yolunuzu giriniz
        self.browser.get(self.link)
        WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
        time.sleep(3)
        Browser.account(self)

    def account(self): #Hesabınıza giriş yapar
        nick = self.browser.find_element_by_id("e-mail")
        pw = self.browser.find_element_by_id("password")
        nick.send_keys(kb.nickname)
        pw.send_keys(kb.password)
        print("Hesap bilgileri girilmiştir. 15 saniye içerisinde Ben Robot Değilim işlemini yapmanız gerekmektedir.")
        time.sleep(15)
        self.browser.find_element_by_xpath("/html/body/div[2]/div/div[5]/form/div[3]/input").click()
        time.sleep(10)
        Browser.Lists(self)

    def Lists(self): #Listeleri günceller
        global follow_tur
        print("Liste elemanları güncelleniyor...")
        yazi1 = open("Lists/Gardrops_follow_tur.txt", "w") 
        dosya = open("Lists/Gardrops_total.txt", "r").readlines()
        dosya1 = open("Lists/Gardrops_follow_atilan.txt", "r").readlines()
        follow_tur = []
        for i in dosya1:
            follow_tur.append(i)
        for j in dosya:
            if j not in follow_tur:
                yazi1.write(j)
        yazi1.close()
        time.sleep(1)
        Browser.Follower(self)

    def Follower(self): #Listedeki kullanıcılara takip atar ve takip atılanları listeye ekler.
        global ts_total,sayac_total
        print("Takip atma işlemi başlanıyor.")
        dosya = open("Lists/Gardrops_follow_atilan.txt", "a") 
        dosya2 = open("Lists/Gardrops_follow_tur.txt", "r").readlines()
        try:
            for k in dosya2:
                try:
                    self.browser.get("https://www.gardrops.com/{}".format(k))
                    WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
                    time.sleep(1)
                    follow = self.browser.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[4]/div/div")
                    if follow.text != "Takibi Bırak":
                        follow.click()
                        ts_total += 1
                        sayac_total += 1
                    else:
                        sayac_total += 1
                    dosya.write(k)            
                except:
                    try:
                        hata = self.browser.find_element_by_xpath("/html/body/div/h1")
                        if hata.text == "An Error Was Encountered":
                            dosya.write(k)
                    except:
                        ana = self.browser.find_element_by_xpath("/html/body/header/div[2]/div/div/div[7]/div[1]/a/div")
                        if ana.text == "kampanya":
                            dosya.write(k)
            print("Takip atma işlemi bitmiştir.")        
            dosya.close()
            time.sleep(2)
            Browser.Toplam()
        except:
            print("Tüm kullanıcılara takip atılmadan bottan çıkış yapılmıştır.")
            dosya.close()
            time.sleep(1)
            Browser.Toplam()

    def Toplam(): #Python chat bildirimi
        global say
        say = 1
        followfiletotal = open("Lists/Gardrops_total.txt" , "r").readlines() #Bu kullanıcılara takip atar
        for i in followfiletotal:
            say += 1
        print("""Merhaba Oğuz Taşdemir, ben Amoyt Bot. Gardrops botunuz başarıyla tamamlanmıştır
        {} adet kullanıcıya takip atılmıştır.
        Bu tur  {} adet kullanicinin profili kontrol edilmistir.
        Amoyt Bot sayesinde şuana kadar toplam {} adet kullanıcı bulunmuştur.""".format(ts_total,sayac_total,say))
        Browser.GetMail()

    def GetMail(): #Gmail bildirimi
        print("Mail gönderme işlemi başarıyla tamamlanmıştır.")
        content = """Merhaba Oguz Tasdemir, ben Amoyt Bot. Gardrops botunuz basariyla tamamlanmistir
        {} adet kullaniciya takip atilmistir.
        Bu tur  {} adet kullanicinin profili kontrol edilmistir.
        Amoyt Bot sayesinde suana kadar toplam {} adet kullanici bulunmustur.""".format(ts_total,sayac_total,say)
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
        apikey = '' #apikeyinizi buraya girin
        message = "Amoyt Bot"

        description = """Merhaba Oğuz Taşdemir, ben Amoyt Bot. Gardrops botunuz başarıyla tamamlanmıştır
        {} adet kullanıcıya takip atılmıştır.
        Bu tur  {} adet kullanıcının profili kontrol edilmiştir.
        Amoyt Bot sayesinde şuana kadar toplam {} adet kullanıcı bulunmuştur.""".format(ts_total,sayac_total,say)
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
            print("Çıkış yapılmıştır.")
            sys.exit()
            time.sleep(10000) #ekstrem bir durumdan kaynaklı olarak bot sonlanmazsa botu manuel kapatmamız için gereken süreyi sağlayacaktır