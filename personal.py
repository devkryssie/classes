
#v = word[::-1]
#print(v) 
def vowels(text):
    vowels = 'aeiou'
    count = 0
    for i in text.lower():
        if i in vowels:
            count +=1
    return count
print(vowels("aeiou"))               
def even(n):
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'        
print(even(5))  
def sum_list(numbers):
    count = 0
    for num in numbers:
        count += num
    return count
print(sum_list([1,2,3,4]))
def fizzbuzz(n):
    if n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    elif n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
print(fizzbuzz(5))

def multiply_table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")
multiply_table(5)
def star_pattern(rows):
    for i in range(1, rows + 1):
        print("*" * i)
star_pattern(5)
def is_palindrome(s):
    if s == s[::-1]:
        print(f"{s} is palindrome")
    else:
        print(f"{s} is not palindrome")
is_palindrome("radar")
is_palindrome("python")
