class User:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    def login(self, email, password):
        return self.email == email and self.password == password


class Student(User):
    def __init__(self, name: str, email: str, password: str):
        super().__init__(name, email, password)
        self.enrolled_courses = []
        self.assessment_results = {}

    def enroll(self, course):
        self.enrolled_courses.append(course)
        course.students.append(self)

    def view_courses(self):
        return f"The list of enrolled courses: {[course.title for course in self.enrolled_courses]}"

    def take_assessment(self, assessment):
        print(f"\nAssessment: {assessment.course.title}")
        score = assessment.administer()
        self.assessment_results[assessment.course.title] = score
        print(f"Score: {score}")
        return score


class Instructor(User):
    def __init__(self, name: str, email: str, password: str):
        super().__init__(name, email, password)
        self.courses_created = []

    def create_course(self, title, description):
        course = Course(title, description, self)
        self.courses_created.append(course)
        return course

    def create_assessment(self, course, questions):
        assessment = Assessment(course, questions)
        course.assessments.append(assessment)
        return assessment


class Course:
    def __init__(self, title, description, instructor):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.materials = []
        self.students = []
        self.assessments = []

    def add_material(self, material):
        self.materials.append(material)


class Assessment:
    def __init__(self, course, questions):
        self.course = course
        self.questions = questions

    def administer(self):
        score = 0
        for question, correct_answer in self.questions.items():
            print(f"\n{question}")
            answer = input("Answer: ").strip()
            if answer.lower() == correct_answer.lower():
                score += 1
        return score


class E_LearningSystem:
    def __init__(self):
        self.students = []
        self.instructors = []
        self.courses = []

    def register_student(self, name, email, password):
        student = Student(name, email, password)
        self.students.append(student)
        return student

    def register_instructor(self, name, email, password):
        instructor = Instructor(name, email, password)
        self.instructors.append(instructor)
        return instructor

    def find_user(self, email, password):
        for user in self.students + self.instructors:
            if user.login(email, password):
                return user


system = E_LearningSystem()

instructor = system.register_instructor("Alice", "alice@example.com", "pass123")
student = system.register_student("Bob", "bob@example.com", "pass456")

course = instructor.create_course("Python Basics", "Learn Python from scratch")
system.courses.append(course)

course.add_material("Intro to Python - PDF")

questions = {
    "What is the keyword to define a function in Python?": "def",
    "What data type is the result of: 5 / 2 in Python 3?": "float"
}
assessment = instructor.create_assessment(course, questions)

student.enroll(course)

print(student.view_courses())
