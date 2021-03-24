# override 

class Left:
    var = "L"
    var_left = "LL"

    def fun(self):
        print("left")
        return "Left"


class Right(Left):
    var = "R"
    var_right = "RR"

    def fun(self):
        super().fun()
        return "Right"


nesne = Right()
print(nesne.fun())
