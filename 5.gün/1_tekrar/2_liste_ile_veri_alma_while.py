sayilar = []
while (sayi:=input("Sayıyı giriniz (Çıkış için 'ç/Ç' ye basınız!) ->")):
    if (sayi == "ç") or (sayi == "Ç"):
        break

    if sayi.isnumeric()==False:
        print("DİKKAT -> Girdiğiniz sayı GEÇERSİZDİR! TEKRAR GİRİNİZ..!")
        continue

    sayi = int(sayi)
    sayilar.append(sayi)

print(sayilar)

sonuc = 0
for i in sayilar:
    sonuc = sonuc + i

print(f"İşlemin sonucu = {sonuc}")