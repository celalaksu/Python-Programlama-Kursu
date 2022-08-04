row = ["EL" for i in range(8)]

print(row)

row_1 = []

for i in range(8):
    row_1.append("EL")

print(row_1)

# liste_adı = [<döngüde çalışacak kod> for <ted> in <ced> <koşul-diğer_işlem>]

kare = [ i*i for i in range(8)]
print(kare)

tek_sayilar= []
for i in range(10):
    if (i%2 == 1):
        tek_sayilar.append(i)

print(tek_sayilar)

ts= [ i for i in range(10) if (i%2==1)]

print(ts)



