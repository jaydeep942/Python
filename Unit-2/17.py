# Write a program to convert the elements of two lists into keyvalue pairs of a dictionary

list1 = ['Maths', 'Python', 'SAD', 'PHP']
list2 = [50, 50, 40, 45]

# Convert lists to dictionary
subject_scores = dict(zip(list1, list2))

print("Subject Scores Dictionary:")
print(subject_scores)