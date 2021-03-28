# kütüphaneleri çağırıyoruz
from cs50 import get_float
from math import floor

# input için loop oluşturuyoruz
while True:
    # kullanıcıdan girdi alıyoruz
    dollar = get_float("Change Owed: ")

    #işlemlerin doğruluğu için sayımızı 100 ile çarpıp
    # floor yardımıya tam sayıya dönüştürüyoruz
    cent = floor(dollar * 100)

    # kullanıcı istenildiği gibi bir değer girerse
    # loopun dışına çıkıp işlemlere başla!
    if cent > 0:
        break

# çeyreklikleri bulmak için değeri 25'e bölüp
# bölüm sayısını çeyrek değişkenine veriyoruz
ceyrek = cent // 25

# 10 kuruşları bulmak için 25 kuruşlardan kalan değeri
# 10'a böldüğümüzde çıkan sonucu cent10 değişkenine veriyoruz
cent10 = (cent % 25) // 10

# aynı işlemi tekrar 10 kuruşlara da uygulayarak
# kalanı 5 kuruşlara bölerek sonucu cent5 değişkenine veriyoruz
cent5 = ((cent % 25) % 10) // 5

# bütün işlemler sonucunda elimizde kalan tek kuruşları da
# kuruş değişkenine veriyoruz
kurus = ((cent % 25) % 10) % 5

# bütün değerleri ayrı bir değişkene verdiğimize göre
# hepsini toplayıp sonucu konsola basıyoruz!
print(f"{ceyrek + cent10 + cent5 + kurus}")

