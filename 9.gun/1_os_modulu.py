import os # işletim sistemi ve dizinler üzerinde işlem

# print(os.getcwd()) # bulunduğumuz yol

# print(os.system("dir")) # dos komutu "dir"

# print(os.listdir()) # klasörleri liste halinde verir

# os.chdir(".\\9.gun")

# print(os.getcwd()) # bulunduğumuz yol

# # aktif klasördeki klasöreri yazdırır.
# dosyalar = os.listdir()
# for dosya in dosyalar:
#     print(dosya)
os.chdir(".\\9.gun")

for i in os.walk(os.getcwd()):
    print(i)

dosya_yolu, dosya_adı = os.path.split("9.gun\\1_os_modulu.py")
print(dosya_yolu)
print(dosya_adı)

