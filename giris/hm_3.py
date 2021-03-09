print("Hangi işlem?")
print("""1- Toplama
2- Çıkarma
3- Çarpma
4- Bölme
Seçim için sıra nosunu yazınız : 
""")

secim = input()

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
elif secim == "3":
    c = a / b
    print("Bölme sonucu :", c)
elif secim == "4":
    c = a * b
    print("Çarpma sonucu :", c)
else:
    print("Yanlış seçim yaptınız.")

