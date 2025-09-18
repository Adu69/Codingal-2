import random
class FruitQuiz:
    def __init__(self):
        self.fruits = {
            'Apple': 'red',
            'Banana':'yellow',
            'Orange': 'orange',
            'Grapes': 'green' or 'purple',
            'Pineapple': 'yellow'
        }
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            answer = input("What is the color of {}".format(fruit))
            if (answer.lower() == color):
                print("Correct Answer!")
            else:
                print("Wrong Answer")
            option = int(input("Do you want to continue? Press 1 for Yes and 0 for No"))
            if option == 0:
                break
print("Welcome to the Fruit Color Quiz!")
fq = FruitQuiz()
fq.quiz()