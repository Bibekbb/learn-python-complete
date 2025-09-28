class Employee:
    Companyame = "Asus"
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02

    def ShowDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.Companyame} is {self.raise_amount}")


emp1 = Employee("Bibek")
emp1.raise_amount = 0.5
emp1.Companyame = "Apple"
# Employee.ShowDetails(emp1)
emp1.ShowDetails()
emp2 = Employee("Bibek-bb")
emp2.ShowDetails()
