# One parent class and multiple child class
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")


class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")


class Danceremployee(Dancer, Employee):
    def __init__(self, dance, name):
        self.dance = dance
        self.nmae = name


o = Danceremployee("Bibek", "BB")
print(o.name)
print(o.dance)
o.show()
