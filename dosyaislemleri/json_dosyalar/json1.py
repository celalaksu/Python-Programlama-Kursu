import json

veri = {
    "ders": [{
        "adi": "Python",
        "kurum": "Arhavi Hem"
    }]
}

print(type(veri))

json_str = json.dumps(veri)
print(type(json_str))
print(json_str)

json_str2 = json.dumps(veri, indent=4)
print(type(json_str2))
print(json_str2)

with open("json_dosyalar\\veri3.json","wt", encoding="utf-8") as dosya:
    json.dump(veri, dosya, indent=4)
    print("Veri dosyaya yazıldı.")

