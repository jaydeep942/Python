#creating list

list = [22,10,52,40,33,68,9]

#Append Method 

list.append(7)
print("After append :",list)

#Insert Method

list.insert(5,99)
print("After Insert in 99 in 5th index :",list)

#copy Method

c = list.copy()
print("After copy of list :",c)

#extend method

ex = [50,55]
list.extend(ex)
print("After Extend :",list)

#count method

count = list.count(50)
print("Counting of 50 in list :",count)

#remove method

list.remove(50)
print("After Removing 50 in list :" , list)

#pop method

list.pop(0)
print("After pop in 0 index element ", list)

#sort method

list.sort()
print("After sorting list :",list)

#reverse method

list.reverse()
print("After reverse :",list)

#clear method

list.clear()
print("After clear :",list)
