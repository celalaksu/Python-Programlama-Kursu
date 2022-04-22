
class OrnekSinif: # Object sınıfının özelliklerini otomatik bu sınıfa aktarır
    __ders__ = "Python" # gizli öğe
    konu = "oop"

    # nesne özelliklleri
    def __init__(self,derssayisi:int):
    
        if derssayisi < 13:
            self.drssys = derssayisi
        else:
            self.drssys = None
        
nesne1 = OrnekSinif(23)
# print(nesne1.drssys)
# nesne2 = OrnekSinif(5)
# print(nesne2.drssys)

# print(nesne1.__ders__)

# otomatik eklenen öğeler - sınıfa
print("Sınıfa kendiliğinden eklenen öğeler")
print("__module__",OrnekSinif.__module__)
print("__module__",nesne1.__module__)
print("__name__",OrnekSinif.__name__)
print("__dict__",OrnekSinif.__dict__)
print("__dict__",nesne1.__dict__)
print("__str__",OrnekSinif.__str__)
print("__str__",nesne1.__str__)

        

