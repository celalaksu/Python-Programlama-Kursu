# scope(kapsam) - global ve local değişkenler
# def scope_test():
#     x = 123 # yerel - local değişken

# scope_test()
# print(x) hata verir

def fonksiyon():
    print("Dışarda tanımlanan değişken", degisken)

degisken = 34 # global değişken

fonksiyon()

print(degisken)