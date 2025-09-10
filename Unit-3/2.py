# Write a program to demonstrate the use of instance and class/static variables

class Employee:
    # Class/Static variable (shared by all objects)
    company_name = "ABC Pvt Ltd"

    def __init__(self, name, salary):
        # Instance variables (unique to each object)
        self.name = name
        self.salary = salary


# Create objects of Employee
emp1 = Employee("Rahul", 50000)
emp2 = Employee("Priya", 60000)

# Access instance variables
print("Instance Variables:")
print(f"{emp1.name} has salary {emp1.salary}")
print(f"{emp2.name} has salary {emp2.salary}")

# Access class variable
print("\nClass/Static Variable:")
print(f"Company Name (from emp1): {emp1.company_name}")
print(f"Company Name (from emp2): {emp2.company_name}")

# Modify class variable
Employee.company_name = "XYZ Technologies"

print("\nAfter modifying class variable:")
print(f"Company Name (from emp1): {emp1.company_name}")
print(f"Company Name (from emp2): {emp2.company_name}")

# Modify instance variable for emp1
emp1.salary = 55000
emp2.salary = 65000

print("\nAfter modifying emp1's salary:")
print(f"{emp1.name} has salary {emp1.salary}")
print(f"{emp2.name} has salary {emp2.salary}")

