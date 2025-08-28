class Vehicle:
    def __init__(self):
        capacity = input("Please enter the maximum seating capacity of your bus: ")
        print("Your fare is Rs.", capacity * 10 + (capacity /10))