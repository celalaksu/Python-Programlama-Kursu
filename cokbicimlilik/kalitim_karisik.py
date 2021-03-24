# composition-kompozisyon
import time

class TekerlekliArac():
    def yon_degistir(self, yon, durum):
        print("Tekerlekli araç ", yon, durum)

class PaletliArac():
    def yon_degistir(self, yon, durum):
        print("Paletli araç ", yon, durum)

class Arac():
    def __init__(self, sinif_kontrol):
        self.sinif_kontrol = sinif_kontrol

    def dondur(self, yon):
        self.sinif_kontrol.yon_degistir(yon, "Başla")
        time.sleep(0.25)
        self.sinif_kontrol.yon_degistir(yon, "Dur")


bmw_m = Arac(TekerlekliArac())
bmw_m.dondur("sol")

p_arac = Arac(PaletliArac())
p_arac.dondur("sağ")