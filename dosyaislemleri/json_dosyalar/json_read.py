import json

with open("json_dosyalar\\veri2.json","rt") as dosya:
    veri = json.load(dosya)
    print("Veri dosyadan okundu.")

print(type(veri))
print(veri)