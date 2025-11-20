# Create a DataFrame df = pd.DataFrame ({'A': [1, None, 3], 'B': [None, 4, 5]}). Fill missing values in column 'A' & ‘B’ with 0
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'A': [1, None, 3],
    'B': [None, 4, 5]
})

# Fill missing values in columns A and B with 0
df['A'] = df['A'].fillna(0)
df['B'] = df['B'].fillna(0)

print(df)
