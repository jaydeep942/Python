# Create a DataFrame with columns ['Name', 'City']. Access column "City" and display it
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Name": ["Amit", "Riya", "Karan"],
    "City": ["Surat", "Mumbai", "Delhi"]
})

# Access and display the "City" column
print(df["City"])