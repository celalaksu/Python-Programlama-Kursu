# veri = bytearray("ş")
veri = bytearray("abcd",encoding="utf-8")
print(veri)
print(veri[1])

print(veri[0])

with open("veri.bin", 'wb') as dosya:
    dosya.write(veri)

veri2 = bytearray("diğer veri", encoding="utf-8")
with open("veri.bin", "rb") as dosya1:
    data = dosya1.readinto(veri2)
    print("Veri eklendi")

print(veri2)