class OrnekSinif():
    __sayac = 0
    ozellik = "sinif özelliği"

    def __init__(self, deger = 1):
        self.__ilk = deger
        self.ulasilan = "Gizli değil"
        OrnekSinif.__sayac += 1

# __ gizli eleman, modülü kullanacak kişiden gizlenir.
# 

ornek_nesne1 = OrnekSinif()
print(ornek_nesne1.ulasilan)

print(ornek_nesne1._OrnekSinif__sayac)
# nesneAdi._SınıfAdi__gizliOgeAdi

# nesne yada sınıfın, öğesi var mı diye kontrol
# eder. True-False değerlerini geri döndürür.
print(hasattr(OrnekSinif,"ozellik"))
print(hasattr(ornek_nesne1,"ulasilan"))
