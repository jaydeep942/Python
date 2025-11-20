# Write a program to display a histogram showing the number of employees of specific age groups.
import matplotlib.pyplot as plt

# Sample employee ages
ages = [22, 25, 27, 29, 30, 32, 35, 36, 38, 40, 42, 45, 47, 50, 52]

# Define age group bins
bins = [20, 30, 40, 50, 60]   # 20–30, 30–40, 40–50, 50–60

# Plot histogram
plt.hist(ages, bins=bins, edgecolor='black')

# Labels and Title
plt.xlabel("Age Groups")
plt.ylabel("Number of Employees")
plt.title("Employee Age Group Distribution")

# Display graph
plt.show()
