
sayilar_listesi = []
while True:
    sayi = input("Sayı gir :")
    if sayi.isdigit():
        sayi = int(sayi)
    else:
        continue
    sayilar_listesi.append(sayi)
    devam = input("Çıkış için 'ç' ye basınız.")
    if devam == "ç":
        break

print(sayilar_listesi)