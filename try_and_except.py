'''
try:
    value = float(input("enter a number:"))
    print(f"solu {10/value}")
except:
    print("oops something went wrong")
'''
#dictionary
student_grade = {"alice":85, "bob": 92, "charlie": 78}
name = input("enter student name:")
try:
    grade = student_grade[name]
    print(f"{name}'s grade is {grade}")
except KeyError:
    print("key error")
except ValueError:
    print("value error")
#list
fruits = ["apple", "banana", "cherry", "date"]
print(f"available fruits: {fruits}")
try:
    position = int(input("enter position to get fruits"))
    print(f"you got {fruits[position]}")
except IndexError:
    print("index out of range")
except ValueError:
    print("invalid literal most be an integer")
#numbers seperated by commas
user_input = input("enter numbers separated by commas:")
numbers = user_input.split(",")
total = 0
try:
    for num in numbers:
        total += int(num)
    print(f"sum of all numbers {total}")
except ValueError:
    print("invalid literal most be an integer")
except ZeroDivisionError:
    print("number must be any number except zero")
except Exception:
    print("opps! something went wrong")
