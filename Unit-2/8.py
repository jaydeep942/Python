# Write programs to demonstrate the use of Positional
# Argument, keyword argument , default arguments , variable
# length arguments

# Positional Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice", 30)

# Keyword Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=25, name="Bob")

# Default Arguments
def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

greet("Charlie")
greet("David", 22)

# Variable Length Arguments
def greet(*names):
    for name in names:
        print(f"Hello {name}")

greet("Eve", "Frank", "Grace")
