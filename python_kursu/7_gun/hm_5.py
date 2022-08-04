while True:

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

    islem = input("Hangi işlemi yapacaksınız.( Toplama - 1, Çarpma -2, Çıkarma - 3, Bölme -4 giriniz ):")

    if (islem == "1"):
        islem_yazili = "Toplama"

        sonuc = 0
        for i in sayilar_listesi:
            sonuc = sonuc + i
    
    if (islem == "4"):
        islem_yazili = "Bölme"

        sonuc = sayilar_listesi[0]
        for i in range(1,len(sayilar_listesi)):
            sonuc = sonuc // sayilar_listesi[i]
        


    print(sonuc)
    print(f"{islem_yazili} işleminin sonucu {sonuc} dur.")

    secim = input("Devam mı? (H/h) ")
    if (secim == "H" or secim =="h"):
        break