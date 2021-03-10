def deneme():
    global a
    a = 20  # global değişken     
    print("fonksiyondan: ",a)

a = 5
deneme()
print("programdan ", a)
