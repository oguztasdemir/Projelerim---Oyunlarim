Merhaba bu botu kodlama nedenim Gardrops uygulamasında kullanıcılara takip atarak geri takip etmelerini ummaktır.

Bu botun çalışma prensibini anlatmadan önce dosyaları kullanma nedenime gelince Gardrops sitesinin yazılımsal bir eksiği bulunmaktadır. Bir kişinin takipçileri sayfasına geldikten sonra sayfayı aşağı kaydırdıktan sonra gelen yeni kullanıcıları takip ettiğimizi varsayalım ve ardından o kişinin takipçiler kısmına tekrar gelelim. Bu kısımda kullanıcıyı takip etmediğimiz şeklinde gösterecektir fakat o takip etmek istediğimiz kişinin profiline girdiğimizde kişiyi takip ettiğimizi göreceğiz.

Gardrops hesabınıza girer. (Robot doğrulamayı 15 saniye içinde sizin geçmeniz gerekmektedir, aksi taktirde kodu kapatıp tekrar açmanız gerekir.)

"kullanıcı.py" kısmında, "user" olarak belirttiğiniz kişinin takipçilerine erişim sağlar ve burada takip etmediğiniz kullanıcıları not defterine kaydetmeye başlar.

Ne kadar kişiyi kontrol etmek istiyorsanız "while a < 3000:" adlı satırdaki 3000'i değiştirmeniz gerekmektedir. (a'yı 3030'dan fazla yapmamanızı öneririm çünkü yapmanız bir işe yaramayacaktır. Bunun nedeni Gardrops aynı anda en fazla 3030 kullanıcıya erişmenize izin vermektedir. Kalan kullanıcılar gözükmemektedir.)

Kullanıcıları "gardrops_tur.txt" içerisine kaydettikten sonra "gardrops_total.txt" ile karşılaştırma yapar. Bu karşılaştırma sonucunda "gardrops_tur.txt" içerisindeki kullanıcılardan "gardrops_total.txt" içerisinde bulunmayanları "gardrops_takip.txt" içerisine not eder. Bu not etme işlemi bittikten sonra "gardrops_takip.txt" içerisindeki tüm kullanıcıların profillerine sırasıyla giriş yaparak "Takip Et" butonu bulduklarına takip eder ve aynı zamanda profillerine erişilen kullanıcıları "gardrops_total.txt" dosyasının içine yükler.


