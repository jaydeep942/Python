# Write a program to search an element in the list using for loop and also demonstrate the use of “else” with for loop.

# Sample list
numbers = [10, 20, 30, 40, 50, 60]

# Take input from the user
search_item = int(input("Enter the number to search: "))

# Search using for loop with else
for num in numbers:
    if num == search_item:
        print(f"Element {search_item} found in the list.")
        break
else:
    # This runs if the loop completes without 'break'
    print(f"Element {search_item} not found in the list.")
