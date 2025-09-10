# Bubble Sort in Python


# def bubble_sort(arr):
#     n = len(arr)  # length of the list
    
#     # Outer loop for number of passes
#     for i in range(n - 1):  
#         # Inner loop for comparing elements
#         for j in range(n - i - 1):  
#             # Compare adjacent elements
#             if arr[j] > arr[j + 1]:
#                 # Swap if they are in the wrong order
#                 # arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 arr[j], arr[j + 1] = arr[j], arr[j +1]


#     return arr


# # Example usage
# numbers = [64, 34, 25, 12, 22, 11, 90]
# print("Original list:", numbers)

# sorted_list = bubble_sort(numbers)
# print("Sorted list:", sorted_list)


# Bubble Sort in Python with user input

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Take input from user
# Example input: 64 34 25 12 22 11 90
user_input = input("Enter numbers separated by space: ")

# Convert input string into a list of integers
numbers = list(map(int, user_input.split()))

print("Original list:", numbers)

sorted_list = bubble_sort(numbers)
print("Sorted list:", sorted_list)
