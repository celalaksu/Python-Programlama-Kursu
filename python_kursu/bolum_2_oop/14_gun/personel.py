# çalışan, yöneticiler, birimler, muhasebe, pazarlama, üretim

class kisi:
    kurum = "Bizim Yeni Limited Şirketi"
    def __init__(self):
        self.ad = None
        self.soyad = None

    def mesai_saati():
        print("Gelme saati 8 dir.")

    def gorev_yap(self):
        print(f"{self.ad} görevini yapıyor.")

class yonetici(kisi):
    gorev = "Yönetici"
    def __init__(self):
        super().__init__()

class calisan(kisi):
    gorev = "Çalışan"
    def __init__(self):
        super().__init__()
        


class freelancer(kisi):
    gorev = "Freelancer"
    def __init__(self):
        super().__init__()
        
