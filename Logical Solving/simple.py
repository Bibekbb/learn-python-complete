class Student:
    def __init__(self,fname,lname,age,address) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age
        self.address = address

class Employee(Student):
    def __init__(self, noman) -> None:
        self.noman = noman


bimal = Student('Bimal','Rai',21,'ltp')
Rohan = Employee('Rohan')
print(NameError)
