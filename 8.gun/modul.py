
def toplama(a,b):
    print(a+b)

def fonk_1(metin):
    print("Bu fonk_1 dir.")
    return metin + metin

# modül kendi çalışınca __name__ değ. değeri __main__
# modül çağrıldığı yerden çalıştırılırsa __name__ değ. değeri dosya adı olur.

if __name__ == "__main__":
    print("Modül sayfası çalıştırıldı.")
    # modüldeki kodları test etmek için kullan.
    toplama(3,4)
    print("Ben modülüm")
    print(__name__)
