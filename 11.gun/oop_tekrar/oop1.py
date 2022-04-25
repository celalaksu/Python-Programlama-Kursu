# sınıf
# nesne

liste = [1,2,3,4]
liste1 = list([1,2,3,4,5])

# list -> sınıf
# liste -> nesne
# kullanacağımız yapı nasıl olmalıdır. veri nasıl olmaldır.
# nesne tasarlamak . tekrar tekrar kullanmamız.
# sınıf -> tasarladığımız nesne nin yapısını oluştur. nesnenin taslağı, şablonu
# yazılan sınıf tekrar tekrar, verileiri fonksiyonları birarada topluyorsunuz.

class Kisi:
    kurum = "MEB" # sınıfın özelliği - class property
    # üretilen nesnede ortak olacak olan özellik
    # yapıcı metod - contructor
    # gizli bir metod - nesne oluşunca çalışır-otomatik - nesne oluşunca gerçeleşmesini istediğimiz
    # kodlar yaz.

    # BİRİNCİ KULLANIM
    # def __init__(self) -> None:
    #     print("Yapıcı metod çalıştı")
    #     # nesne oluşturulunca çalışmasını istediğiniz - yapılmasını istediğiniz kodlar.
    #     # ilklendirme

    # İKİNCİ KULLANIM
    def __init__(self,ad, soyad) -> None:
        self.ad = ad # gelen verileri alıp, tanımlanan nesneye atadık.
        self.soyad = soyad
        # ad ve soyad değişkenlerine - nesnenin özellikleri - object( instance - ornek ) property
        self.sinif = None
        # self -> otomatik olarak çağıran nesne parametre ollarak gönderilir.

    # nesnenin metodu
    def toplama_yap(self,a,b): # metod
        print("İşlemin sonucu ",a+b)

    #sınıfa ait olan metot
    @classmethod
    def sinif_metodu(cls): # cls -> sınıfı tutan
        print("Sınıf metodu çalıştı.", cls.kurum)
        

    # static metod
    @staticmethod
    def statik_metod(a):
        print("Statik metod çalıştırıldı.",a)

    


# BİRİNCİ KULLANIM
# ahmet = Kisi()
# print(ahmet.kurum)
# ayse = Kisi()
# print(ayse.kurum)

# İKİNCİ KULLANIM
ogrenci1 = Kisi("Ahmet", "Aksu") # self -> ogrenci1
ogrenci1.sinif = 11 # self -> ogrenci1
print(ogrenci1.ad," ", ogrenci1.soyad," ",ogrenci1.kurum, " ", ogrenci1.sinif)
ogrenci1.toplama_yap(3,5)
ogrenci1.sinif_metodu()
Kisi.sinif_metodu()

ogrenci2 = Kisi("Ayşe","Aksu") # self -> ogrenci2
ogrenci2.sinif = 9
print(ogrenci2.ad," ", ogrenci2.soyad," ", ogrenci2.kurum," ", ogrenci2.sinif)
ogrenci2.toplama_yap(5,6)
ogrenci2.statik_metod("DATA")
