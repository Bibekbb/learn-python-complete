# Object ma kk xa tyo herna use hunxa kk xa herna use hunxa

x = (1,2,3)
dir(x)
print(dir(x))
print(x.__add__)

#Dict

class Person:
    def __init__(self, name , age):
        self.name =  name
        self.age = age
        self.version = 1

p = Person("Bibek",21)
print(p.__dict__)
print(help(Person))