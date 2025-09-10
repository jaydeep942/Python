# Write a python program that removes any repeated items
# from a list so that each item appears at most once. For
# instance,the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0]
def remove_duplicates(input_list):
    # Create an empty list to store unique items
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage
original_list = list(map(int, input("Enter the numbers (space-separated): ").split()))
print("Original list:", original_list)
print("List after removing duplicates:", remove_duplicates(original_list))