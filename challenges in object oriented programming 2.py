class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+' ('+self.meaning+')'
flash = []
print("Welcome to flashcard application")
while(True):
    word = input("Enter the name you want to ad to flashcard: ")
    meaning = input("Enter the meaning of the word: ")
    flash.append(flashcard(word, meaning))
    option = int(input("Press 1 to add more words or 0 to exit: "))
    if(option):
        break
print("\nYour flashcards")
for i in flash:
    print(">", i)
