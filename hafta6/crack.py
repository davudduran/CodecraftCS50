# Kullanılacak kütüphaneleri çağırıyoruz
import sys
from crypt import crypt
import time


def main():

    # Yanlış kullanımı kontrol et, yanlış ise doğrusunu göster
    # ve işlemleri durduruyoruz.
    if len(sys.argv) != 2:
        print('Usage error!')
        print('Syntax: python crack.py hash')
        print('hash is DES-hashed password')
        sys.exit(1)

    # girdi'yi hash değişkenine veriyoruz
    hashed_password = sys.argv[1]

    # ASCII tablosuna göre alfabetik karakterleri
    # liste halinde bir değişkene atıyoruz (0,A,B,...Y,Z,a,b,...,y,z)
    characters = list(range(0, 1)) + list(range(65, 91)) + list(range(97, 123))

    # Guess String'ini sonra kullanmak üzere oluşturuyoruz
    guess = ''

    # 5. Karakter için döngü
    for i in characters:

        # 4. Karakter için döngü
        for j in characters:

            # 3. Karakter için döngü
            for k in characters:

                # 2. Karakter için döngü
                for l in characters:

                    # İlk karakter için string
                    for m in characters:

                        # Tahmin değişkenimizi doldurmaya başlıyoruz
                        guess = guess if i == 0 else guess + chr(i)
                        guess = guess if j == 0 else guess + chr(j)
                        guess = guess if k == 0 else guess + chr(k)
                        guess = guess if l == 0 else guess + chr(l)
                        guess = guess if m == 0 else guess + chr(m)

                        found_match = check_match(hashed_password, guess)

                        if found_match:
                            break

                        # Guess strinigin temizliyoruz
                        guess = ''

                    if found_match:
                        break

                if found_match:
                    break

            if found_match:
                break

        if found_match:
            break

    if found_match:
        print(guess)
    else:
        print('No possible password found. Invalid hash?')
        sys.exit(0)


def check_match(hashed_password, guess):
    # extract salt from hashed_password

    salt = hashed_password[0:2]

    # encrypt guess
    guess_hash = crypt(guess, salt)

    return hashed_password == guess_hash




main()