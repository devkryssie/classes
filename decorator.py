def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def function():
  return "Hello Sally"

print(myfunction())

def addition(add):
    def inner():
        return add()+1
    return inner
@addition
def myadd():
    return 5 
print(myadd())
def changecase(func):
  def myinner(x):
    return func(x)
  return myinner

@changecase
def myfunction(nam):
  return 5def changecase(func):
  def myinner(x):
    return func(x).upper()
   return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))
 

print(myfunction(1))

                     
