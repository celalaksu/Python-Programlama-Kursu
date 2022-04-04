# fonk. kullanacğı verileri fonksiyona gönderebiliriz

# parametreli fonksiyonlar
# toplama(5,6)

# a = 5
# print("merhaba",a)

# fonsiyona kaç tane veri gönderceğim? - cevap : 3
# gönderilecek veri sayısı kadar, fonk. tanımlanmasında parametre olmalıdır.
# 3 tane parametre - fonk_adi(parametre1,parametre2,.......)
def toplama(sayi1,sayi2):
    sonuc = sayi1 + sayi2
    print(f"işlemin sonucu {sonuc}'tur")

print("birinci kullanım")
toplama(45,65)

print("ikinci kullanım")
a = 23
b = 34
toplama(a,b)
# fonks. parametre sayısı kadar veri göndermeniz gerekir.
print("üçüncü kullanım")
# toplama(a)
# toplama()

def toplama2(sayi1:int, sayi2:int):
    sonuc = sayi1 + sayi2
    print(f"işlemin sonucu {sonuc}'tur")

toplama2(54, 65)
toplama2("merhaba","python")
toplama2()
