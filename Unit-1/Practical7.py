# Write a program to create a byte type array, read, modify, and display the elements of the array
from array import array

# Create a byte type array ('B' is for unsigned char, values 0-255)
byte_array = array('B', [10, 20, 30, 40, 50])

print("Original array:")
for value in byte_array:
    print(value, end=" ")
print()

# Modify elements
byte_array[1] = 25   # Change 20 → 25
byte_array[3] = 45   # Change 40 → 45

print("Modified array:")
for value in byte_array:
    print(value, end=" ")
print()

# Reading individual element
index = 2
print(f"Element at index {index}:", byte_array[index])
