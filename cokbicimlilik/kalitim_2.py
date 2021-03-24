import time

class Arac():
    def yon_degistir(self, yon, durum):
        pass
        # Bu fonksiyonun içeriği alt sınıfta override edilerek hazırlanacaktır.
        # Bu sayede hangi sınıfın nesnesinden çağrılırsa o sınıftaki yon_degistir() metodu çalışacaktır.
        # Yani dondur() metodu TekkerlekliAraç() sınıfından oluşturulan nesne tarafından
        # çağrılırsa TekerlekliAraç() sınıfının yon_degistir() metodu;
        # PaletliArac() sınıfından oluşturulan nesne tarafından çağrılırsa, PaletliArac()
        # sınıfındaki metod çalıştırılacaktır.
        # Bu tanımlama şekline POLYMORPHISM - ÇOK BİÇİMLİLİK denilmektedir.
        # Polymorhism ile ;
            # Bütün sınıflarda aynı isimde var olan metod, her alt sınıfta farklı kodlar ile 
            # çalıştırılabilmektedir. Yani yon_degistir() metodunun kodları her sınıfta farklıdır.

            # Alt sınıflara ait olan özel metotlara süper sınıflar üzerinden çalıştırılabilmektedir.
            # Yani alt sınıflara ait olan arac_kontrol() ve on_teker_dondur() metotlarına, 
            # süper sınıfta - Arac() sınıfı - bulunan dondur() metodu üzerinden erişmiş olduk. 

    def dondur(self, yon):
        self.yon_degistir(yon, "Basla")
        time.sleep(0.25)
        self.yon_degistir(yon, "Dur")


class PaletliArac(Arac):
    def arac_kontrol(self, yon, durum):
        print("Paletli araç ", yon, durum)

    def yon_degistir(self, yon, durum):
        self.arac_kontrol("sol", "Basla")

class TekerlekliArac(Arac):
    def on_teker_dondur(self,yon, durum):
        print("Tekerlekli araç ", yon, durum)

    def yon_degistir(self, yon, durum):
        self.on_teker_dondur(yon, durum)


t_arac = TekerlekliArac()
t_arac.dondur("sağ") 
# Üst satırdaki kod aşağıdaki çıktıyı verir.
# Tekerlekli araç  sağ Basla
# Tekerlekli araç  sağ Dur

p_arac = PaletliArac()
p_arac.dondur("sol")
# Üst satırdaki kod aşağıdaki çıktıyı verir.
# Paletli araç  sol Basla
# Paletli araç  sol Basla