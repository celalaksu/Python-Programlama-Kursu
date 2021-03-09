while True:
    print("Hangi işlem?")
    print("""1- Toplama
    2- Çıkarma

    Çıkmak için Ç harfine basınız.
    
    Seçim için sıra nosunu yazınız : 
    """)

    secim = input()

    if secim == "Ç":
        break

    if not (secim == "1" or secim == "2"):
        print("Yanlış giriş yaptın.")
        continue 
    

    sayilar = []

    while True:
        sayi = input("Sayıyı girin (Çıkmak için Ç'ye basın):")
        
        if sayi == "Ç":
            break

        sayi = int(sayi)

        sayilar.append(sayi)

    print(sayilar)

    if secim == "1":
        # toplam = sayilar[0] + sayilar[1]
        toplam = 0
        # [30, 40, 60]
        for sayi in sayilar:
            toplam = toplam + sayi

        print(f"Toplama sonucu : {toplam}")

    elif secim == "2":

        fark = sayilar[0]
        # 1, 2, 3, 4 .....
        for index in range(1,len(sayilar)):
            fark = fark - sayilar[index] 

    else:
        print("Yanlış seçim yaptınız.")

