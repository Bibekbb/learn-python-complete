#One class to make another class is called single inheritance

class Animal:
    def __init__(self, name , species) -> None:
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed) -> None:
        Animal.__init__(self, name,species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Bella")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()