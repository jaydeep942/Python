# Create a program to display memory locations of two variables using id() function, and then use identity operators two compare whether two objects are same or not

a = int(input("Enter an integer value for a: "))
b = int(input("Enter an integer value for b: "))

# Display memory locations using id()
print("Memory location of a:", id(a))
print("Memory location of b:", id(b))

# Compare if both variables refer to the same object using identity operator
if a is b:
    print("a and b refer to the SAME object.")
else:
    print("a and b refer to DIFFERENT objects.")
