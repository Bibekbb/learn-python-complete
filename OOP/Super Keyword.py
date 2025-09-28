# Child class to call parents class to use super keyword

# class ParentClsss:
#     def parent_method(self):
#         print("This is parent Method")


# class ChildClass(ParentClsss):
#     def parent_method(self):
#         print("Bibek")
#         super().parent_method()
#     def child_method(self):
#         print("This is child method")
#         super().parent_method()


# Child_object = ChildClass()
# Child_object.child_method()
# Child_object.parent_method()

# class employee:
#     def __init__(self,name ,id):
#         self.name = name
#         self.id = id

# class programer(employee):
#     def __init__(self,name, id , lang):
#         self.lang = lang
#         super().__init__(name,id)

# Bibek = employee("Bibek bb", 500)
# babe = programer("Sanu maya",1000, "Python")
# print(babe.name)


# class Employee:
#     def __init__(self, name, id) -> None:
#         self.name = name
#         self.id = id

# class Programmer(Employee):
#     def __init__(self, name, id, lang) -> None:
#         self.lang = lang
#         super().__init__(name, id)

# Bibek = Employee("Bibek BB", 101)
# Mousam = Programmer("Mousam Don", 20, "Python")
# print(Mousam.name)


class Employee:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self, name, id, lang) -> None:
        self.lang = lang
        super().__init__(name, id)


Bibek = Programmer("Bibek BB", 10)
Bibe = Employee("Bibekbb", 20, "Python")

print(Bibek.name)
