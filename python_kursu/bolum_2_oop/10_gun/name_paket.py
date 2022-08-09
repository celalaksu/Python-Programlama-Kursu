def fonksiyon():
    print("merhaba paket")
    print(__name__) # çıktısı __main__ dir

# eğer bu dosya modül olarak kullanılmayacaksa
# __name__ değeri kullanılır.



if __name__ == "__main__": # modül olarak çağrılmadığında çalış
    fonksiyon()

# bütün kodların çalışmasını engellemek için kullanılır

# __name__ -> __main_ ise dosyayın kendisi çalışır
# __name__ -> __name_paket__ ise yani dosya adı ile modül olarak çalışır
