import back,comment,follow,like,save,watch,time
import kullanıcı as kb

choose = int(input("""Lütfen yapmak istediğiniz aşamayı seçin:
Beğeni botu için 1
Yorum botu için 2
Takipçi botu için 3
Kaydetme botu için 4
Video izletme botu için 5
Geri Takibi çalıştırmak için 6"""))

if choose == 1:
    print("Beğeni botu çalışıyor")
    kb.nickname = input("Lütfen bot atılacak sisteme girebilmek için bir fake hesabınızın kullanıcı adını girin: ")
    kb.sifre = input("Lütfen bot atılacak sisteme girebilmek için bir fake hesabınızın kullanıcı adını girin: ")
    kb.link = input("Beğeni atılacak gönderinin linkini yazın: ")
    kb.sayi = int(input("Kaç adet beğeni atılmasını istiyorsanız o miktarı girin (Girilen miktarda beğeni gelmeyecektir. Bunun nedeni siteden kaynaklıdır. Bazı hesaplar engel yemiştir.): "))
    print("Başarılı şekilde yönlendirilmiştir.")
    like.Browser("https://chrome.google.com/webstore/detail/zenmate-free-vpn%E2%80%93best-vpn/fdcgdnkidjaadafnichfpabhfomcebme?hl=tr")
    time.sleep(2)

elif choose == 2:
    print("Yorum botu çalışıyor")
    kb.nickname = input("Lütfen bot atılacak sisteme girebilmek için bir fake hesabınızın kullanıcı adını girin: ")
    kb.sifre = input("Lütfen bot atılacak sisteme girebilmek için bir fake hesabınızın kullanıcı adını girin: ")
    kb.link = input("Yorum atılacak gönderinin linkini giriniz: ")
    kb.sayi = int(input("Kaç adet yorum atılmasını istiyorsanız o miktarı girin (Girilen miktarda yorum gelmeyecektir. Bunun nedeni siteden kaynaklıdır. Bazı hesaplar engel yemiştir.): "))
    print("Başarılı şekilde yönlendirilmiştir.")
    comment.Browser("https://chrome.google.com/webstore/detail/zenmate-free-vpn%E2%80%93best-vpn/fdcgdnkidjaadafnichfpabhfomcebme?hl=tr")
    time.sleep(2)

elif choose == 3:
    print("Takipçi botu çalışıyor")
    kb.nickname = input("Lütfen bot atılacak sisteme girebilmek için bir fake hesabınızın kullanıcı adını girin: ")
    kb.sifre = input("Lütfen bot atılacak sisteme girebilmek için bir fake hesabınızın kullanıcı adını girin: ")
    kb.takip = input("Takip atılacak hesabın nickini giriniz: ")
    kb.sayi = int(input("Kaç adet takipçi atılmasını istiyorsanız o miktarı girin (Girilen miktarda takipçi gelmeyecektir. Bunun nedeni siteden kaynaklıdır. Bazı hesaplar beğeni engeli yemiştir fakat onları da beğeni atmış saymaktadır.): "))
    print("Hesaba başarılı şekilde girilmiştir.")
    follow.Browser("https://chrome.google.com/webstore/detail/zenmate-free-vpn%E2%80%93best-vpn/fdcgdnkidjaadafnichfpabhfomcebme?hl=tr")
    time.sleep(2)

elif choose == 4:
    print("Kaydetme botu çalışıyor")
    kb.nickname = input("Lütfen bot atılacak sisteme girebilmek için bir fake hesabınızın kullanıcı adını girin: ")
    kb.sifre = input("Lütfen bot atılacak sisteme girebilmek için bir fake hesabınızın kullanıcı adını girin: ")
    kb.link = input("Kaydetme atılacak gönderinin linkini yazın: ")
    kb.sayi = int(input("Kaç adet kaydetme atılmasını istiyorsanız o miktarı girin (Girilen miktarda kaydetme gelmeyecektir. Bunun nedeni siteden kaynaklıdır. Bazı hesaplar engel yemiştir.): "))
    print("Başarılı şekilde yönlendirilmiştir.")
    save.Browser("https://chrome.google.com/webstore/detail/zenmate-free-vpn%E2%80%93best-vpn/fdcgdnkidjaadafnichfpabhfomcebme?hl=tr")
    time.sleep(2)

elif choose == 5:
    print("Video izleme botu çalışıyor")
    kb.nickname = input("Lütfen bot atılacak sisteme girebilmek için bir fake hesabınızın kullanıcı adını girin: ")
    kb.sifre = input("Lütfen bot atılacak sisteme girebilmek için bir fake hesabınızın kullanıcı adını girin: ")
    kb.link = input("İzlenme atılacak gönderinin linkini yazın: ")
    kb.sayi = int(input("Kaç adet izlenme atılmasını istiyorsanız o miktarı girin (Girilen miktarda izlenme gelmeyecektir. Bunun nedeni siteden kaynaklıdır. Bazı hesaplar engel yemiştir.): "))
    print("Başarılı şekilde yönlendirilmiştir.")
    watch.Browser("https://chrome.google.com/webstore/detail/zenmate-free-vpn%E2%80%93best-vpn/fdcgdnkidjaadafnichfpabhfomcebme?hl=tr")
    time.sleep(2)

elif choose == 6:
    print("Geri takip botu çalışıyor")
    kb.nickname = input("Lütfen botu çalıştırabilmek için hesabınızın kullanıcı adını giriniz: ")
    kb.sifre = input("Lütfen botu çalıştırabilmek için hesabınızın şifresini giriniz: ")
    print("Başarılı şekilde yönlendirilmiştir.")
    back.Browser("https://www.instagram.com/")
    time.sleep(2)