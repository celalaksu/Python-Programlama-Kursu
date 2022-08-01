while True:
    sayi_1 = int(input("Birinci sayıyı girin : "))
    sayi_2 = int(input("İkinci sayıyı girin : "))
    islem = input("Hangi işlemi yapacaksınız.( Toplama - 1, Çarpma -2, Çıkarma - 3, Bölme -4 giriniz ):")

    if (islem == "1"):
        islem_yazili = "Toplama"
        sonuc = sayi_1 + sayi_2
    if (islem == "4"):
        islem_yazili = "Bölme"
        sonuc = sayi_1 // sayi_2
    print(sonuc)
    print(f"{islem_yazili} işleminin sonucu {sonuc} dur.")

    secim = input("Devam mı? (H/h) ")
    if (secim == "H" or secim =="h"):
        break