# ornek_sinif
# ornekSinif

class Kalem():
    # renk = "Mavi"
    sinif_adi = "Pencil"

    def __init__(self,renk):
        self.rengi = renk # nesne için değişken-özellik-property tanımlaması
        print("Yapıcı-constructor metod çalıştı.")

    # metod
    def yazdir(self):
        print("Bu kalemin işi yazı yazmaktır.")