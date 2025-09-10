# Create a program to sort tuple with nested tuples

nested_tuple = (('Maths', 50), ('Python', 50), ('SAD', 40), ('PHP', 45))

print("Original nested tuple:", nested_tuple)

# extra not use in this program Sorting the nested tuple based on the second element of each inner tuple
sorted_nested_tuple = tuple(sorted(nested_tuple, key=lambda x: x[1]))

print("Sorted nested tuple:", sorted_nested_tuple)