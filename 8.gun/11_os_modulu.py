import os

print(os.getcwd()) # bu dosyanın bulunduğu yolu verir.

print(os.system("dir"))# kök klasördeki klasörleri listeler.

print(os.listdir())# kök klasördeki klasörleri liste içinde verir.

# Klasördeki dosya adlarını yazdırma
os.chdir(".\\8.gun") # klasörü değiştirme
dosyalar = os.listdir()
for dosya in dosyalar:
    print(dosya)

os.mkdir("deneme_dizini")

os.rename("deneme_dizini","degismis_dizin")

os.rmdir("degismis_dizin")# içi boş dizini siler

# os.stat("dosya_adı.uzantısı")# dosya hakkında bilgiler verir.

print("Dosya ve dizinler")
# kök dizin, altdizin ve dosyaları gösterir.
for i in os.walk(os.getcwd()):
    print(i)

os.path.exists("\\8.gün")# dizin var mı diye kontrol eder. True ve False değerleri gönderir.

#os.path.isdir("dizin yolu")
#os.path.isfile("dosya yolu")

# Dosya yolu ve dosya adını ayırma
dosya_yolu, dosya_adi = os.path.split("8.gun\\3_modul_ice_aktarma.py")
print(dosya_yolu)
print(dosya_adi)

# Dosya adını ve uzantısını ayırma
print(os.path.splitext(dosya_adi))