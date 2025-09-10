# Write a program to store data into instances using
# mutator methods and to retrieve data from the instances using
# accessor methods

class Student:
    def __init__(self):
        # private instance variables
        self.__name = ""  or  None
        self.__age = 0

    # Mutator methods (setters)
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")

    # Accessor methods (getters)
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


# Create Student object
s1 = Student()

# Store data using mutator methods
s1.set_name("Shashwat")
s1.set_age(20)

# Retrieve data using accessor methods
print("Student Name:", s1.get_name())
print("Student Age:", s1.get_age())
