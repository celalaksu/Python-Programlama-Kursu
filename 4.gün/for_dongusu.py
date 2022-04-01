# while - koşul True olduğu sürece 
# for döngüsü - bazı elemanlar verilir - her bir eleman üzerinde yapmak istediğimiz işlemleri döngü içinde yazıyoruz
# for dongüsü - kaç eleman - bir yapıda eleman sayısını bilmeye biliriz.

# for <degisken_adı> in <çoklu_değişken> :
#       <değişken_adı> üzerinde yapılacak işlemleri
#       ........
# else: - isteğe bağlı
#   son değer üzerinde işlem yapmak için kullanılır
#   döngü kırıldığında (break) çalışmaz
#       
# çoklu değişken : range(5) - 0 1 2 3 4 5

# <degişken_adı> elemanları ayrı ayrı 

# for sayi in range(5):
#     print(sayi)

# for i in range(2, 10, 2):
#     print(i**2)

for i in range(2, 10, 2):
    print(i**2)
else:
    print("else kısmı çalıştı")