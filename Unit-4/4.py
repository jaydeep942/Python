# Create a Pandas Series from a list of integers
import pandas as pd

# Take input from user (comma-separated numbers)
user_input = input("Enter integers separated by commas: ")

# Convert input string → list of integers
numbers = list(map(int, user_input.split(',')))

# Create Series
s = pd.Series(numbers)

print("\nPandas Series:")
print(s)
