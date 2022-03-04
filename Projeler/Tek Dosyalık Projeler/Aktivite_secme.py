import random
import time

home_act = ["","",""]   
out_act = ["","",""]

akt = random.randint(1,2)

if akt == 1:
    h_act = random.randint(1,3)
    print("Evde kalcaksınız")
    print("Yapacağınız aktivite 3 saniye sonra gösterilecektir.")
    time.sleep(3)
    print(home_act[h_act-1])
    
elif akt == 2:
    o_act = random.randint(1,3)
    print("Dışarı çıkacaksınız")
    print("Yapacağınız aktivite 3 saniye sonra gösterilecektir.")
    time.sleep(3)
    print(out_act[o_act-1])