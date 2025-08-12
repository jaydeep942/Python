# Write a program to find out and display the common and the non common elements in the list using membership operators


list1= [10,20,30,40,50,60,70,80,90,100]
list2=[5,10,15,20,25,30,35,40,45,50]

common_elements = []
non_common_elements = []

for item in list1:
    if item in list2:
        common_elements.append(item)
    else:
        non_common_elements.append(item)

for item in list2:
    if item not in list1:
        non_common_elements.append(item)

print("Common elements:", common_elements)
print("Non-common elements:", non_common_elements)