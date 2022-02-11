import random
import sys

pc_min = 1
pc_max = 1000   #1 ile kaç arasında olmasını istiyorsan bunu değiştir
a = 0
sayaç = 0

while a == 0:
    pc = random.randint(pc_min,pc_max)
    print("Bilgisayarın tahmini: ", pc)
    tahmin = input("Sayınız daha büyük ise (b), daha küçük ise (k), tahmin doğru ise (e), kapatmak için (q)")
    
        
    if tahmin == "b" or tahmin == "B":
        print("Daha büyük söylemen gerek.")
        pc_min = pc
       
    elif tahmin == "k" or tahmin == "K":
        print("Daha büyük söylemen gerek.")
        pc_max = pc    
        
    elif tahmin == "e" or tahmin == "E":
        print("Tahmininiz başarılı. Tebrikler")
        #Bu kısma (break) de ekleyebilirsin. Döngüden çıkmanı sağlar ve bu yüzden oyun sona erer.
        #Bu kısma (sys.exit()) de ekleyebilirsin. Döngüden çıkmanı sağlar ve bu yüzden oyun sona erer.
        a = 1
        
    elif tahmin == "q" or tahmin =="Q":
        print("Oyundan başarıyla çıkış yapılıyor.")
        #Bu kısma (a = 1)'de yapabilirsin. Döngüden çıkmanı sağlar ve bu yüzden oyun sona erer.
        #Bu kısma (break) de ekleyebilirsin. Döngüden çıkmanı sağlar ve bu yüzden oyun sona erer.
        sys.exit()
    
    
#Tur sayıları    
    if sayaç < 10:      # Tahmin sayısını azaltıp arttırmak istersen bu 10 sayısını değiştir.
        sayaç += 1
        print("Bilgisayar {} tahmin hakkını kullandı. {} tahmin hakkı kaldı. ".format(sayaç,(10-sayaç)))
    else:
        print("Tahmin hakkı bitti.")
        #Bu kısma (a = 1)'de yapabilirsin. Döngüden çıkmanı sağlar ve bu yüzden oyun sona erer.
        #Bu kısma (sys.exit()) de ekleyebilirsin. Döngüden çıkmanı sağlar ve bu yüzden oyun sona erer.
        break
    
    
    