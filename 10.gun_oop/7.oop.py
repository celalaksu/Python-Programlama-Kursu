class deneme:
    x="bir deneme yazılımıdır bu"
    def __init__(self, yas):
        if type(yas)==int or type(yas)==float:
            self.yas=yas
        elif type(yas)==str:
            if yas.isnumeric()==True:
                self.yas=int(yas)
            else:
                self.yas=None
        else:
            self.yas=None
nesne=deneme("5")
print(nesne.yas)
print(type(nesne.yas))