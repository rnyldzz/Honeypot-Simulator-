# Honeypot Simülatörü

Bu proje, siber saldırganların davranışlarını gözlemlemek ve analiz etmek amacıyla Python ile geliştirilmiş basit, düşük etkileşimli bir honeypot simülatörüdür. 
Belirlenen portları (örneğin, FTP, SSH) dinleyerek gelen bağlantı denemelerini yakalar ve saldırganın IP adresi, port bilgisi ile denediği kullanıcı adı/parola gibi verileri loglar.



# Özellikler

    Çoklu Port Desteği: Aynı anda birden fazla portu dinleyerek farklı hizmetleri taklit eder.

    Düşük Etkileşim: Saldırgana sadece bir karşılama mesajı gönderir ve daha fazla etkileşime izin vermez, bu sayede risk en aza indirilir.

    Detaylı Loglama: Bağlantı kurulan IP adresi, port numarası ve saldırganın gönderdiği veriler honeypot_logs.txt dosyasına kaydedilir.

    Kolay Kurulum: Dış kütüphanelere bağımlılığı azdır ve standart Python 3 ile çalışır.

# Nasıl Çalışır?

Proje, temel Python socket kütüphanesini kullanarak belirli portlarda ağ bağlantılarını dinlemeye başlar. Her bağlantı talebi geldiğinde, threading modülü ile yeni bir iş parçacığı oluşturulur. 
Bu iş parçacığı, saldırgana sahte bir hizmetin karşılama mesajını gönderir ve saldırganın ilettiği ilk veri bloğunu (genellikle kullanıcı adı ve parola) yakalar. Yakalanan tüm bilgiler, tarih ve saat damgasıyla birlikte bir log dosyasına yazılır.



# Kurulum ve Çalıştırma

Bu projeyi çalıştırabilmek için Python 3'e ihtiyacınız vardır. Proje, 1024'ten küçük portları dinleyeceği için sudo yetkisi gerektirir.

    Projeyi Klonlayın:
    Bash

git clone https://github.com/KULLANICI_ADINIZ/PROJE_ADINIZ.git
cd PROJE_ADINIZ

Projeyi Başlatın:
Bash

    sudo python3 honeypot.py

    

# Log Dosyası Analizi

Proje çalıştırıldıktan sonra, tüm saldırı denemeleri honeypot_logs.txt adlı dosyaya kaydedilir. Bu dosyayı bir metin düzenleyiciyle açarak saldırganların hangi IP adreslerinden geldiğini, hangi portları hedeflediklerini ve 
hangi kullanıcı adı/parola kombinasyonlarını denediklerini görebilirsiniz.


# Sorumluluk Reddi

Bu proje yalnızca eğitim ve araştırma amaçlıdır. Gerçek bir ağ ortamında kullanılması, yasal veya güvenlik sorunlarına yol açabilir. Projeyi kendi riskinizde kullanın. Geliştirici, oluşabilecek herhangi bir zarardan sorumlu değildir.























