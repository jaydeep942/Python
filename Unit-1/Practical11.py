# Write a python program that asks the user to enter a length in centimeters. If the user enters a negative length, the program should tell the user that the entry is invalid. Otherwise, the program should convert the length to inches and print out the result. (2.54 = 1 inch)
# Take length in centimeters from user
cm = float(input("Enter length in centimeters: "))

# Check for negative input
if cm < 0:
    print("Invalid entry! Length cannot be negative.")
else:
    # Convert to inches (1 inch = 2.54 cm)
    inches = cm / 2.54
    print(f"{cm} cm is equal to {inches:.2f} inches.")
