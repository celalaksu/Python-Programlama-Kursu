# kalıtım - inheritance - Bir sınıfın özelliklerini başka sınıfa aktarma işlemi

# öğrenci - görev - yaptığı iş - kurallar
# öğretmen - branşı - görev
# yönetici - yönetim- öğretmen - meslek

# ortak bilgiler
# kurum - her kişi için aynıdır
# ad - soyad - her kişi için değişen

class SuperSinif: # Super sınıf - base class
    def __init__(self, isim) -> None:
        self.isim = isim
        self.durum = None

    def ust_sinif_metodu(self):
        print("Ust sinıf metodu çalıştı", self.__class__)

class AltSinif(SuperSinif): # sub class - alt sınıf - alt sınıflar daha ayrıntılı - gelişmiş
    def __init__(self, isim) -> None:
        super().__init__(isim)

    def alt_sinifa_aitmetod(self):
        print("Alt sınıf metodu çalıştı.")


class BirAltSinif(AltSinif):
    def __init__(self, isim) -> None:
        super().__init__(isim)

nesne2 = SuperSinif("supersinif")
print(nesne2.isim)
nesne2.ust_sinif_metodu()

nesne1 = AltSinif("altsinif")
print(nesne1.isim)
nesne1.durum = "Aktif"
nesne1.ust_sinif_metodu()

nesne3 = BirAltSinif("biraltsini")

nesne3.alt_sinifa_aitmetod()