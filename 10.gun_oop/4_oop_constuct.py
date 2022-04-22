# constructor - yapıcı metot
# gizli olarak bulunan bir yapıdır.
# __init__ metodu otomatik çalışır. Nesne oluşunca 
# self --> sınıftan oluşturulan nesneyi temsil eder.

# class OrnekSinif:
#     ders = "Python"
#     konu = "oop"

#     def __init__(self):
#         print("Yapıcı metod çalıştı.")

# nesne1 = OrnekSinif()
# nesne2 = OrnekSinif()

class OrnekSinif:
    ders = "Python"
    konu = "oop"

    # nesne özelliklleri
    def __init__(self,tarih,derssayisi):
        print("Yapıcı metod çalıştı.")
        self.trh = tarih # buraya gelen veri, üretilen nesneye aittir.
        self.drssys = derssayisi
        self.sinifi:str = ""

nesne1 = OrnekSinif("22.04.2022",10)
nesne1.sinifi = "Öğretmenler"
nesne1.drssys = 12
nesne1.ders = "Java"
print(nesne1.ders)


nesne2 = OrnekSinif("23.04.2022",11)
nesne2.sinifi = "meb"
nesne2.trh = "24.04.2022"
nesne2.ders = "Rust"
print(nesne2.ders)
print(nesne1.ders)

print(nesne1.ders, nesne2.ders)
print("nesne1 in tarihi", nesne1.trh, nesne1.drssys, nesne1.sinifi)
print("nesne2 in tarihi", nesne2.trh, nesne2.drssys, nesne2.sinifi)