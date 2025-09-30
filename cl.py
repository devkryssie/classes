import random
guess = input("guess correct num")
secret = random.randint(1, 10)
if guess == secret:
    print("u guessed correctly:")
else:
   print("wrong number:")
user = input("enter email:")
if "@" in user:
    print("email correct:")
else:
    print("invalid email")

