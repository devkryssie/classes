'''
class human:
    def __init__(self,sounds):
        self.sounds = sounds
    def sound(self):
        return self.sounds
class animal:
    def __init__(self,sounds):
        self.sounds = sounds
    def sound(self):
        return self.sounds
def car:
    def __init__(self,sounds):
        self.sounds = sounds
    def sound(self):
        return self.sounds
person = human("sing")
ani = animal("crying")
benz = car("horn")
for x in [person, ani,benz]:
    print(x.sound())
'''
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  #def move(self):
    #print("Move!")

class Car(Vehicle):
  def move(self):
    print("move")

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")  
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")    

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()


