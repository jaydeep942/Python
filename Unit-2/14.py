# Write a program to accept elements in the form of a tuple and display its minimum, maximum, sum and average.

# Accepting elements from the user
elements = input("Enter elements separated by commas: ")
# Creating a tuple from the input
elements_tuple = tuple(map(int, elements.split(",")))

# Calculating required values
min_value = min(elements_tuple)
max_value = max(elements_tuple)
sum_value = sum(elements_tuple)
average_value = sum_value / len(elements_tuple)

# Displaying the results
print("Minimum:", min_value)
print("Maximum:", max_value)
print("Sum:", sum_value)
print("Average:", average_value)
