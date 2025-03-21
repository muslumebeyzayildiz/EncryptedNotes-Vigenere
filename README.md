Bu uygulama, kullanıcının yazdığı notları bir başlık ve bir master key (anahtar) yardımıyla Vigenère şifreleme algoritması kullanarak şifreler, bir .txt dosyasına kaydeder ve daha sonra aynı başlık ve anahtarla deşifre ederek tekrar okunabilir hale getirir.
🚀 Uygulamanın İşleyişi
1. 📥 Not Ekleme ve Şifreleme
Kullanıcı:

Bir başlık (title) girer.
Şifrelemek istediği gizli notunu (secret text) yazar.
Bir adet master key (string) girer.
Şifreleme işlemi:

Uygulama, not içeriğini ve anahtarı alır.
Türkçe karakterlere uygun olarak özelleştirilmiş Vigenère şifreleme algoritması uygulanır.
Şifrelenmiş metin, girilen başlıkla birlikte mysecret.txt dosyasının içine şu formatta eklenir:
pgsql
Kopyala
Düzenle
TITLE: Not Başlığı
ENCRYPTED: ŞifrelenmişVeriBurada
-----
Not: Her kayıt alt alta eklenir. Eski veriler silinmez.

2. 📤 Notu Deşifre Etme
Kullanıcı:

Daha önce girdiği başlığı tekrar girer.
Aynı master key’i yeniden girer.
Deşifreleme işlemi:

Uygulama mysecret.txt dosyasını satır satır okur.
Girilen başlıkla eşleşen bir kayıt bulur.
Eşleşme durumunda, ilgili şifreli metin alınır.
Aynı Vigenère algoritması bu kez deşifreleme (çözme) modunda çalışır.
Kullanıcıya şifresiz orijinal metin ekranda gösterilir.
🔤 Vigenère Algoritması Nasıl Çalışıyor?
Şifreleme:
Her harf, master key’deki bir harf ile kaydırılır. Örneğin:

m harfi ve anahtardaki karşılığı k ise, m alfabede 12., k ise 10. sırada.
Yeni harf: (12 + 10) % alfabe_uzunluğu ile bulunur.
Bu projede Türkçe karakter içeren özel bir alfabe kullanılır:
'abcçdefgğhıijklmnoöprsştuüvyz'

Deşifreleme:
Aynı şekilde, şifreli harften anahtar harfinin pozisyonu çıkarılır:

(şifre_index - anahtar_index) % alfabe_uzunluğu
Bu sayede yalnızca doğru anahtarla şifre çözülebilir.

💾 Kayıt Formatı
Tüm şifreli notlar, proje klasöründe mysecret.txt dosyasına şu şekilde yazılır:

markdown
Kopyala
Düzenle
TITLE: Not Başlığı 1
ENCRYPTED: gçşaföğd...
-----
TITLE: Not Başlığı 2
ENCRYPTED: öüçıjlk...
-----
Dosya "append" (ekle) modunda çalıştığı için her yeni not eskiler silinmeden eklenir.
