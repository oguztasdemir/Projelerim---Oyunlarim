from pickle import FALSE
import time, random,sys,requests,smtplib
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import kullanıcı as kb
from webbrowser import Chrome

a = 1
takip_sayisi = 0
nick = []
takip_etme = 0
follow_list = []

class Browser:
    sayac2 = 1
    def __init__(self,link):
        self.link = link
        Browser.goInstagram(self)


    def goInstagram(self): #İnstagramı açar.
            print("Google 2 saniye içerisinde açılacaktır.")
            time.sleep(2)
            self.browser = webdriver.Chrome("") #chromedriver yolunuzu giriniz
            self.browser.get(self.link)
            time.sleep(1)
            Browser.login(self)


    def login(self): #Hesabımıza girmemizi sağlar. Bu kısımda kullanıcı.py adlı kısımdaki hesaba giriş yapacaktır.
            dosya = open("Lists/İnstagram_{}_gt.txt".format(kb.nickname), "a")
            time.sleep(2)
            dosya.close()
            print("İnstagram başarılı şekilde açıldı.")
            WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
            time.sleep(1)
            username = self.browser.find_element_by_name("username")
            password = self.browser.find_element_by_name("password")
            username.send_keys(kb.nickname)
            password.send_keys(kb.password)
            time.sleep(1)
            login1 = self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div")
            login1.click()
            WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
            time.sleep(5)
            Browser.ErrorTest(self)


    def ErrorTest(self): #İnstagram'a giriş yaptığımız kısımda bu kısım çalışacaktır. Herhangi bir nedenden dolayı hesabımıza giremezsek kodu en baştan çalıştıracaktır.
            print("Profile başarılı şekilde giriş yapıldı.")
            print("Hesabınıza başarıyla giriş yapılmıştır.")
            print("Bağlanılan hesabın adı: ", kb.nickname)   
            self.browser.get("https://www.instagram.com/"+kb.nick)
            Browser.CreateList(self)
        
    def CreateList(self):
        print("Liste elemanları teke düşürülüyor...")
        file = open("Lists/İnstagram_takip.txt" , "r").readlines() #sayfaadan çektiğimiz
        file2 = open("Lists/İnstagram_total.txt", "r").readlines() #sayfadan çektiğimiz
        filecontrol = open("Lists/İnstagram_total.txt" , "a") #isim teke düşer
        list = []

        for line in file2: #bu kısımdan diğer fonksiyona geçene kadar gizli hesapları teke düşürür
            list.append(line)
        for line in file:
            if line not in list:
                filecontrol.write(line)
                list.append(line)
        filecontrol.close()
        Browser.FollowList(self)


    def FollowList(self): #Takip atılacak kullanıcıların listesini oluşturur
        print("Takip atılacaklar listesi hazırlanıyor...")
        file = open("Lists/İnstagram_total.txt", "r").readlines()
        file2 = open("Lists/İnstagram_{}_gt.txt".format(kb.nickname), "r").readlines()
        filecontrol = open("Lists/İnstagram_follow.txt","w")
        ls = []
        lst = []
        for i in file2:
            ls.append(i)
        for j in file:
            if j not in ls:
                filecontrol.write(j) 
                #lst.append(j)
            #for k in lst:
            #filecontrol.write(k) 
        filecontrol.close()    
        Browser.SendFollow(self)

    def SendFollow(self):
        global takip_etme, follow_list
        print("Takip etme ekranına gelinmiştir.")
        file = open("Lists/İnstagram_follow.txt","r").readlines()
        #file2 = open("Lists/İnstagram_{}_gt.txt".format(kb.nickname), "a")
        for i in file:
            time.sleep(1)
            print("Takip atılacak kullanıcının hesabı: ", i)
            self.browser.get("https://www.instagram.com/{}".format(i))
            WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
            time.sleep(2)
            try:
                try:
                    takip = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button")
                except:
                    takip = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button")
                finally:
                    if takip.text == "Takip Et":
                        takip.click()
                        takip_etme += 1
                        follow_list.append(i)
                        print("Takip edilen {}. hesaptır.".format(takip_etme))
                    elif takip.text == "Sen de Onu Takip Et":
                        follow_list.append(i)
                    else:
                        follow_list.append(i)
                        print("Kullanıcıyı zaten takip ediyorsunuz")
                    if takip_etme > kb.istek_takip:
                        Browser.End(self)
            except:
                print("Bir nedenden dolayı kullanıcıya takip atılamamıştır. Diğer kullanıcıya geçiliyor.")
                follow_list.append(i)
                try:
                    try:  #gizli hesap olan profiller için çalışma durumu
                        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/h2")
                        follow_list.append(i)
                        print("Gizli hesap bulunmuştur.")
                    except: #kullanıcı adına göre bir profil bulunamama durumu
                        self.browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a/div/div/img")
                        follow_list.append(i)
                        print("Bu kullanıcı adına göre bir profil bulunamadı.")
                except:
                    try: #sayfaya ulaşamama hatası
                        hata4 = self.browser.find_element_by_xpath("/html/body/div/div[1]/div/div/h2")
                        if hata4 == "Üzgünüz, bu sayfaya ulaşılamıyor.":
                            follow_list.append(i)
                    except: #yukarıda yazılı olan hatalardan hiçbiri olmazsa, ekstrem dışı bir sorun olursa bu kısım çalışacaktır.
                        print("Kod sonlandırılmıştır. {} adet kullanıcıya takip atılmıştır.".format(takip_etme))
                        time.sleep(1)
                        Browser.End(self)
                if takip_etme > kb.istek_takip:
                    Browser.End(self)
        Browser.Lists(self)        

    def Lists(self):
        print(follow_list)
        print("Profili ziyaret edilen kullanıcılar listeye ekleniyor")
        file = open("Lists/İnstagram_{}_gt.txt".format(kb.nickname), "a")
        file2 = open("Lists/İnstagram_{}_gt.txt".format(kb.nickname), "r").readlines()
        for i in follow_list:
            if i not in file2:
                file.write(i)
        file.close()    
        time.sleep(1)
        Browser.Toplam()


    def Toplam(): #Python chat bildirimi
        global say
        say = 1
        followfiletotal = open("Lists/Gardrops_total.txt" , "r").readlines() #Bu kullanıcılara takip atar
        for i in followfiletotal:
            say += 1
        print("""Merhaba Oguz Tasdemir, ben Amoyt Bot. Gardrops botunuz basariyla tamamlanmistir
        {} adet kullanıcıya takip atılmıştır.""".format(takip_etme))
        Browser.GetMail()

    def GetMail(): #Gmail bildirimi
        print("Mail gönderme işlemi başarıyla tamamlanmıştır.")
        content = """Merhaba Oguz Tasdemir, ben Amoyt Bot. Gardrops botunuz basariyla tamamlanmistir
        {} adet kullanıcıya takip atılmıştır.""".format(takip_etme)
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("GÖNDEREN KİŞİNİN MAİL ADRESİ","GÖNDEREN KİŞİNİN MAİL ADRESİNİN ŞİFRESİ")
        mail.sendmail("GÖNDEREN KİŞİNİN MAİL ADRESİ","GÖNDERİLECEK KİŞİNİN MAİL ADRESİ",content)
        time.sleep(1)
        Browser.GetMobile()

    def GetMobile(): #telefon bildirimi
        print("Telefona bildirim gönderme işlemi başarıyla tamamlanmıştır.")
        endpoint = 'https://api.mynotifier.app'
        apikey = '' #apikeyinizi buraya girin
        message = "Amoyt Bot"

        description = """Merhaba Oguz Tasdemir, ben Amoyt Bot. Gardrops botunuz basariyla tamamlanmistir
        {} adet kullanıcıya takip atılmıştır.""".format(takip_etme)
        requests.post(endpoint,{
            "apiKey": apikey,
            "message": message,
            "description": description,
            "type": "success",
        })
        Browser.End()        

    def End():
        try:
            print("Sistemden çıkış yapılıyor...")
            sys.exit()
        except:
            print("Hata ekranına gelindi...")
        finally:
            sys.exit()
            time.sleep(1000) #ekstrem bir durumdan dolayı botumuz kapanmazsa bizim manuel kapatmamız için gerekli süreyi sağlar
        



    