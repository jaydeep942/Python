# Create a sample list of 7 elements and implement the List
# methods mentioned: append, insert, copy, extend, count,
# remove, pop, sort, reverse and clear.

# Sample list
sample_list = [1, 2, 3, 4, 5, 6, 7]
print("Initial list:", sample_list)

# Append
sample_list.append(8)
print("After appending 8:", sample_list)

# Insert
sample_list.insert(0, 0)
print("After inserting 0 at index 0:", sample_list)

# Copy
copied_list = sample_list.copy()
print("Copied list:", copied_list)

# Extend
sample_list.extend([9, 10])
print("After extending with [9, 10]:", sample_list)

# Count
count_of_5 = sample_list.count(5)
print("Count of 5 in the list:", count_of_5)

# Remove
sample_list.remove(3)
print("After removing 3:", sample_list)

# Pop
popped_element = sample_list.pop()
print("Popped element:", popped_element)
print("After popping an element:", sample_list)

# Sort
sample_list.sort()
print("After sorting:", sample_list)

# Reverse
sample_list.reverse()
print("After reversing:", sample_list)

# Clear
sample_list.clear()
print("After clearing:", sample_list)