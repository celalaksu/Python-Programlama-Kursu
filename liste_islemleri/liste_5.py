sayilar = []

while True:
    sayi = input("Sayıyı girin (Çıkmak için Ç'ye basın):")
    
    if sayi == "Ç":
        break

    sayi = int(sayi)

    sayilar.append(sayi)

print(sayilar)