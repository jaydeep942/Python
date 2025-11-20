# Create a DataFrame with columns ['Name', 'Age', 'Score']. Sort the DataFrame based on the 'Score' column in descending order

import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Name": ["Amit", "Riya", "Karan", "Meera"],
    "Age": [21, 22, 20, 23],
    "Score": [85, 92, 78, 90]
})

# Sort by 'Score' in descending order
sorted_df = df.sort_values(by="Score", ascending=False)

print(sorted_df)
