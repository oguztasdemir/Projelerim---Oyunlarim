import random
import sys

print("""**************************************
      
Doğruluk Cesaretlilik Oyununa Hoşgeldiniz!!!

Puanlandırma sistemi:
Doğruluk sorusunu her cevapladığınızda 1 puan kazanırsınız, her pas geçtiğinizde 1 puan kaybedersiniz.
Cesaretlik sorunda her yaptığınız için 2 puan kazanırsınız, her pas geçtiğinizde 2 puan kaybedersiniz.

Hedef skor ve oyuncu sayısı oyun başlangıcında kullanıcılardan istenilir.

**************************************""")


gamer_list = []     #Oyuncu listesi, kaç oyuncu olucağını belirtmek için böyle boş bıraktım
gamer_point = []    #Tüm puanlar 0'dan başlayacak. Oyuncu sayısı kadar içeriği dolacak.
secim_list = []     #Soru oylaması
pc_soru = []        #Bilgisayarın bize sunduğu 3 soru burada listelenecek.
sl = []
os = 0
x = int(input("Kaç oyuncu oynayacak: "))
end = int(input("Oyunu bitirmek için gerekli puanı girin: "))
so = 0
iddaa = 0


for i in range(1):
    sayac = 1
    while sayac <= x:
        gamer_list.append(input("{}. oyuncnun adınızı girin: ".format(sayac)))
        gamer_point_add = 0
        gamer_point.append(gamer_point_add)
        sayac += 1



while True: 
    def Sorular(gamer_list):
        truth = ["1. soru", "2. soru", "3. soru", "4. soru", "5. soru", "6. soru"]
        dare = ["1. soru", "2. soru", "3. soru", "4. soru", "5. soru", "6. soru"]
        secim = input("Doğruluk için (d) - Cesaret için (c) - Oyunu kapatmak için (q)")
        Sormak(pc_soru,truth,dare,secim)



    def Sormak(pc_soru,truth,dare,secim):
        
        pc_soru = []
        
        if secim == "d" or secim == "D":
            soru1 = random.sample(truth,1)
            soru2 = random.sample(truth,1)
            soru3 = random.sample(truth,1)
            pc_soru.append(soru1)
            pc_soru.append(soru2)
            pc_soru.append(soru3)
            print(str(pc_soru))
            Seçim(iddaa,sl,secim_list,so,pc_soru,secim,truth,dare)

        elif secim == "c" or secim == "C":
            soru1 = random.sample(dare,1)
            soru2 = random.sample(dare,1)
            soru3 = random.sample(dare,1)
            pc_soru.append(soru1)
            pc_soru.append(soru2)
            pc_soru.append(soru3)
            print(str(pc_soru))
            Seçim(iddaa,sl,secim_list,so,pc_soru,secim,truth,dare)

        elif secim == "q" or secim == "Q":
            print("oyundan çıkılıyor...")
            sys.exit()


    def Seçim(iddaa,sl,secim_list,so,pc_soru,secim,truth,dare):
        secim_list = []
        sl = []
        so = os+1
        while int(so) < int(x):
            secis = input("Hangi soruyu/iddaayı yaptırmak istiyorsanız seçin (1-2-3)")
            print("{} adlı oyuncu {} numaralı soruyu/iddaayı seçti.".format(gamer_list[so],secim))
            secim_list.append(int(secis))
            so += 1
            
        print(secim_list)
        sl.append(secim_list.count(1))
        sl.append(secim_list.count(2))
        sl.append(secim_list.count(3))
        print(sl)
        
        if sl[0] > sl[1] and sl[0] > sl[2]:
            print("En çok seçilen soru/iddaa 1. seçenektir.")
            iddaa = 0        
            print("Seçilen soru/iddaa: ", pc_soru[iddaa])
            Cevaplamak(gamer_point,os,end,truth,dare,secim)
            
        elif sl[1] > sl[0] and sl[1] > sl[2]:
            print("En çok seçilen soru/iddaa 2. seçenektir.")
            iddaa = 1
            print("Seçilen soru/iddaa: ", pc_soru[iddaa])
            Cevaplamak(gamer_point,os,end,truth,dare,secim)
            
        elif sl[2] > sl[1] and sl[2] > sl[0]:
            print("En çok seçilen soru/iddaa 3. seçenektir.")
            iddaa = 2
            print("Seçilen soru/iddaa: ", pc_soru[iddaa])
            Cevaplamak(gamer_point,os,end,truth,dare,secim)
            
        else:
            print("Seçilen iddaaların sayısı eşittir. Lütfen tekrar seçim yapınız.")
            Seçim(iddaa,sl,secim_list,so,pc_soru,secim,truth,dare)
                    




    def Cevaplamak(gamer_point,os,end,truth,dare,secim): 
        if secim == "d" or secim =="D":
            print("")
            dogruluk = input("Sorunun cevabını buraya yazın. Eğer soruya cevap vermeyekceseniz (p) yazın. Pass geçtiğiniz taktirde ceza puanı yersiniz. ")
            if (dogruluk == "p" or dogruluk =="P"):
                print("")

                print("Soruya cevap vermediniz. Ceza puanı yediniz. Sıra diğer oyuncuya geçiyor.")
                gamer_point[os] -= 1
            else:
                print("")
                print("Soruya cevap verdiniz. Sıra diğer oyuncuya geçiyor.")
                gamer_point[os] += 1


            if int(gamer_point[os]) < int(end):
                print("")
                print("Şuanki puanınız {}, hedef puana ulaşabilmek için {} puan daha gereklidir. Sıra diğer oyuncuya geçiyor." .format(gamer_point[os],int(end)-int(gamer_point[os])))
            else:
                print("")
                print("Tebrikler oyunu kazandınız.")
                sys.exit()
                

        elif secim == "c" or secim == "C":     
            print("")
            cesaret = input("Sorunun cevabını buraya yazın. Eğer soruya cevap vermeyekceseniz (p) yazın. Pass geçtiğiniz taktirde ceza puanı yersiniz. ")
            if (cesaret == "p" or cesaret =="P"):
                print("")
                print("İstenilen şeyi yapamadın.. Ceza puanı yediniz. Sıra diğer oyuncuya geçiyor.")
                gamer_point[os] -= 2
            else:
                print("")
                print("İstenilen şeyi yaptınız. Puanınız ekleniyor.")
                gamer_point[os] += 2


            if int(gamer_point[os]) < int(end):
                print("")
                print("Şuanki puanınız {}, hedef puana ulaşabilmek için {} puan daha gereklidir. Sıra diğer oyuncuya geçiyor." .format(gamer_point[os],int(end)-int(gamer_point[os])))
            else:
                print("")
                print("Tebrikler oyunu kazandınız.")
                sys.exit()
        


    os += 1
    if os < x:
        os = os
    elif os == x:
        print("Oyun baştakine döndü")
        os = 0
        
    so = os
        
    print("")
    print("Sıra {} adlı oyuncuda.".format(gamer_list[os]))
    print("_____________________________________________")
    
    print(gamer_list)
    print(gamer_point)
    Sorular(gamer_list)













