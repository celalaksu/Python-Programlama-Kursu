sinif_listesi = ["ugur", "hasan", "buse", "celal"]

print(len(sinif_listesi)) # listedeki eleman sayısı

for index in range(len(sinif_listesi)):
    
    sinif_listesi[index] = sinif_listesi[index].capitalize()

print(sinif_listesi)