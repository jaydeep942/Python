# Write a program to create a list using range functions and
# perform append, update and delete elements operations
# in it.

# Create a list using range function
numbers = list(range(1, 18))  # will create [1, 2, 3, 4, 5]
print("Initial list:", numbers)

# Append an element
numbers.append(19)
print("After appending 19:", numbers)

# Update an element (change value at index 2)
numbers[2] = 20  # changes the 3rd element (index 2)
print("After updating index 2 to 20:", numbers)

# Delete an element (remove element at index 1)
del numbers[1]  # removes 2nd element
print("After deleting element at index 1:", numbers)
