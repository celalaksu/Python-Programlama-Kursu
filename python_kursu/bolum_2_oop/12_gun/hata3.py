# try:
#     pass
# except EN ÖZEL:
#     pass
# except:
#     pass
# except GENEL HATA:
#     pass

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")

print("THE END.")

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")
except Exception:
    print("Hata oluştu")


print("THE END.")


# YANLIŞ KULLANIM
try:
    y = 1 / 0
except Exception:# HATA OLDUĞUNDA DİĞER SATIRLAR ÇALIŞMAZ
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Hata oluştu")