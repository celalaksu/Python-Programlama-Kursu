print(""" 1- Toplama
2 - Çıkarma
3- Çarpma
4 - Bölme
5 - Çıkış
""")


a = input("Birinci sayıyı gir :")
a = int(a)
b = input("İkinci sayıyı gir :")
b = int(b)

secim = input("Hangi işlemi yapmak istiyorsunuz ? : ( 1, 2, 3, 4, 5) ")

if secim == "1":
    sonuc  = a+b
    print(sonuc)
elif secim == "2":
    sonuc = a - b
    print(sonuc)
elif secim == "3":
    sonuc = a * b
    print(sonuc)
elif secim == "4":
    sonuc = a // b
    print(sonuc)
elif secim == "5":
    pass
else:
    print(" Yanlış seçim yaptınız.")