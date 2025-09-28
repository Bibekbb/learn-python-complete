class person:

    def __init__(self, n, o):
        print("Hello Bibek is smart boy")
        self.name = n 
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("Bibek" ,"Developer")
b = person("Musu", "Accountant")
# print(a.name)
a.info()
b.info()