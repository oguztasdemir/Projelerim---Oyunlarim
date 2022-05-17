import random
urunler = ["Albeni Kaplama Bar 40 gr","Metro Kaplamalı Bar 36gr","Piko Kaplamalı Bar Portakallı 18gr","CocoStar H. Cevizli Bar 25gr","Çokomilk 24gr","Lavviva 35gr","Çokonat 33gr","Alpella 3gen Beyaz 28gr","Dido Sütlü 35gr","Dido Gold 36gr","Çikolatalı Gofret 36gr","Caramio Kr. Batton 32gr"]
toplu_fiyat = [53.28,44.4,33.36,47.52,33.36,71.28,71.28,44.4,71.28,80.88,73.44,66.48]
tekli_fiyat = [2.22,1.85,1.39,1.98,1.39,2.97,2.97,1.85,2.97,3.37,2.04,2.77]
random_kontrol = []
urun_listem = []

y = 0 #komisyon tutarı
x = 0 #aldığım fiyat
z = 0 #komisyonlu haldeyken kar - zarar yokken koyulabilecek fiyat


def Karma(urunler,toplu_fiyat,tekli_fiyat,random_kontrol):
    global kutu,x
    sayac = 0
    sec = int(input("Koli(17-18 çeşit ürün gibi) seçeneği için 1\nKutu seçeneği için 2\nKodun çalışma prensibi için 3"))
    
    if sec == 1: #Koli seçeneği (toplu fiyat)
        adet = int(input("Kolinize kaç adet ürün eklenilsin."))
        while sayac < adet:
            kutu = random.randint(0,len(urunler)-1)

            if kutu in random_kontrol:
                pass
            elif kutu not in random_kontrol:
                    random_kontrol.append(kutu)
                    sayac += 1
                    print("Eklenilen {}. üründür. Eklenilen ürün: {},Birim fiyatı: {}".format(sayac,urunler[kutu],tekli_fiyat[kutu]))
                    urun_listem.append(urunler[kutu])
                    x += tekli_fiyat[kutu]
        Fiyat()         

    elif sec == 2: #Kutu Seçeneği (tekli fiyat)
        adet = int(input("Kolinize kaç adet ürün eklenilsin."))
        while sayac < adet:
            koli = random.randint(0,len(urunler)-1)

            if koli in random_kontrol:
                pass
            elif koli not in random_kontrol:
                    random_kontrol.append(koli)
                    sayac += 1
                    print("Eklenilen {}. üründür. Eklenilen ürün: {},Kutu fiyatı: {}".format(sayac,urunler[koli],toplu_fiyat[koli]))
                    urun_listem.append(urunler[koli])
                    x += toplu_fiyat[koli]
        Fiyat()  
    
    elif sec == 3:
        print("Kodumuz Trendyol'da komisyon dahil fiyat hesaplama ve rastgele paket içeriği sunma üzerine dayalı bir koddur. Koli seçeneğine tıkladığınızda her üründen 1'er adet ekler ve siz ne kadar ürün eklemek istediğinizi yazdığınızda o kadar ürünün total fiyatını size hesaplayarak koli seçeneğini gösterir. Kutu seçeneğinde de ürünleri kutu (örneğin 36 adet ülker çikolatalı gofret = 1 kutu) şeklinde hesaplayarak sizlere sunmaktadır.")

def Fiyat():   
    global y,z
    y = x*15/85
    z = x + y
    Çıktı()
    
def Çıktı():
    print("________________________")
    print("Ürün Paketi: {}\nÜrün Maaliyeti: {}\nÜrünün komisyonlu hesaplanmış tutarı: {}".format(urun_listem,x,z))
        

Karma(urunler,toplu_fiyat,tekli_fiyat,random_kontrol)









# x * 1.176 = z #komisyon halledilmişi










"""
x + 15x/100 - 15x/100
x + y - ((15x + 15y)/100) = x
100x + 100y (15x + 15y) = 100x
85x +  85y = 100x
85y = 15x
y = 15/85x"""

