from ornek_sinif import Kalem

kalem1 = Kalem("Mavi")
print(kalem1.rengi)
print(kalem1.sinif_adi)

# sınıfta olmayan özelliğin nesneye tanımlanması
kalem1.tur = "tükenmez"
print(kalem1.tur)

kalem2 = Kalem("Kırmızı")
print(kalem2.rengi)
print(kalem2.sinif_adi)

print(Kalem.sinif_adi)

kalem3 = Kalem("Sarı")
print(kalem3.rengi)
print(kalem3.sinif_adi)

kalem1.yazdir()

print("Nesnenin varlıkları")
print(kalem1.__dict__)
print(kalem2.__dict__)

print()
print("======================")
print("sınıfın varlıkları")
print(Kalem.__dict__)




