class Employee:
    def __init__(self, name, salary):
        self.salary = salary
        self.name = name

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))


e = Employee("Bibek", 10000)
print(e.name)
print(e.salary)

string = "sanu-12000"
e1 = Employee.fromStr(string)
print(e1.name)
print(e1.salary)
