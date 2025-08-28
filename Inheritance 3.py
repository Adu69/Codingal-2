class Bird:
    def __init__(self):
        print("Bird is ready")
    def WhoisThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Bird is ready")
    def WhoisThis(self):
        print('Penguin')
    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.WhoisThis()
peggy.swim()
peggy.run()
