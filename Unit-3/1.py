# Write a program to create a Student class with a constructor
# having more than one parameter . Also create a method named
# display() to view the student details. 

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

# Creating an instance of Student
student1 = Student("Alice", 20, "A")
student1.display()
print('=================')
print(student1.display())
