
try:
    x = int(input("Sayı girin"))
    y = 1/x
    print(y)
except ZeroDivisionError:
    print("0 bölmeye çalışıyorsun.")
except ValueError as hata:
    print("Sayısal bir değer girin.", hata)
except Exception as istisna:
    print("Sorun oluştu.", istisna)

# İlk önce en özel hata kontrol edilir. En sonda genel hata kontrolü yapılır.

# yanlış hata yakalama
# try:
#     x = int(input("Sayı girin"))
#     y = 1/x
#     print(y)
# except :
#     print("0 bölmeye çalışıyorsun.")
# except ValueError:
#     print("Sayısal bir değer girin.")
# except ZeroDivisionError:
#     print("Sorun oluştu.")