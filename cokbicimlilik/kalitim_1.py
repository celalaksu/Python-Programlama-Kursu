import time
# hatalı çalışıyor -- kontrol et
# nesne tanımlayarak dene
class PaletliArac():
    def arac_kontrol(self, yon, durum):
        pass

    def dondur(self, yon):
        self.arac_kontrol("sol", "Basla")
        time.sleep(0.25)
        self.arac_kontrol("sol", "Dur")

class TekerlekliArac():
    def on_teker_dondur(yon, durum):
        pass

    def dondur(self, yon):
        self.on_teker_dondur("sol", "Basla")
        time.sleep(0.25)
        self.on_teker_dondur("sol", "Dur")