# kullanacağımız kütüphaneleri "import" komutuyla çağırıyoruz
import cs50

# biz bozana kadar devam edecek bir loop oluşturuyourz
while True:

    # cs50 kütüphanesinden yaralrlanarak kullanıcıdan bir integer değeri alıyoruz
    satir = cs50.get_int("Yukseklik: ")

    # eğer kullanıcı sınırlarımızın dışında bir yükseklik seçerse
    # loopun başına tekrar dönüp soruyu yineliyoruz
    if satir <= 0 or satir > 23:
        continue

    # eğer istenilen sınırlarda ise
    else:
        # satır değişkeninin uzunluğunda bir for loopu oluşturuyoruz
        for i in range(satir):

            # (satır-i-1) tane boşluk ve (1*i+1) tane # basıyoruz
            print(' '*(satir-i-1) + '#'*(1*i+1))

        #loopun dışına çıkabiliriz, işlem tamamlandı!
        break
    
    