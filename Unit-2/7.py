# Write a program to pass a list to a function and display it
def display_list(input_list):
    print("The items in the list are:")
    for item in input_list:
        print(item)

# Example usage
user_list = list(map(int, input("Enter the numbers (space-separated): ").split()))
display_list(user_list)
