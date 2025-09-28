# defined in class

class Employee:
    def __init__(self,name):
        self.name = name

        pass
    name = "Bibek"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i

e = Employee("Bibek")
print(e.name)
print(len(e))