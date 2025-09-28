# class Employee:
#     def __init__(self):
#         self.__name = "Bibek"

# a = Employee()
# # print(a.__name) #Can not be accessed directly
# print(a._Employee__name) # Can be accessed directly
# print(a.__dir__())


#Protected
class Student:
    def __init__(self):
        self._name = "Bibek"
        
    def _funName(self):
        return "Coder Bibek"

class Subject(Student): 
    pass

obj = Student()
obj1 = Student()
# Calling by object of student class

print(obj._name)
print(obj._funName())

# Calling by object of student of subject class
print(obj1._name)
print(obj1._funName())
