liste=[9,5,10,1,4,7,6,8] # list kelimesi pythonda kullanıldığı için ( veri türü adı olarak )
# değişken adı olarak kullanılmaz  o yüzden liste olarak değiştirdim.
list2=[]
kucuk=liste[0]

leng=len(liste)


for j in range(leng):
    for i in range(leng):
        if kucuk > liste[i]:
            kucuk=liste[i]
            liste[0],liste[i]=liste[i],liste[0]

    list2.append(kucuk)
    del liste[0]
    leng=len(liste)
    if len(liste) == 0:
        break
    kucuk=liste[0] # son döngüye kadar liste değişkenindeki bütün veriler silineceği için
    # son döngüde out of index hatası gelir. O yüzden if len(liste)==0 kontrolü ekledim.

print(list2)