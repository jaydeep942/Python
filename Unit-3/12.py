# Write a program to overload the addition operator (+) to make
# it act on the class objects.

# Class for complex numbers (just for example)
class StudentMarks:
    def __init__(self, marks1, marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    # Overloading the + operator
    def __add__(self, other):
        return StudentMarks(self.marks1 + other.marks1,
                            self.marks2 + other.marks2)

    # To print object values nicely
    def __str__(self):
        return f"Marks1: {self.marks1}, Marks2: {self.marks2}"


# Main Program
s1 = StudentMarks(40, 50)
s2 = StudentMarks(60, 70)

print("Student 1:", s1)
print("Student 2:", s2)

# Using overloaded +
s3 = s1 + s2
print("Total Marks (after + overloading):", s3)
