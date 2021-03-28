# kütüphaneleri çağırıyoruz
from cs50 import get_string
from sys import argv


def main():
    # biplenecek sözcükleri bir değişkene
    # bizim yazdığımız bir fonksiyon yardımıyla alıyoruz
    bleepers = get_bleepers()

    # Kullanıcıdan biplenecek mesajı alıyoruz
    message = get_message("What message would you like to censor?\n")

    # Mesajın biplenmiş halini konsola basmak için
    # yazdığımız fonksiyonu kullanııyoruz
    print(censor_msg(message, bleepers))


# Get bleepers, bip'lenecek kelimeleri aldığımız fonksiyon
def get_bleepers():
    # Kodumuzun sadece bir adet girdi ile
    # çalıştırıldığını kontrol ediyoruz, eğer öyleyse
    if len(argv) == 2:
        # Boş bir bip seti oluşturuyoruz
        bleepers = set()
        # Girdi olarak alınan dosyayı okuma modunda açıyoruz
        file = open(argv[1], "r")
        for line in file:
            # Dosyadaki sözcükleri bip setine ekliyoruz
            bleepers.add(line.rstrip("\n"))
        file.close()
        return bleepers
    # Hatalı kod çalıştırmasında doğrusunu gösteriyoruz
    else:
        print("Usage: python bleep.py dictionary")
        exit(1)


# Kullanıcıdan mesaj alıyoruz
def get_message(prompt):
    return get_string(prompt)


# Mesajı kontrol eder ve biplenecek mesajları bipler
def censor_msg(msg, bleepers):
    # Geri döndüreceğimiz mesajı string olarak oluşturuyoruz
    censored_msg = ""
    # Gelen mesajı kelimelere ayırıyoruz
    words = msg.split(" ")
    for word in words:
        # Büyük-küçük harf duyarsız işlem yapmak istediğimiz için
        # lower() kullanarak kelimelerin hepsini küçük harfli yapıyoruz
        if word.lower() in bleepers:
            # eğer kelimemiz, biplenecekler listesindeyse
            # her karakteri * ile değiştirip stringimize ekliyoruz
            censored_msg += ("*" * len(word)) + " "
        else:
            # Biplenmeyecek ise, değiştirmeden ekliyoruz
            censored_msg += word + " "
    # Mesajın sol halini geri döndürüyoruz
    return censored_msg

main()
