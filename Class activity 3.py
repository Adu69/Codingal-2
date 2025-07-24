class Parrot:
    species = 'bird'
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Woo is a {}".format(woo.species))
print("Blu is also a {}".format(blu.species))
print()
print("{} is {} yrs old".format(blu.name, blu.age))
print("{} is {} yrs old".format(woo.name, woo.age))
