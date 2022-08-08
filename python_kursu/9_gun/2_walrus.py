# walrus : 3.10 , hem atama yapar, hem veri döndürür

# = --> atama operatör

c = 5 # RAM e veri kayıt eder

# := --> walrus operatörü
#print(b=34)# hatalı
b=34
print(b)

print(a := 55) # çıktısı 55 olur

print(a)

sayı = int(input("Sayı girin"))

while (sayı) < 10 :
    print(sayı)
    sayı += 1 



while (sayı := int(input("Sayı girin"))) < 10 :
    print(sayı)
    sayı += 1 