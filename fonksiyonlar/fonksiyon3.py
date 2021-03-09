# parametrelere başlangıç değeri vermek

def toplama(a=5, b=10, c=15):
    sonuc = a + b + c
    print(sonuc)

toplama(10,20,30) # 60
toplama() # 30
toplama(40,50) # 105, c = 15
toplama(b=40,c=50) # 95 , a = 5
toplama(a=76,c=100) # 176, b = 10

# değeri olan parametreler sona eklenir.
def toplama2(a, c, b=10):
    sonuc = a + b + c
    print(sonuc)

toplama2(5,15)
