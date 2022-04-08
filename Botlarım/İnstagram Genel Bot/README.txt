
Merhaba ben Oğuz Taşdemir;

Bu algoritmamda birden fazla fonksiyonu olan İnstagram botu kodladım. Botumuz instagram hesabımıza geri takip yapan hesapları bulup onlara takip atabiliyor, aracı siteler sayesinde yorum - beğeni - takip - video izleme - gönderi kaydetme gibi işlevleri yapabiliyor. Tüm yazılım main.py üzerinden yürütülmektedir. Algoritmamızı çalıştırmak için main.py'deki yönergeleri takip etmelisiniz.

Öncelikle sizlere back.py içerisindeki çalışma prensibini precode olarak göstermek istiyorum. Main.py kısmından çalıştırabilirsiniz.

#precode
1- sanal bilgisayar açılır
2- instagrama giriş yapar
3- instagram hesabına giriş yapar
4- profile giriş yapar
5- eğer kullanıcının fotoğrafı varsa son paylaşılan fotoğrafa tıklar, fotoğrafı beğenenlerin listesini açar ve rastgele birinin profiline gider
6- eğer kullanıcının fotoğrafı yoksa takipçi listesini açar ve rastgele bir takipçisine takip atar
7- girilen kullanıcının takipçi - takip ettiği kişi sayısı karşılaştırması yapılır. 
8- takip edilen kişi sayısı, takipçiden fazlaysa o kullanıcıya takip atılır ve takip edilen kişi sayısı (kod içerisinde a adlı değişken) 1 arttırılır 
9- Eğer kullanıcıyı önceden takip ediyorsak bir şey yapmaz.
10- Eğer takipçi sayısı, takip edilen kişi sayısından fazlaysa bir şey yapmaz.
11- Hesap gizli mi değil mi karşılaştırması yapılır. Bunun nedeni profildeki takipçilere erişebilmektir.
12- Eğer profil gizliyse googledeki 1 önceki sayfaya giriş yaparak başka bir kullanıcının profiline girilir ve 8. adımdan itibaren olay tekrarlanır.
13- Eğer kullanıcının profili gizli değilse 8. adımdan itibaren tekrarlanır.
14- Eğer bot başlatıldığından beri 100 kişiye takip atılmışsa işlem tamamlanmış demektir. Bot ve sanal bilgisayar kendisini kapatır.


Ekstra Notlar:
- "back.py" hariç tüm botlara vpn ekleme kısmı ekledim çünkü geri kalan tüm siteler instagram dışı sitelerden çalışmaktadır ve bu sitelere her DNS ayarı girmemektedir. DNS ayarı düzgün olanlar VPN'i algoritma üzerinden kaldırıp kullanabilirler.

- "back.py" hariç diğer tüm botları kullanırken fake hesap kullanmanızı öneririm, aksi taktirde hesaplarınız çalınabilir. Bu çalınma işlemi bizim tarafımızdan olmamaktadır, kullandığımız bot siteleri tarafından çalınma ihtimali vardır.

- İnstagram içerisindeki XPATH ve classlar sürekli olarak güncelleniyordur. Eğer bot hata verirse XPATH ve classları güncellemeyi unutmayın.

Herhangi bir sorun çıkarsa veya bir yardıma ihtiyacınız olursa bana instagram üzerinden ulaşabilirsiniz. İnstagram adresim: @oguz_tasdemir