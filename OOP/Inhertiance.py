class Employee:
    def __init__ (self, name, id):
        self.name = name
        self.id = id

    def ShowDetails(self):
        print(f"The name of Employee : {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(slef):
        print("The deafault language is Python")

e1= Employee("Bibek BB", 1)
e1.ShowDetails()
e2 = Programmer("Mousam BB", 5)
e2.ShowDetails()
e2.showLanguage()

# Types of Inheritance:
# 1. Single
# 2. Multiple
# 3. Multilevel
# 4. Hierarchical
# 5. Hybrid