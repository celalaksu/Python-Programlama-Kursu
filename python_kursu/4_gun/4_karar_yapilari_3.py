# Alışveriş site 100 tl üzeri kargo bedava
alisveris_miktari = int(input("Ne kadarlık alışveriş yaptınız? : "))
kargo_bedeli = 20

# Kullanıcıya toplam ödeme miktarını söyleyeceğiz.

if (alisveris_miktari >= 100):
    print(f"Kargonuz bedavadır. Toplamda {alisveris_miktari} TL kadar ödeme yapacaksınız.")
    print()
    print()
else:
    toplam_bedel = alisveris_miktari + kargo_bedeli
    print(f"Kargo bedeli {kargo_bedeli} TL kadardır.")
    print(f"Toplamda {toplam_bedel} TL kadar ödeme yapacaksınız.")


