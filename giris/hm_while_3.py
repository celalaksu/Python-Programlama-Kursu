while True:
    print("Hangi işlem?")
    print("""1- Toplama
    2- Çıkarma

    Çıkmak için Ç harfine basınız.
    
    Seçim için sıra nosunu yazınız : 
    """)

    secim = input()

    if not (secim == "1" or secim == "2"):
        print("Yanlış giriş yaptın.")
        continue

    
    
    if secim == "Ç":
        break

    a = input("Birinci sayıyı gir :")
    a = int(a)
    b = input("İkinci sayıyı gir :")
    b = int(b)

    if secim == "1":
        c = a + b
        print("Toplama sonucu :", c)
    elif secim == "2":
        c = a - b
        print("Çıkarma sonucu :", c)
    else:
        print("Yanlış seçim yaptınız.")

