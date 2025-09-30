'''
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 5:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
'''
class count:   
    def __init__(self, direction):
        self.direction = direction

    def __iter__(self):

        if self.direction == "up":
            self.current = 1
        else:  
            self.current = 5
        return self

    def __next__(self):
        if self.direction == "up":
            if self.current > 5:
                raise StopIteration
            num = self.current
            self.current += 1
            return num
        else:  
            if self.current < 1:
                raise StopIteration
                num = self.current
                self.current -= 1
            return num
for n in count("up"):
    print(n)
#for n in count("down"):
#    print(n)
