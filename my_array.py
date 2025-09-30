class Array:
    def __init__(self):
        self.fruits = []
    def append(self, fruits):
        self.fruits += [fruits]

    def insert(self, i, fruits):
        self.fruits = self.fruits[:i] + [fruits] + self.fruits[i:]
    def pop(self):
        fruit = self.fruits[-1]
        self.fruits = self.fruits[:-1]
        return fruit

    def remove(self, i):
        fruit = self.fruits[i]
        self.fruits = self.fruits[:i] + self.fruits[i+1:]
        return fruit

