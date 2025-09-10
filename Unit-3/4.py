# Write a program to use class method to handle the
# Common features of all the instance of Student class.

class Student:
    college_name = "Government BCA College" 
    
    def __init__(self, name, age):
        self.name = name       # instance variable
        self.age = age         # instance variable

    # Class method to handle common feature
    @classmethod
    def set_college_name(cls, new_name):
        cls.college_name = new_name

    @classmethod
    def get_college_name(cls):
        return cls.college_name

    # Instance method to display student info
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, School: {Student.college_name}")


# Create student objects
s1 = Student("Rahul", 18)
s2 = Student("Priya", 19)

print("Before changing school name:")
s1.display()
s2.display()

# Change common feature (college name) using class method
Student.set_college_name("K.K shashtri Government College")

print("\nAfter changing college name:")
s1.display()
s2.display()

# Access college name using class method
print("\nCollege Name (via class method):", Student.get_college_name())

