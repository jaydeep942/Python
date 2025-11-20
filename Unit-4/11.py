# Create a DataFrame  df = pd.DataFrame({'Category': ['A', 'B', 'A', 'B'], 'Value': [10,20, 30, 40]}).  Group the data by the 'Category' column and calculate the multiple aggregation functions like mean, maximum and minimum of the'Value' for each group.
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40]
})

# Group by Category and apply multiple aggregations
result = df.groupby('Category')['Value'].agg(['mean', 'max', 'min'])

print(result)
