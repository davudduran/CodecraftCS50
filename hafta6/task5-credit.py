# kütüphaneleri çağırıyoruz
from cs50 import get_int
from math import floor

def main():
    # kullanacağımız değişkenleri tanımlyoruz
    digit1 = 0
    digit2 = 0
    num_digits = 0
    sum_of_double_odds = 0
    sum_of_evens = 0
    # kullanıcıdan girdi alıyoruz
    cc_number = get_int("Number: ")

    # Numaranın sonundan başlayarak tek ve
    # çift sayıları bulup hepsini toplar
    while cc_number > 0:
        #son 2 basamağı değişkenlere alır
        digit2 = digit1
        digit1 = cc_number % 10

        # eğer çift basamaklardan birisindeysek
        # çift basamakların toplamı değişkenine
        # bu değeri ekle
        if num_digits % 2 == 0:
            sum_of_evens += digit1

        # tek basamaklardan birisindeysek,
        # o basamak değerini iki ile çarparız.
        # en sonunda ortaya çıkan sayıların
        # tüm basamaklarını toplarız.
        else:
            multiple = 2 * digit1
            sum_of_double_odds += (multiple // 10) + (multiple % 10)

        # son basamağı siler ve
        # basamak sayısı değişkenini arttırır
        cc_number //= 10
        num_digits += 1

    # kart numarasının doğruluğunun kontrol değerini ve
    # ilk 2 basamak değerini ayrı değişkenlere atıyoruz
    is_valid = (sum_of_evens + sum_of_double_odds) % 10 == 0
    first_two_digits = (digit1 * 10) + digit2

    # Kart'ların diziliş kurallarına göre
    # hangi kart olduğuna karar verip onu print edeceğiz
    if digit1 == 4 and num_digits >= 13 and num_digits <= 16 and is_valid:
        print("VISA\n")
    elif first_two_digits >= 51 and first_two_digits <= 55 and num_digits == 16 and is_valid:
        print("MASTERCARD\n")
    elif (first_two_digits == 34 or first_two_digits == 37) and num_digits == 15 and is_valid:
        print("AMEX\n")

    # Bildiğimiz bir kurala uymuyorsa INVALID basacağız
    else:
        print("INVALID\n")


main()