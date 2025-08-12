# Write a program to display sum of two complex numbers

a = float(input("Enter real part of first complex number: "))
b = float(input("Enter imaginary part of first complex number: "))

# Take input from the user for second complex number
c = float(input("Enter real part of second complex number: "))
d = float(input("Enter imaginary part of second complex number: "))

num1 = complex(a, b)
num2 = complex(c, d)

sum_complex = num1 + num2

print(f"Sum of {num1} and {num2} is {sum_complex}")