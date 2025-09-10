# Write a program to handle multiple exceptions

# Program to handle multiple exceptions

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    
    result = num1 / num2
    print(f"Result = {result}")

    # Example: Accessing an invalid index
    numbers = [1, 2, 3]
    index = int(input("Enter index to access from list: "))
    print(f"Element at index {index} is {numbers[index]}")

# Handling specific exceptions
except ZeroDivisionError:
    print("❌ Error: Division by zero is not allowed!")

except ValueError:
    print("❌ Error: Please enter valid integers only!")

except IndexError:
    print("❌ Error: List index out of range!")

# Handling multiple exceptions in one line
except (TypeError, OverflowError) as e:
    print("❌ Error occurred:", e)

# Generic exception (fallback)
except Exception as e:
    print("❌ Unexpected error:", e)

else:
    print("✅ Program executed without errors.")

finally:
    print("Program execution finished.")
