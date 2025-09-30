def list_num(numbers):
    new_list = []
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)
    return new_list
print(list_num([1,2,3,4,5,6]))
def squared(numbers):
    new = []
    for n in numbers:
            new.append(n**2)
    return new
print(squared([2,3,4]))
def is_palindrome(text):
    reverse = ""
    for i in text:
        reverse = i + reverse
    return text == reverse
print(is_palindrome("madam"))
def rem_duplicate(items):
    new = []
    for i in items:
        if i not in new:
            new.append(i)
    return new
print(rem_duplicate([1,1,2,2,3,4,4,4]))
def password(password):
    has_letter = False
    has_number = False
    has_specials = False
    specials = "!@#$%^&*()_+=-"

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True
        elif char in specials:
            has_specials = True
    if len(password) >= 8 and has_letter and has_number and has_specials:
        return "strong"
    elif len(password) >= 6 and has_letter and has_number:
        return "medium"
    else:
        return "weak"
print(password("pass123@#"))
    
