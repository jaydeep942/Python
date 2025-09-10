# Write a program to understand various methods of array class
# mentioned: append, insert, remove, pop, index, tolist and count.

list_array = [1,2,3,4,5,6,7,8,9,10]
print("Original List: ", list_array)

# append() → adds element at the end
list_array.append(11)
print("List after append: ", list_array)

# insert() → inserts at a given index
list_array.insert(0,999)
print("list after insert", list_array)

# remove() → removes first occurrence of value
list_array.remove(999)
print("List after remove: ", list_array)

# pop() → removes element at index (or last element if not given)
list_array.pop()
print("List after pop: ", list_array)

list_array.pop(3)# removes element at index 3
print("List after pop at index 3: ", list_array)

# index() → returns index of first occurrence
print("Index of 5 is: ", list_array.index(5))

# tolist() → converts array into normal Python list
list_version = list_array[:] # to list when work when we use the array module and that module copy in simple list list_array.tolist()
print("Converted to list:", list_version)

# count() → counts occurrences of a value
list_array.append(30)
list_array.append(30)
print("Array after adding 30 twice:", list_array)
print("Count of 30:", list_array.count(30))