
import random

sayı = random.randint(1,1000)
a = 0
sayaç = 0

while a == 0:
    tahmin = int(input("Tahmininiz: \nOyundan çıkmak istiyorsanız (q)"))
    if sayı < tahmin:
        print("Bilgisayarın tuttuğu sayı, tahmininizden daha düşüktür. Tahmininizi azaltmaya çalışın.")
        sayaç += 1
        print("{} tahmin hakkı kullandınız. {} tahmin hakkınız kaldı.".format(sayaç,(10-sayaç)))
    elif sayı > tahmin:
        print("Bilgisayarın tuttuğu sayı, tahmininizden daha yüksektir.. Tahmininizi arttırmaya çalışın.")
        sayaç += 1
        print("{} tahmin hakkı kullandınız. {} tahmin hakkınız kaldı.".format(sayaç,(10-sayaç)))

    elif sayı == tahmin:
        print("\nTebrikler {}. seferinde sayıyı bildiniz.".format(sayaç))
        break

    elif tahmin == "q":
        break
    
    