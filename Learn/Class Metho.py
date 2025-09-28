# make custom data types

class Employee:
    company = "Google"
    def show(self):
        print(f"The name is {self.name} and Company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "Bibek"
e1.show()
e1.changeCompany("Info Developers")
e1.show()
print(Employee.company)
