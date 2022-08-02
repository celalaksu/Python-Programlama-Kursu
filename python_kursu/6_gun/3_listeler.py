# Birden fazla veri tutan değişkenler
# list ( listeler )

# liste_adı = [deger1, deger2,...............................]
# farklı veri türlerini bir arada tutar.
# dinamiktir. otomatik olarak büyüyebilir.
# Array (dizi) - sabit boyutlu - tek tip veri tutarlar ( diğer diller )

sinif_listesi = ["ugur", "hasan", "buse", "celal"]
# 0-ugur
# 1- hasan
# 2 buse
# 3- celal
# 4- hata verir

gunler = [1,2,3,4,5,6,7]

kisi_bilgileri = ["ahmet",27,1988,"Teknisyen"]

bos_liste = []

print(sinif_listesi)
# liste elemanına erişim - index no kullanılır

# index - çoklu veri yapılarında elemanlara verilen sıra numarasıdır.
# gizlidir. İndex 0-sıfır dan başlar

# liste_adı[index_no]

print(sinif_listesi[3])
print(sinif_listesi[0])

# eleman değiştirme

sinif_listesi[3] = "Betül"
print(sinif_listesi)

gecici_veri = sinif_listesi[0]
sinif_listesi[0] = sinif_listesi[1]
sinif_listesi[1] = gecici_veri

print(sinif_listesi)

# eleman silme
del sinif_listesi[1]
print(sinif_listesi)

# metod - ( fonksiyon ) - farklı bir nesne ile kullanıdığı için

# int, str, float, list, fonksiyon --> pythonda herşey nesnedir.
# print(), int()

# sinif_listesi.fonksiyon_adı() fonksiyon-->metod
# nesneler üzerinde farklı işlemler yapılmasını sağlar

sinif_listesi.append("Eray") # listeye eleman ekler sona ekler
sinif_listesi.append("Eray")
print(sinif_listesi)

c_count = sinif_listesi.count("Eray") # elemandan kaç tane var
print(c_count)

# (__value: str, /) -> int " -> int" metodun veri ürettiğini ifade eder
# (__value: str, /) -> kaç tane parametre verilmesi gerektiğini belirtir

sinif_listesi.insert(2,"Furkan")
print(sinif_listesi)

sinif_listesi.pop(0)
print(sinif_listesi)

sinif_listesi.remove("Eray")
print(sinif_listesi)

sinif_listesi.sort()
print(sinif_listesi)

sinif_listesi.reverse()
print(sinif_listesi)

# ters index
print(sinif_listesi[-1])

# parçalama-slice

parca1 = sinif_listesi[1:3]
print(parca1)

parca2 = sinif_listesi[-3:-1]
print(parca2)
