class OrnekSinif:
    ders = "python"

    def __init__(self) -> None:
        self.konu = "oop"

    # ornek metodu -> nesneye ait olan - çağıran nesne parametre olarak gönderilir. nesne 
    # özellikleri üzerinde işlem yapabiliriz.
    # sınıf netodu -> sınıfa ait - sınıf adı ile ulaşılır.çağıran sınıf parametre olarak gönderilir. sınıf 
    # özellikleri üzerinde işlem yapabiliriz.
    # static metd -> normal bir metoddur. metoda sınıf veya nesne gönderilmez.
    # metodlara sınıf ve nesne otomatik gönderilir, biz metoda parametre olarak göndermeyiz.

    
    def nesne_metodu(self,gelenveri):
        print("Bu metod nesneylere ait olacaktır.",gelenveri)
        print(self.konu)

    @classmethod # öğenin yapısını veya görevini ifaden yardımcı değimlerdir. - decorator
    def sinif_metodu(cls):
        print("Bu metod sınıfa ait bir metottur")
        print(cls.ders)
        

    @staticmethod
    def static_metod():
        print("Statik metod çalıştı")
        
if "__name__" == "__main__":

    nesne1 = OrnekSinif()
    nesne1.nesne_metodu("Nesneden gönderilern Veri")
    nesne2 = OrnekSinif()
    nesne2.nesne_metodu("nesne 2 den gönderildi")
    nesne2.sinif_metodu()
    OrnekSinif.sinif_metodu()
    # OrnekSinif.nesne_metodu("Giden veri") # hata oluşur.
    OrnekSinif.nesne_metodu(nesne1,"gidenveri")

    nesne1.static_metod()
    nesne2.static_metod()
    OrnekSinif.static_metod()