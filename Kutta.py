class Dog:
    animal = "Dog"  # class variable

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    def display(self):
        print(f"Animal: {Dog.animal}, Breed: {self.breed}, Colour: {self.colour}")

dog1 = Dog("Labrador", "Golden")
dog2 = Dog("Beagle", "Brown")

dog1.display()