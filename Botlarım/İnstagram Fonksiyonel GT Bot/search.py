import time, random,sys,requests,smtplib
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import kullanıcı as kb
from webbrowser import Chrome

a = 1
takip_sayisi = 0
nick = []

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
            #Bu kısım hata ekranı gördüğümüz zaman eklenecektir
            print("Hesabınıza başarıyla giriş yapılmıştır.")
            print("Bağlanılan hesabın adı: ", kb.nickname)   
            self.browser.get("https://www.instagram.com/"+kb.nick)
            Browser.CheckProfile(self)


    def CheckProfile(self): #Takipçiyi kontrol edecek
        global takip_sayisi, a, nick
        try: #hesap gizli değilse
            takipçi = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div")
            takip = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div") 
        except: #hesap gizliyse
            takipçi = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/div")
            takip = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/div") 

        try: #takipçi listesinde . var ise onu silmek için bu kulanılacak
            try:
                takipçi = takipçi.text.replace(".", "")
                takipçi = takipçi.replace(" takipçi", "")
                takipçi = int(takipçi)
            except:
                takipçi = takipçi.text.replace(",", "")
                takipçi = takipçi.replace(" takipçi", "")
                takipçi = int(takipçi)
        except: #takipçi listesinde . yok ise bu kısım çalışacak
                takipçi = takipçi.text.replace(" takipçi", "")
                takipçi = int(takipçi)
 
        try: #takip edilenler listesinde . var ise onu silmek için bu kulanılacak
            try:
                takip = takip.text.replace(".", "")
                takip = takip.replace(" takip", "")
                takip = int(takip)
            except:
                takip = takip.text.replace(",", "")
                takip = takip.replace(" takip", "")
                takip = int(takip)
        except: #takip edilenler listesinde . yok ise bu kısım çalışacak
            takip = takip.text.replace(" takip", "")
            takip = int(takip)
        print("Bu kullanıcının takipçi-takip sayısı: {} {}".format(takipçi,takip))

        if takipçi < 15: #Takipçi sayısı 15'den düşük ise bunu yapacak
            self.browser.back()
            WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
            self.browser.refresh()
            Browser.NextProfile(self)

        if takipçi <= takip: #Takip edilen kişi sayısı eğer takipçi sayısından daha çoksa bunu yapacaktır
            print("Takip edilen kullanıcı sayısı takipçi sayısından büyük olan {}. kullanıcı bulunmuştur.".format(a))
            a += 1
            isim = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/h2")
            nick.append(isim.text)
        Browser.NextProfile(self)


    def NextProfile(self): #hesap gizli değilse bu işlemi yapıyor
        try:
            print("Gizli Hesap kontrolü yapılıyor.")
            gizli = self.browser.find_element_by_class_name("rkEop")
            print(gizli.text)
            print("Hesap gizlidir.")
            self.browser.back()
            WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
            time.sleep(1)
            self.browser.refresh()
            WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
            time.sleep(1)
            sayi = random.randint(1,10)
            self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div").click()
            WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)     
            time.sleep(10)
            self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/span/a/span".format(sayi)).click()
            WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
            print("Listedeki {}. kişinin profiline girilmiştir.".format(sayi))
            print()
            time.sleep(3)
            if a <= kb.takip_atma:
                Browser.CheckProfile(self)
            else:
                Browser.List(self)
            Browser.CheckProfile(self)   
        except:
           try: 
            print("Bir sonraki kullanıcıya geçiliyor.")
            sayi = random.randint(1,10)
            self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div").click()
            WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)     
            time.sleep(10)
            self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/span/a/span".format(sayi)).click()
            WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
            print("Listedeki {}. kişinin profiline girilmiştir.".format(sayi))
            print()
            time.sleep(3)
            if a <= kb.takip_atma:
                Browser.CheckProfile(self)
            else:
                Browser.List(self)
           except: #Herhangi bir gecikmeden - internet kesintisinden dolayı çekilen nicklerin kaybolmaması için direkt listeye yollanmasını sağlar
               print("Bota erişim kesilmiştir. Tekrar bağlanılmaya çalışılıyor")
               time.sleep(1)
               Browser.ErrorTry(self,sayi)

    def ErrorTry(self,sayi):
        try:
            self.browser.refresh()
            time.sleep(5)
            self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div").click()
            WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)     
            time.sleep(10)
            self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/span/a/span".format(sayi)).click()
            WebDriverWait(Chrome, 0, poll_frequency=0.5, ignored_exceptions=None)
            print("Listedeki {}. kişinin profiline girilmiştir.".format(sayi))
            print()
            time.sleep(3)
            Browser.CheckProfile(self)
        except:
            print("Tekrar bağlanma başarısız. Liste elemanı çağırılıyor.")
            time.sleep(1)
            Browser.List(self)


    def List(self):
        print("Listeye ekleme yapılıyor...")
        dosya = open("Lists/İnstagram_takip.txt","r").readlines()
        dosya2 = open("Lists/İnstagram_takip.txt","a")
        for i in nick:
            if i not in dosya:
                dosya2.write("{}\n".format(i))
        dosya2.close()
        Browser.Toplam()


    def Toplam(): #Python chat bildirimi
        global say
        say = 1
        followfiletotal = open("Lists/Gardrops_total.txt" , "r").readlines() #Bu kullanıcılara takip atar
        for i in followfiletotal:
            say += 1
        print("""Merhaba Oguz Tasdemir, ben Amoyt Bot. Gardrops botunuz basariyla tamamlanmistir
        {} adet geri takip etme potansiyeli olan kullanıcı bulumuştur.""".format(a))
        Browser.GetMail()

    def GetMail(): #Gmail bildirimi
        print("Mail gönderme işlemi başarıyla tamamlanmıştır.")
        content = """Merhaba Oguz Tasdemir, ben Amoyt Bot. Gardrops botunuz basariyla tamamlanmistir
        {} adet geri takip etme potansiyeli olan kullanıcı bulumuştur.""".format(a)
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
        {} adet geri takip etme potansiyeli olan kullanıcı bulumuştur.""".format(a)
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
        
        
