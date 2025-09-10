# Write a lambda/Anonymous function to find bigger number in two given numbers

print('======')

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

bigger_number = lambda x, y: x if x > y else y

print(f"The bigger number between {x} and {y} is: {bigger_number(x, y)}")