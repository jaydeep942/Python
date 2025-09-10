#  Write a program to check the object type to know
# whether the method exists in the object or not.

class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name} is studying.")


class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(f"{self.name} is teaching.")


# Function to check if method exists in the object
def check_method(obj, method_name):
    if hasattr(obj, method_name):
        print(f"Yes, '{method_name}' method exists in {obj.__class__.__name__}.")
    else:
        print(f"No, '{method_name}' method does NOT exist in {obj.__class__.__name__}.")


# Main Program
s1 = Student("Rahul")
t1 = Teacher("Manoj")

check_method(s1, "study")    
check_method(s1, "teach")   
check_method(t1, "teach")    
check_method(t1, "study")    
