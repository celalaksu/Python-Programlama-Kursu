a = input("Birinci sayıyı gir :")
a = int(a)
b = input("İkinci sayıyı gir :")
b = int(b)
c = input("Üçüncü sayıyı gir: ")
c = int(c)

if a > b :
    print(a, b, "den büyüktür")
elif b > a :
    print( b, a, "dan büyüktür.")
elif c > a :
    print( c, a, "dan büyüktür")
else:
    print("Tüm koşullar false çıktı.")

