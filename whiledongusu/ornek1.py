tek_sayilar = 0
cift_sayilar = 0

sayi = input("Sayı gir:")
sayi = int(sayi)

while sayi != 0:
    if sayi % 2 == 1:
        tek_sayilar += 1
    else:
        cift_sayilar += 1
    sayi = input("Yeni sayı girin ya da çıkmak için 0 girin.")
    sayi = int(sayi)

print("Tek sayı sayısı :", tek_sayilar)
print("Cift sayı sayısı :", cift_sayilar)