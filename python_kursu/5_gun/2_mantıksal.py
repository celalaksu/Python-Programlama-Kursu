# mantıksal operatörler
# ve ( and ), veya ( or ), değil ( not )
# birden fazla koşulu birlikte yazabilmek
# Sonuç True ya da False

5>6 # False

13==55 # False

10 == 10 # True

# ve --> Verilen bütün koşullar gerçekleşmek zorunda # True --> Sonuç True
print(5>6 and 13==55 and 10 == 10)

# veya --> Verilen koşullardan sadece bir tanesnin gerçekleşmesi yeterlidir
# --> 1 True varsa sonuç True

print(5>6 or 13==55 or 10 == 10) # True

# not - tersini alır, True ise False yapar
print(not(not(10==10)))