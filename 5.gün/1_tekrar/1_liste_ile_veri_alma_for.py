secim = input("Kaç tane veri gireceksiniz? -> ")
secim = int(secim)

sayilar = []
for i in range(1,secim+1):
    sayi = input(f"{i}. sayıyı giriniz (Çıkış için 'ç/Ç' ye basınız!) -> ")
    
    if (sayi == "ç") or (sayi == "Ç"):
        break
    
    sayi = int(sayi)
    sayilar.append(sayi)

print(sayilar)