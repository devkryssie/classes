'''
def vowels(text):
    vowels = 'aeiou'
    count = 0
    for i in text.lower():
        if i in vowels:
            count += 1
    return count
print(vowels('python is fun'))

def list_num(numbers):
    new_list = []
    for n in numbers:
         if n % 2 == 0:
             new_list.append(n)
    return new_list
print(list_num([1,2,3,4,5,6]))
    
def create_email(email):
    email_name = f"{email}@gmail.com"
    print(email_name)
create_email("jerry")
'''
def get_name():
    return [1,2,3,4,5]
  
def get_num():
    return [1,2,3,4,5]
    
def calculate_numbers():
    num1 = get_name()
    num2 = get_num()
    return sum(num1) + sum(num2)
print(calculate_numbers())
def calc(operator *numbers):
    if operator == "+":
        return sum(numbers)
can we combine default parameter values with kwargs?
what happens if we pass positional argument to a parameter in kwargs

    
