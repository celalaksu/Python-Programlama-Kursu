while ((secim := input("Hangi işlemi yapmak istiyorsunuz ? : ( 1-Toplama, 2-Çıkarma, 3-Çarpma, 4-Bölme, 5-Çıkış) ")) != "5") :

    sayilar = []
    while (sayi:=input("Sayıyı giriniz (Çıkış için 'ç/Ç' ye basınız!) ->")):
        if (sayi == "ç") or (sayi == "Ç"):
            break

        if sayi.isnumeric()==False:
            print("DİKKAT -> Girdiğiniz sayı GEÇERSİZDİR! TEKRAR GİRİNİZ..!")
            continue

        sayi = int(sayi)
        sayilar.append(sayi)

    sonuc = 0
    match secim:
        case "1":
            for i in sayilar:
                sonuc = sonuc + i            
        case "2":
            for i in sayilar:
                sonuc = sonuc - i  
        case "3":
            sonuc = 1
            for i in sayilar:
                sonuc = sonuc * i  
        case "4":
            b_sonuc=sayilar[0]
            for i in range(len(sayilar)-1):
                b_sonuc = b_sonuc / sayilar[i+1]
            sonuc = b_sonuc 
        case "5":
            break 
        case _:
            print(" Yanlış seçim yaptınız.")
    
    print(f"İşlemin sonucu = {sonuc}")
