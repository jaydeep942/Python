# Write a program to handle some built in exceptions like ZeroDivisionError


# Program to handle built-in exceptions

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    
    result = num1 / num2
    print(f"Result = {result}")

except ZeroDivisionError:
    print("❌ Error: Division by zero is not allowed!")

except ValueError:
    print("❌ Error: Please enter only numeric values!")

except Exception as e:   # handles any other exception
    print("❌ Unexpected Error:", e)

else:
    print("✅ Division successful, no error occurred.")

finally:
    print("Program execution completed.")
