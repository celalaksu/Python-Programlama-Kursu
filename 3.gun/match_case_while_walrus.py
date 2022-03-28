
while ((secim := input("Hangi işlemi yapmak istiyorsunuz ? : ( 1-Toplama, 2-Çıkarma, 3-Çarpma, 4-Bölme, 5-Çıkış) ")) != "5") :

    a = input("Birinci sayıyı gir :")
    a = int(a)
    b = input("İkinci sayıyı gir :")
    b = int(b)

    match secim:
        case "1":
            sonuc  = a+b
            print(sonuc)
        case "2":
            sonuc = a - b
            print(sonuc)
        case "3":
            sonuc = a * b
            print(sonuc)
        case "4":
            sonuc = a // b
            print(sonuc)
        case _:
            print(" Yanlış seçim yaptınız.")