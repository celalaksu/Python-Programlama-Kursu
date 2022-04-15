# parametre  olarak;
# *args -> birden fazla sıralı değişken fonk. gönderilebilir. args -> zorunlu, genel kullanım.
# *args -> veri türü tuple - demet
# **kwargs -> birden fazla key-value değeri gönderilebilir.

def toplama(*prt):
    print(prt)

toplama(1,2,3,4,5)
a = 4
b = 9
c = 10
toplama(a,b,c)


def fonksiyon2(**kwargs):
    print(kwargs)

fonksiyon2(dil="python",konu="moduller")

def fonk_3(*args, **kwargs):
    print(args)
    print(kwargs)

fonk_3(a,b,c,dil="python",konu="moduller")