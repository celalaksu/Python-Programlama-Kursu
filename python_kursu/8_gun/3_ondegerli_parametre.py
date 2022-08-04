# default değerli parametreler ( argumanlar )

def carpma(a,b,c=2):
    sonuc = a*b*c
    return sonuc

# c yerine veri gelmediği zaman c inin değeri 1 kabul edilir.

s1 = carpma([1,2,2],5) # c=2
print(s1)
s2 = carpma(2,3,4) # c = 4
print(s2)

# def carpma(a,b=3,c): HATALI TANIMLAMA
#     sonuc = a*b*c
#     return sonuc

print("============================")
def fonk_2(a="pyth", b = 2, c = [1,2,3]):
    print(a)
    print(b)
    print(c)

fonk_2(b=4, a = "arhem")

fonk_2(4,"dkdk")