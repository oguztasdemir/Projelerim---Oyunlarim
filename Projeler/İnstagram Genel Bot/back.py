#expertleri kontrol edeceğim bazı yerleri sorun çıkartıyor. Kodun ilerlemesi engelleniyor.

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import kullanıcı as kb
import random
a = 1
class Browser:
    
    sayac2 = 1
    def __init__(self,link):
        self.link = link
        Browser.goInstagram(self)


    def goInstagram(self): #İnstagramı açar.
        try:
            print("Google 2 saniye içerisinde açılacaktır.")
            time.sleep(2)
            self.browser = webdriver.Chrome("/Users/yarentasdemir/Desktop/chromedriver")
            self.browser.get(self.link)
            time.sleep(1)
            Browser.login(self)
    
        except:
            print("Beklenmedik bir sorunla karşılaşıldı. Kod 2 saniye içerisinde tekrar başlatılacaktır")
            time.sleep(2)
            Browser.goInstagram(self)
    

    def login(self): #Hesabımıza girmemizi sağlar. Bu kısımda kullanıcı.py adlı kısımdaki hesaba giriş yapacaktır.
        try:
            print("İnstagram başarılı şekilde açıldı.")
            time.sleep(1)
            username = self.browser.find_element_by_name("username")
            password = self.browser.find_element_by_name("password")
            username.send_keys(kb.nickname)
            password.send_keys(kb.password)
            time.sleep(1)
            login1 = self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div")
            login1.click()
            time.sleep(5)
            Browser.ErrorTest(self)
            
        except:
            print("Hesaba giriş kısmında beklenmedik bir sorunla karşılaşıldı. Kod tekrardan başlatılacaktır.")
            time.sleep(2)
            Browser.goInstagram(self)

    def ErrorTest(self): #İnstagram'a giriş yaptığımız kısımda bu kısım çalışacaktır. Herhangi bir nedenden dolayı hesabımıza giremezsek kodu en baştan çalıştıracaktır.
        
            #Bu kısım hata ekranı gördüğümüz zaman eklenecektir
            print("Hesabınıza başarıyla giriş yapılmıştır.")
            print("Bağlanılan hesabın adı: ", kb.nickname)   
            self.browser.get("https://www.instagram.com/"+kb.nick)
            Browser.getFollowers(self)

     

    def getFollowers(self): #Hesabımızla etkileşimde olan bir kişinin profiline gidecektir.
        try: #Girdiğimiz hesapta paylaşılan son fotoğrafa tıklayıp bu fotoğrafı eğenen son kişinin profiline gidecektir.
            print("Profilinize başarılı şekilde giriş yapıldı.")
            time.sleep(2)
            followers = self.browser.find_element_by_class_name("_9AhH0")
            followers.click()
            print("Son paylaştığınız fotoğrafa başarılı şekilde tıklama yapıldı.")
            time.sleep(2)
            followers2 = self.browser.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/div[2]/div/a/div")
            followers2.click()
            print("Fotoğrafı beğenenlerin listesi başarılı şekilde açılmıştır.")
            time.sleep(2)
            sayi1 = random.randint(2,10)
            if sayi1 == 2:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/span/a/span")
                followers3.click()
                print("Fotoğrafı beğenen 2. kişinin profiline başarılı şekilde gidilmiştir.")
                time.sleep(2)
            elif sayi1 == 3:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[3]/div[2]/div[1]/div/span/a/span")
                followers3.click()
                print("Fotoğrafı beğenen 3. kişinin profiline başarılı şekilde gidilmiştir.")
                time.sleep(2)
            elif sayi1 == 4:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div/span/a/span")
                followers3.click()
                print("Fotoğrafı beğenen 4. kişinin profiline başarılı şekilde gidilmiştir.")
                time.sleep(2)
            elif sayi1 == 5:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[5]/div[2]/div[1]/div/span/a/span")
                followers3.click()
                print("Fotoğrafı beğenen 5. kişinin profiline başarılı şekilde gidilmiştir.")
                time.sleep(2)
            elif sayi1 == 6:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[6]/div[2]/div[1]/div/span/a/span")
                followers3.click()
                print("Fotoğrafı beğenen 6. kişinin profiline başarılı şekilde gidilmiştir.")
                time.sleep(2)
            elif sayi1 == 7:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[7]/div[2]/div[1]/div/span/a/span")
                followers3.click()
                print("Fotoğrafı beğenen 7. kişinin profiline başarılı şekilde gidilmiştir.")
                time.sleep(2)
            elif sayi1 == 8:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[8]/div[2]/div[1]/div/span/a/span")
                followers3.click()
                print("Fotoğrafı beğenen 8. kişinin profiline başarılı şekilde gidilmiştir.")
                time.sleep(2)
            elif sayi1 == 9:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[9]/div[2]/div[1]/div/span/a/span")
                followers3.click()
                print("Fotoğrafı beğenen 9. kişinin profiline başarılı şekilde gidilmiştir.")
                time.sleep(2)
            elif sayi1 == 10:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[10]/div[2]/div[1]/div/span/a/span")
                followers3.click()
                print("Fotoğrafı beğenen 10. kişinin profiline başarılı şekilde gidilmiştir.")
                time.sleep(2)                                
            Browser.check_followers(self,a)
            
        except: #Eğer girilen hesapta fotoğraf yok ise girdiğimiz hesabın takipçiler sayfasına erişim sağlayacaktır.
            followers = self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a/div")
            time.sleep(2)
            sayi2 = random.randint(2,10)
            if sayi2 == 2:
                follower = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[2]/div/div[2]/div[1]/div/div/span/a/span")
                follower.click()
                print("Takipçi listenizdeki 2. kullanıcının profiline gidiliyor.")
                time.sleep(3)
            elif sayi2 == 3:
                follower = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[3]/div/div[2]/div[1]/div/div/span/a/span")
                follower.click() 
                print("Takipçi listenizdeki 3. kullanıcının profiline gidiliyor.")
                time.sleep(3)           
            elif sayi2 == 4:
                follower = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[4]/div/div[2]/div[1]/div/div/span/a/span")
                follower.click()
                print("Takipçi listenizdeki 4. kullanıcının profiline gidiliyor.")
                time.sleep(3)
            elif sayi2 == 5:
                follower = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[5]/div/div[2]/div[1]/div/div/span/a/span")
                follower.click()
                print("Takipçi listenizdeki 5. kullanıcının profiline gidiliyor.")
                time.sleep(3)
            elif sayi2 == 6:
                follower = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[6]/div/div[2]/div[1]/div/div/span/a/span")
                follower.click()
                print("Takipçi listenizdeki 6. kullanıcının profiline gidiliyor.")
                time.sleep(3)
            elif sayi2 == 7:
                follower = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[7]/div/div[2]/div[1]/div/div/span/a/span")
                follower.click()
                print("Takipçi listenizdeki 7. kullanıcının profiline gidiliyor.")
                time.sleep(3)
            elif sayi2 == 8:
                follower = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[8]/div/div[2]/div[1]/div/div/span/a/span")
                follower.click()
                print("Takipçi listenizdeki 8. kullanıcının profiline gidiliyor.")
                time.sleep(3)
            elif sayi2 == 9:
                follower = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[9]/div/div[2]/div[1]/div/div/span/a/span")
                follower.click()
                print("Takipçi listenizdeki 9. kullanıcının profiline gidiliyor.")
                time.sleep(3)
            elif sayi2 == 10:
                follower = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[10]/div/div[2]/div[1]/div/div/span/a/span")
                follower.click()
                print("Takipçi listenizdeki 10. kullanıcının profiline gidiliyor.")
                time.sleep(3)                
            Browser.check_followers(self,a)


    def check_followers(self,a): #Takip-Takipçi karşılaştırılması yapılacaktır
        takipçi = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div")
        takip = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div") 

        try: #takipçi listesinde . var ise onu silmek için bu kulanılacak
            takipçi = takipçi.text.replace(" takipçi", "")
            takipçi = takipçi.replace(".", "")
            takipçi = int(takipçi)
            print(takipçi)
        except: #takipçi listesinde . yok ise bu kısım çalışacak
            takipçi = takipçi.text.replace(" takipçi", "")
            takipçi = int(takipçi)
            print(takipçi)

        try: #takip edilenler listesinde . var ise onu silmek için bu kulanılacak
            takip = takip.text.replace(" takip", "")
            takip = takip.replace(".", "")
            takip = int(takip)
            print(takip)
        except: #takip edilenler listesinde . yok ise bu kısım çalışacak
            takip = takip.text.replace(" takip", "")
            takip = int(takip)
            print(takip)        


        if takipçi <= takip: #Takip edilen kişi sayısı eğer takipçi sayısından daha çoksa bunu yapacaktır
            print("Takip edilen kişi sayısı, takipçiden fazla olduğu için kullanıcı takip edilmiştir. ")
            takip_et = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button")
            print(takip_et.text)
            time.sleep(2)
            try:
                if takip_et.text == "Takip Et":
                    print("Kullanıcı başarıyla takip edilmiştir. Takip edilen {}. hesaptır".format(a))
                    takip_et.click()
                    time.sleep(1)
                    a += 1
                    Browser.TakipGeç(self)
                    
                elif takip_et.text == "Sen de Onu Takip Et":
                    print("Kullanıcı sizi takip ediyor")
                    time.sleep(1)
                    Browser.TakipGeç(self)
                else:
                    print("Kullanıcıyı zaten takip ediyorsunuz. 1")
                    time.sleep(1)
                    Browser.TakipGeç(self)
            except:
                print("Kullanıcı zaten takip ediyorsunuz. 2")
                time.sleep(2)
                Browser.TakipGeç(self)

        elif takipçi > takip: #Takipçi sayısı eğer takip edilen kişi sayısından daha çoksa bunu yapacaktır
            print("Takip edilen kişi sayısı, takipçiden az olduğu için kullanıcı takip edilmemiştir.")
            Browser.TakipGeç(self)



    def TakipGeç(self): #Kullanıcıyı takip etmeye çalışmadan geçilecek kısımdır
        print("TakipGeç fonksiyonu çalışıyor.")
        try: #Hesap gizli değilse takipçi listesine girilecektir
            diger_takipci = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div")
            diger_takipci.click()
            sayi3 = random.randint(2,10)
            time.sleep(3)
            if sayi3 == 2:
                takip_at = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[2]/div/div[2]/div[1]/div/div/span/a/span")
                takip_at.click()
                print("Listedeki 2. kişinin profiline girilmiştir.")
            elif sayi3 == 3:
                takip_at = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[3]/div/div[2]/div[1]/div/div/span/a/span")
                takip_at.click()
                print("Listedeki 3. kişinin profiline girilmiştir.")                
            elif sayi3 == 4:
                takip_at = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[4]/div/div[2]/div[1]/div/div/span/a/span")
                takip_at.click()
                print("Listedeki 4. kişinin profiline girilmiştir.")    
            elif sayi3 == 5:
                takip_at = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[5]/div/div[2]/div[1]/div/div/span/a/span")
                takip_at.click()
                print("Listedeki 5. kişinin profiline girilmiştir.") 
            elif sayi3 == 6:
                takip_at = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[6]/div/div[2]/div[1]/div/div/span/a/span")
                takip_at.click()
                print("Listedeki 6. kişinin profiline girilmiştir.") 
            elif sayi3 == 7:
                takip_at = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[7]/div/div[2]/div[1]/div/div/span/a/span")
                takip_at.click()
                print("Listedeki 7. kişinin profiline girilmiştir.") 
            elif sayi3 == 8:
                takip_at = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[8]/div/div[2]/div[1]/div/div/span/a/span")
                takip_at.click()
                print("Listedeki 8. kişinin profiline girilmiştir.") 
            elif sayi3 == 9:
                takip_at = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[9]/div/div[2]/div[1]/div/div/span/a/span")
                takip_at.click()
                print("Listedeki 9. kişinin profiline girilmiştir.") 
            elif sayi3 == 10:
                takip_at = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[10]/div/div[2]/div[1]/div/div/span/a/span")
                takip_at.click()
                print("Listedeki 10. kişinin profiline girilmiştir.") 
            time.sleep(3)
            print("Hata bulunamamıştır")
            Browser.check_followers(self,a)           

        except: #Hesap gizliyse 1 önceki sayfaya erişim sağlanacaktır
            time.sleep(3)
            print("Hata bulundu")
            Browser.GizliHesap(self)

    def GizliHesap(self): #Bir nedenden dolayı takipçi listesine erişemezsek bu kısım kullanılacaktır
        print("GizliHesap fonksiyonu çalışıyor")
        self.browser.back()
        self.browser.refresh()
        time.sleep(2)
        sayi4 = random.randint(2,10)
        try:          
            diger_takipci = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div")
            diger_takipci.click()       
            time.sleep(2)               
            if sayi4 == 2:    
                takipat = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[2]/div/div[2]/div[1]/div/div/span/a/span")
                time.sleep(1)
                takipat.click()
                print("Listedeki 2. kişinin profiline girilmiştir.")      
            elif sayi4 == 3:
                takipat = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[3]/div/div[2]/div[1]/div/div/span/a/span")
                time.sleep(1)
                takipat.click()
                print("Listedeki 3. kişinin profiline girilmiştir.")             
            elif sayi4 == 4:
                takipat = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[4]/div/div[2]/div[1]/div/div/span/a/span")
                time.sleep(1)
                takipat.click()
                print("Listedeki 4. kişinin profiline girilmiştir.")  
            elif sayi4 == 5:
                takipat = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[5]/div/div[2]/div[1]/div/div/span/a/span")
                time.sleep(1)
                takipat.click()
                print("Listedeki 5. kişinin profiline girilmiştir.") 
            elif sayi4 == 6:
                takipat = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[6]/div/div[2]/div[1]/div/div/span/a/span")
                time.sleep(1)
                takipat.click()
                print("Listedeki 6. kişinin profiline girilmiştir.") 
            elif sayi4 == 7:
                takipat = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[7]/div/div[2]/div[1]/div/div/span/a/span")
                time.sleep(1)
                takipat.click()
                print("Listedeki 7. kişinin profiline girilmiştir.") 
            elif sayi4 == 8:
                takipat = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[8]/div/div[2]/div[1]/div/div/span/a/span")
                time.sleep(1)
                takipat.click()
                print("Listedeki 8. kişinin profiline girilmiştir.") 
            elif sayi4 == 10:
                takipat = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[9]/div/div[2]/div[1]/div/div/span/a/span")
                time.sleep(1)
                takipat.click()
                print("Listedeki 9. kişinin profiline girilmiştir.") 
            elif sayi4 == 10:
                takipat = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[10]/div/div[2]/div[1]/div/div/span/a/span")
                time.sleep(1)
                takipat.click()
                print("Listedeki 10. kişinin profiline girilmiştir.") 
            print("Hata bulunmamıştır.")                                            
        except:
            follower2 = self.browser.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/div[2]/div/a/div")
            follower2.click()
            print("Fotoğrafı beğenenlerin listesi başarılı şekilde açılmıştır.")
            if sayi4 == 2:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/span/a/span")
                time.sleep(1)
                followers3.click()
                print("Fotoğrafı beğenen 2. kişinin profiline başarılı şekilde gidilmiştir.")
                time.sleep(2)
            elif sayi4 == 3:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[3]/div[2]/div[1]/div/span/a/span")
                time.sleep(1)
                followers3.click()
                print("Fotoğrafı beğenen 3. kişinin profiline başarılı şekilde gidilmiştir.")
                time.sleep(2)
            elif sayi4 == 4:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div/span/a/span")
                time.sleep(1)
                followers3.click()
                print("Fotoğrafı beğenen 4. kişinin profiline başarılı şekilde gidilmiştir.")
                time.sleep(2)     
            elif sayi4 == 5:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[5]/div[2]/div[1]/div/span/a/span")
                time.sleep(1)
                followers3.click()
                print("Fotoğrafı beğenen 5. kişinin profiline başarılı şekilde gidilmiştir.")
            elif sayi4 == 6:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[6]/div[2]/div[1]/div/span/a/span")
                time.sleep(1)
                followers3.click()
                print("Fotoğrafı beğenen 6. kişinin profiline başarılı şekilde gidilmiştir.")
            elif sayi4 == 7:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[7]/div[2]/div[1]/div/span/a/span")
                time.sleep(1)
                followers3.click()
                print("Fotoğrafı beğenen 7. kişinin profiline başarılı şekilde gidilmiştir.")
            elif sayi4 == 8:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[8]/div[2]/div[1]/div/span/a/span")
                time.sleep(1)
                followers3.click()
                print("Fotoğrafı beğenen 8. kişinin profiline başarılı şekilde gidilmiştir.")
            elif sayi4 == 9:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[9]/div[2]/div[1]/div/span/a/span")
                time.sleep(1)
                followers3.click()
                print("Fotoğrafı beğenen 9. kişinin profiline başarılı şekilde gidilmiştir.")
            elif sayi4 == 10:
                followers3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/div[10]/div[2]/div[1]/div/span/a/span")
                time.sleep(1)
                followers3.click()
                print("Fotoğrafı beğenen 10. kişinin profiline başarılı şekilde gidilmiştir.")
                time.sleep(2) 
            print("Hata bulundu")                        
        Browser.check_followers(self,a)




