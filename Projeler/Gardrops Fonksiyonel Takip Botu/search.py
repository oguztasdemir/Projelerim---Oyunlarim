from os import link
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import kullanıcı as kb
from selenium.webdriver.common.keys import Keys
import smtplib,requests,time

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
        self.browser = webdriver.Chrome("Chrome driver bilginizi buraya girin")
        self.browser.get(self.link)
        WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
        time.sleep(3)
        Browser.account(self)

    def account(self): #Hesaba giriş yapar
        nick = self.browser.find_element_by_id("e-mail")
        pw = self.browser.find_element_by_id("password")
        nick.send_keys(kb.nickname)
        pw.send_keys(kb.password)
        print("Hesap bilgileri girilmiştir. 15 saniye içerisinde Ben Robot Değilim işlemini yapmanız gerekmektedir.")
        time.sleep(15)
        self.browser.find_element_by_xpath("/html/body/div[2]/div/div[5]/form/div[3]/input").click()
        time.sleep(10)
        Browser.Kullanicilar(self)


    def Kullanicilar(self): #User_list kısmındaki kullanıcının profiline gider
        self.browser.get("https://www.gardrops.com/{}/followers".format(kb.user_list[kb.hesap_sayac]))
        WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
        time.sleep(1)
        print("{} adlı kullanıcının takipçileri kontrol ediliyor.".format(kb.user_list[kb.hesap_sayac]))
        kb.hesap_sayac += 1
        Browser.Scroll(self)


    def Scroll(self): #Sayfayı aşağı indirir
        döngü = 0   
        while döngü < kb.scroll:  
            döngü += 1 
            page = self.browser.find_element_by_tag_name("html")
            page.send_keys(Keys.END)
            time.sleep(0.3)
        Browser.GetFollowers(self)
    
    def GetFollowers(self): #Listeye ekleme yapar
        global a
        try:   
            print("Kullanıcı ismi çekme kısmına başarılı şekilde ulaşılmıştır.")    
            while a < kb.kisi:
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
        if kb.hesap_sayac <= (kb.hesap_sayac + kb.hesap) - 1:
            print("Diğer kullanıcının takipçilerine bakılıyor.")
            a = 1
            Browser.Kullanicilar(self)
        elif kb.hesap_sayac > (kb.hesap_sayac + kb.hesap) - 1:
            #print("{} tane kullanıcıya takip atılmıştır.".format(ts))
            print("Takip edilenler listeye eklenilmiştir.")
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
        Amoyt Bot sayesinde şuana kadar toplam {} adet kullanıcı bulunmuştur.""".format(a_total,takip_sayac_total,say))
        Browser.GetMail()

    def GetMail(): #Gmail bildirimi
        print("Mail gönderme işlemi başarıyla tamamlanmıştır.")
        content = """Merhaba Oguz Tasdemir, ben Amoyt Bot. Gardrops botunuz basariyla tamamlanmistir
        {} adet kullanici bulunmustur.
        {} adet yeni kullanici bulunmustur.
        Amoyt Bot sayesinde suana kadar toplam {} adet kullanici bulunmustur.""".format(a_total,takip_sayac_total,say)
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login(" "," ") #mail atan hesabın e-maili - mail atan hesabın şifresi
        mail.sendmail(" "," ",content) #mail atan hesabın e-maili - mail alacak olan hesabın e-maili
        time.sleep(1)
        Browser.GetMobile()


    def GetMobile(): #telefon bildirimi
        print("Telefona bildirim gönderme işlemi başarıyla tamamlanmıştır.")
        endpoint = 'https://api.mynotifier.app'
        apikey = ' ' #apikeyiniz
        message = "Amoyt Bot" #bildirim başlığı

        description = """Merhaba Oğuz Taşdemir, ben Amoyt Bot. Gardrops botunuz başarıyla tamamlanmıştır
        {} adet kullanıcı bulunmuştur.
        {} adet yeni kullanıcı bulunmustur.
        Amoyt Bot sayesinde şuana kadar toplam {} adet kullanıcı bulunmuştur.""".format(a_total,takip_sayac_total,say) #metin içeriği
        requests.post(endpoint,{
            "apiKey": apikey,
            "message": message,
            "description": description,
            "type": "success",
        })