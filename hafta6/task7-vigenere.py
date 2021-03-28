# kütüphaneleri çağır
import sys
from cs50 import get_string

def main():
    # Girdi kontrolü ve anahtar kontrolü için
    # validate_key fonksiyonunu çağırıyoruz
    key = validate_key()

    # kullanıcıdan girdi istiyoruz ve bu girdiyi
    # şifrelemek üzere encrypt fonksiyonuna gönderiyoruz
    plaintext = get_string("plaintext: ")
    encrypted = encrypt(plaintext, key)

    # Sonucu konsola print ediyoruz!
    print('Encrypting "' + plaintext + '" with a keyword of "' + key + '," using Vigenère’s cipher, yields the ciphertext "' + encrypted + '."')

def validate_key():
    # Programın doğru çalıştırıldığını kontrol eder
    # yanlış çalıştıırldıysa doğrusunu gösterir
    if len(sys.argv) != 2:
        print("Incorrect usage. Usage: python vigenere <key>")
        sys.exit(0)

    # Şifre anahtarının doğruluğunu kontrol eder
    # yanlış çalıştıırldıysa doğrusunu gösterir
    if not (sys.argv[1]).isalpha:
        print("Invalid key. Use only alphabetical characters.")
        sys.exit(0)
    else:
        return sys.argv[1]

def encrypt(plaintext, key):
    # sonra kullanmak üzere
    # birkaç değişken oluşturuyoruz!
    output = ''
    key_len = len(key)
    letter_counter = 0

    # yazıdaki her bir karakter için tekrarlanacak bir döngü oluşturuyoruz
    for c in plaintext:
        # alfabetik karakter değilse doğrudan şifreye ekle
        if not c.isalpha() or c.isspace():
            output += c

        # alfabetik karakter ise
        else:
            # Büyük harf karakteri şifrele ve
            # eğer karakterimiz küçük harf ise, büyük harf karşılığına bakılır
            if c.isupper():
                # kelimemizi anahtarın içinde buluyoruz
                cipher_char = key[letter_counter % key_len].upper()
                cipher_char_ascii = ord(cipher_char.upper()) if cipher_char.islower() else ord(cipher_char)
                output += chr(((ord(c) - ord('A')) + (cipher_char_ascii - ord('A'))) % 26 + ord('A'))

            # Küçük harf karakterimizi şifreleyip
            # küçük harf karşılığına bakacağız, eğer karakterimiz büyük harf ise
            else:
                cipher_char = key[letter_counter % key_len]
                cipher_char_ascii = ord(cipher_char.lower()) if cipher_char.isupper() else ord(cipher_char)
                output += chr(((ord(c) - ord('a')) + (cipher_char_ascii - ord('a'))) % 26 + ord('a'))

            # şifredeki karakter sıramızı bir sonraki karaktere ilerletiyoruz
            letter_counter += 1

    return output

main()
