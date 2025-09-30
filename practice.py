class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"my name is {self.name} i am {self.age} years old")
s1 = student("john", 20)
s1.show()
class car:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour
    def show(self):
        print(f"the {self.colour} {self.brand} is driving")
c1 = car("lexus", "red")
c1.show()
class phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def call(self, number):
        print(f"calling {number} using {self.brand} {self.model}")
p = phone("samsung", "galaxys21")
p.call("0768575757")


