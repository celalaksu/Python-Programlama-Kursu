def programlama(konu, dil="Python"):  # değer verilen parametreler sona yazılır.
    print(f"{dil}'da {konu} konusunu işliyoruz.")

programlama("Fonksiyonlar")
programlama("fonksiyonlar", "Rust")

# Fonsiyona parametre gönderilmediği zaman, fonksiyon tanımlanmasındaki değer geçerli olur.
# Önceden tanımlı parametreler, positinal parametrelerden sonra belirtilir.
