import pandas as pd

# Dictionary data
data = {
    "Name": ["Amit", "Riya", "Karan"],
    "Age": [21, 22, 20],
    "City": ["Surat", "Ahmedabad", "Vadodara"]
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)


#  Optional : user give the value and then create dataframe
# import pandas as pd

# # Empty dictionary
# data = {}

# # Ask number of columns
# n = int(input("Enter number of columns: "))

# for i in range(n):
#     key = input(f"Enter column name {i+1}: ")
#     values = input(f"Enter values for '{key}' separated by commas: ")
    
#     # Convert string to list
#     data[key] = values.split(",")

# # Create DataFrame
# df = pd.DataFrame(data)

# print("\nGenerated DataFrame:")
# print(df)
