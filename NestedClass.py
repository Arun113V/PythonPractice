class Zoo:

    def __init__(self):
        self.animals = []


    def add_animal(self,name,species):
        animal = self.Animal(name,species)
        self.animals.append(animal)

    class Animal:
        def __init__(self,name,species):
            self.name = name
            self.species = species

        def display_info(self):
            print(f"Name:{self.name} and species: {self.species}")


my_zoo = Zoo()
my_zoo.add_animal("Human","Mammal")
my_zoo.add_animal("Eagle","Bird")
my_zoo.add_animal("Crocodile","Reptile")

for animal in my_zoo.animals:
    animal.display_info()