# Write a menu driven program to perform the following menu: (1) Find Area of Circle (2) Find Area of Triangle (3) Find Area of Square (4) Find Simple Interest (5) Exit. (using match-case)

import math

while True:
    print("\nMenu:")
    print("1. Find Area of Circle")
    print("2. Find Area of Triangle")
    print("3. Find Area of Square")
    print("4. Find Simple Interest")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    match choice:
        case 1:  # Area of Circle
            r = float(input("Enter radius: "))
            area = math.pi * r * r
            print(f"Area of Circle = {area:.2f}")

        case 2:  # Area of Triangle
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = 0.5 * base * height
            print(f"Area of Triangle = {area:.2f}")

        case 3:  # Area of Square
            side = float(input("Enter side length: "))
            area = side * side
            print(f"Area of Square = {area:.2f}")

        case 4:  # Simple Interest
            p = float(input("Enter principal amount: "))
            r = float(input("Enter rate of interest: "))
            t = float(input("Enter time in years: "))
            si = (p * r * t) / 100
            print(f"Simple Interest = {si:.2f}")

        case 5:  # Exit
            print("Exiting program. Goodbye!")
            break

        case _:  # Invalid choice
            print("Invalid choice! Please enter a number between 1 and 5.")
