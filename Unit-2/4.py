# Create a program to search the position of an element in
# an array using index() method of array class.

import array as arr

# Create an integer array
numbers = arr.array('i', [10, 20, 30, 40, 50, 60])

print("Array elements:", numbers.tolist())

# Take input from the user
search_element = int(input("Enter the element to search: "))

try:
    # Find index (position) of element
    position = numbers.index(search_element)
    print(f"Element {search_element} found at position (index): {position}")
except ValueError:
    print(f"Element {search_element} not found in the array.")
