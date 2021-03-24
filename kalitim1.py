class Level1:

    variable_1 = 100

    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


# class Level2(Level1):

class Level2():
    variable_2 = 200

    def __init__(self):
        super().__init__()
        self.var_2 = 201
    
    def fun_2(self):
        return 202


# class Level3(Level2):
class Level3(Level1, Level2):

    variable_3 = 300

    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302

nesne = Level3()

print(nesne.var_1)
