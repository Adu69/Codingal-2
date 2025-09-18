class Reverse:
    def __init__(self, s=""):
        self.s = s

    def get_reversed(self):
        return self.s[::-1]

word = input("Enter a word: ")
rev = Reverse(word)
print("Reversed string:", rev.get_reversed())