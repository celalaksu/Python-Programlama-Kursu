import time

class Arac():
    def yon_degistir(self, yon, durum):
        pass

    def dondur(self, yon):
        self.yon_degistir(yon, "Basla")
        time.sleep(0.25)
        self.yon_degistir("sol", "Dur")


class PaletliArac(Arac):
    def arac_kontrol(yon, durum):
        pass

    def yon_degistir( yon, durum):
        self.arac_kontrol("sol", "Basla")

class TekerlekliArac(Arac):
    def on_teker_dondur(yon, durum):
        pass

    def yon_degistir(self, yon, durum):
        self.on_teker_dondur("sol", "Basla")

