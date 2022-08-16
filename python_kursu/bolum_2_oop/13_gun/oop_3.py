
from curses.ascii import isdigit


class Ornek():
    
    def __init__(self,sayi): 
        self.sayi = sayi
        # Nesne ilk oluştuğunda çalışması gereken bütün kodlar
        # başka bir fonk çalış
        # farklı bir kütüphane çalış
        # Kullanılacak verileri KONTROL ETME
        if (isdigit(sayi)):
            self.sayi1 = sayi

       

n1 = Ornek(12) # self = n1
print(n1.a)
print(n1.sayi)

n2 = Ornek(15)
print(n2.a)
print(n2.sayi)