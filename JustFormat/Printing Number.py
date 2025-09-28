class Dog:
    species = ["Bhote Kukur"]

    def _init_(self,n,c):
        self.name =n
        self.state ="Sleeping"
        self.color = c
    def command(self, x):
        if x == self.name:
            self.bark(2)
        elif x == "sit":
            self.state = "sit"
        else:
            self.state  = "wag tail"
    def bark(self , freq):
        for i in range(freq):
            print(self.name +":Woof!")

bello = Dog("Bello","Black")
alice = Dog("alice","white")

print(bello.color)
print(alice.color)

