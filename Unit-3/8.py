# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Subclass 1
class Student(Person):   # Inheriting from Person
    def __init__(self, name, age, student_id):
        super().__init__(name, age)   # call base class constructor
        self.student_id = student_id

    def display_student(self):
        self.display_person()
        print(f"Student ID: {self.student_id}")


# Subclass 2
class Teacher(Person):   # Inheriting from Person
    def __init__(self, name, age, subject):
        super().__init__(name, age)   # call base class constructor
        self.subject = subject

    def display_teacher(self):
        self.display_person()
        print(f"Subject: {self.subject}")


# Main Program
s1 = Student("Rahul", 20, "101")
t1 = Teacher("Manoj", 40, "Computer Science")

print("=== Student Details ===")
s1.display_student()

print("\n=== Teacher Details ===")
t1.display_teacher()
