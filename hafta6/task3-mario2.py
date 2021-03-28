import cs50

# biz bozana kadar devam edecek bir loop oluşturuyourz
while True:

    # cs50 kütüphanesinden yaralrlanarak
    # kullanıcıdan bir integer değeri alıyoruz
    satir = cs50.get_int("Yükseklik: ")

    # eğer kullanıcı sınırlarımızın dışında bir yükseklik seçerse
    # loopun başına tekrar dönüp soruyu yineliyoruz
    if satir <= 0 or satir > 23:
        continue

    # eğer istenilen sınırlarda ise
    else:
        # satır sayısı kadar tekrar eden bir loop oluşturuyoruz
        for i in range(satir):
            #ilk mario'da kullandığımız şekilde ilk basamakları oluşturuyoruz
            print(' '*(satir-i-1) + '#'*(1*i+1),end="")
            #ek olarak bir boşluk ve basamakların ikinci kısmını basıyoruz
            print(' ','#'*(1*i+1))

        #loopun dışına çıkabiliriz, işlem tamamlandı!
        break

