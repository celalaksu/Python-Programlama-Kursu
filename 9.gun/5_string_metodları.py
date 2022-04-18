
metin = "Pyhton" # -> 0.....5 index
print(type(metin))

# str index

print(metin[0])

print(metin[2:4])

# str - immutabel - değiştirilemez.

# del metin[2] # hata verir

print(len(metin)) # uzunluğu verir.
print(ord("R")) # karakterin sayılsal karşılığını
print(chr(82)) # sayısal değerin karakter karşılığnı verir. ( Unicode )

# in ve not in

print("p" in metin) # p harfi metin değişkeninde varmı

print("p" not in metin) # p harfi metin değişkeninde yok mu?

metin.isdigit()
metin.isalpha()

metin.index("P")

# listeye dönüştürme
metin_liste = list(metin)
print(metin_liste)

# eleman değiştir
metin_liste[5] = "N"
print(metin_liste)

# listeyi tekrar metne dönüştür
yeni_metin = "".join(metin_liste)
print(yeni_metin)

yeni_metin_2 = "-".join(metin_liste)
print(yeni_metin_2)

print("aaabbcccccc".count("ab")) # metin için başka bir metni saydırabilirsiniz.

print("a,b,c".split(",")) # verilen metinleri listeye çevirir.

print(metin.split(","))

print("merhaba python kodlama".split(" ")) # boşluğa göre bölme işlemi yap - liste halinde kelimeleri verir.

print(metin+metin)
print(metin*5)


