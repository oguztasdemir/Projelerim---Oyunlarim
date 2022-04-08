#İnstagram_takip.txt kısmındaki içerikleri İnstagram_total ile karşılaştırıp isimleri teke düşürür

file = open("Lists/İnstagram_takip.txt" , "r").readlines() #sayfaadan çektiğimiz
file2 = open("Lists/İnstagram_total.txt", "r").readlines() #sayfadan çektiğimiz
filecontrol = open("Lists/İnstagram_total.txt" , "w") #isim teke düşer
count = 0
list = []

for line in file2 :
    list.append(line)
for line in file:
    if line not in list:
        filecontrol.write(line)
        list.append(line)

filecontrol.close()


