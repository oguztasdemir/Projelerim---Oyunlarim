import math
import time

print("""
      
Hesap Makinesi

Toplama = 1
Çıkarma = 2
Çarpma = 3
Bölme = 4
Üs = 5
Karekök = 6
Logaritma = 7
Derece --> Radyan = 8
Radyan --> Derece = 9
Sin = 10
Cos = 11
Tan = 12
Cot = 13      

Çıkış = 14
""")


while True:
    işlem = int(input("Lütfen yapmak istediğiniz işlemi girin: (1-14)"))
    
    if int(işlem == 1):
        print("Toplama İşlemi")
        sayı1 = int(input("Sayıyı giriniz: "))
        sayı2 = int(input("Sayıyı giriniz: "))
        print("Sayıların toplamı: ", sayı1 + sayı2)


    elif int(işlem == 2):
        print("Çıkarma İşlemi")
        sayı1 = int(input("Sayıyı giriniz: "))
        sayı2 = int(input("Sayıyı giriniz: "))
        print("Sayıların farkı: ", sayı1 - sayı2)
        

    elif int(işlem == 3):
        print("Toplama İşlemi")
        sayı1 = int(input("Sayıyı giriniz: "))
        sayı2 = int(input("Sayıyı giriniz: "))
        print("Sayıların çarpımı: ", sayı1 * sayı2)



    elif int(işlem == 4):
        print("Bölme İşlemi")
        sayı1 = int(input("Sayıyı giriniz: "))
        sayı2 = int(input("Sayıyı giriniz: "))
        print("Sayıların bölümü: ", sayı1 / sayı2)


    elif int(işlem == 5):
        print("Üs Bulma")
        sayı1 = int(input("Sayının üs değerini giriniz: "))
        sayı2 = int(input("Sayıyı giriniz: "))
        print("Üslü sayının değeri: ", sayı2 ** sayı1)


    elif int(işlem == 6):
        print("Karekök Bulma")
        sayı = int(input("Sayıyı giriniz: "))
        print("Sayının kökü: ", math.sqrt(sayı))
        

    elif int(işlem == 7):
        print("Logaritma Bulma")
        sayı1 = int(input("Logaritmanın tabanını giriniz "))
        sayı2 = int(input("Sayıyı giriniz: "))
        print("Logaritma değerinin sonucu: ", math.log(sayı2,sayı1))


    elif int(işlem == 8):
        print("Dereceyi Radyana Çevirme")
        sayı = int(input("Sayı giriniz: "))
        print("Derecenin radyanı: ", math.degrees(sayı))


    elif int(işlem == 9):
        print("Radyanı Dereceye Çevirme")
        sayı = int(input("Sayı giriniz: "))
        print("Radyanın derecesi: ", math.radians(sayı))

    elif int(işlem == 10):
        print("Sinüs Bulma")
        seçim = input("Radyan için (r)\nDerece için (d)")
        if seçim == "r" or seçim == "R":
            sayı = int(input("Radyanı giriniz: "))
            print("Radyanın sinüsü: ", math.sin(sayı))
        elif seçim == "d" or seçim == "D":
            sayı = int(input("Dereceyi giriniz: "))
            print("Derecenin sinüsü: ", math.sin(sayı))
            

    elif int(işlem == 11):
        print("Cosinüs Bulma")
        seçim = input("Radyan için (r)\nDerece için (d)")
        if seçim == "r" or seçim == "R":
            sayı = int(input("Radyanı giriniz: "))
            print("Radyanın cosinüsü ", math.cos(sayı))
        elif seçim == "d" or seçim == "D":
            sayı = int(input("Dereceyi giriniz: "))
            print("Derecenin cosinüsü: ", math.cos(sayı))
        


    elif int(işlem == 12):
        print("Tanjant Bulma")
        seçim = input("Radyan için (r)\nDerece için (d)")
        if seçim == "r" or seçim == "R":
            sayı = int(input("Radyanı giriniz: "))
            print("Radyanın tanjantı: ", math.tan(sayı))
        elif seçim == "d" or seçim == "D":
            sayı = int(input("Dereceyi giriniz: "))
            print("Derecenin tanjantı: ", math.tan(sayı))


    elif int(işlem == 13):
        print("Cotanjant Bulma")
        seçim = input("Radyan için (r)\nDerece için (d)")
        if seçim == "r" or seçim == "R":
            sayı = int(input("Radyanı giriniz: "))
            print("Radyanın cotanjantı: ", 1/math.tan(sayı))
        elif seçim == "d" or seçim == "D":
            sayı = int(input("Dereceyi giriniz: "))
            print("Derecenin cotanjantı: ", 1/math.tan(sayı))


    elif (işlem == 14):
        print("Başarıyla çıkış yapılıyor...")
        time.sleep(1)
        break


















