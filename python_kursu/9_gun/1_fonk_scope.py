from tkinter import Y


x = 123 # bu değişken

def fonk():
    x = 456
    print(x) # bu değişken ile aynı değil farklıdır
    # local değişken olarak adlandırılır

fonk() # ekrana 456
print(x) # 123


