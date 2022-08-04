sinif_listesi = ["ugur", "hasan", "buse", "celal"]
print(len(sinif_listesi)) # eleman sayısını verir.

# in ( içinde ), not in ( içinde değil)

print("Uğur" in sinif_listesi) # True , False değerini üretir

index_no = 0
for eleman in sinif_listesi: # range(len(sinif_listesi-1))
    print(eleman.capitalize()),
    sinif_listesi[index_no] = eleman.capitalize()
    index_no += 1 # ( index_no = index_no + 1)

print(sinif_listesi)


    
    