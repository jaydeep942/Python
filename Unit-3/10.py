# Write a program to understand the order of execution of methods in several base classes 
# according to method resolution order (MRO)

# Base Class A
class A:
    def display(self):
        print("Method from Class A")

# Base Class B
class B(A):
    def display(self):
        print("Method from Class B")

# Base Class C
class C(A):
    def display(self):
        print("Method from Class C")

# Derived Class (inherits from B and C)
class D(B, C):
    pass


# Main Program
d1 = D()
d1.display()   # Which display() will run?

# Print Method Resolution Order
print("\nMRO of Class D:")
print(D.mro())
