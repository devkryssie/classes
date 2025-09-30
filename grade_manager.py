students = []
def add_student():
    name = input("enter name :")
    score = int(input("enter score:"))
    students.append((name, score))
    print("student added!")
def calculate_average():
    total = 0
    count = 0
    for name,score in students:
        total += score
        count += 1
    if count > 0:
        average = total / count
        print(f"the average score is {average}")
def display_students():
    for name, score in students:
        print(f"{name} {score}")
add_student()
#add_student()
#add_student()
display_students()
calculate_average()
