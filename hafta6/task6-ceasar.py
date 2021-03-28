# kütüphaneleri çağırıyoruz
from cs50 import get_string
from sys import argv

def main():
    #kullanıcıdan anahtar almak için get_key fonksiyonunu çağırıyoruz
    key = get_key()

    # kullanıcıdan şifrelenecek yazıyı almak için get_plaintext fonksiyonunu çağırıyoruz
    plaintext = get_plaintext("plaintext: ")

    # şifrelenmiş mesajı printliyoruz, şifrelenmiş mesaja ulaşmak için
    # encipher_text fonskiyonunu çağırıyoruz
    print("ciphertext:", encipher_text(plaintext, key))


def get_key():

    # Programın tam olarak 1 girdi ile çalıştırıldığını kontrol et
    # eğer doğru çalıştırıldıysa onu bir integer olarak al
    if len(argv) == 2:
        return int(argv[1])

    # eğer yanlış çalıştırıldıysa, doğrusunu göster.
    else:
        print("Usage: python caesar.py key")
        exit(1)


# kullanıcıdan normal yazıyı bir string olarak al
def get_plaintext(prompt):
    return get_string(prompt)


# Yazıyı şifreler
# Büyük-küçük harf düzenini değiştirmez
# Alfabeden olmayan karakterler aynı kalır
# ord() fonksiyonu bir char(karakter) değeri alır ve ascii(integer) değerini geri döndürür
# chr() fonksiyonu bir ascii değeri(integer olarak) alır ve char değerini döndürür
def encipher_text(text, key):
    # sonra doldurmak üzere boş bir String(yazı) değişkeni oluşturuyoruz.
    str = ""
    for char in text:
        if not char.isalpha():
            # alfabe karakteri değilse doğrudna ekle
            str += char
        if char.isupper():
            # Büyük harf ise, ascii değeri = 65
            str += chr(((ord(char) - 65) + key) % 26 + 65)
        if char.islower():
            # Küçük harf ise, ascii değeri = 97
            str += chr(((ord(char) - 97) + key) % 26 + 97)

    # şifreleme tamamlandı değeri geri döndürüyoruz!
    return str

main()


