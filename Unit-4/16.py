# Write a program to create a line graph to show the profits of a company in various years
import matplotlib.pyplot as plt

# Sample data
years = [2018, 2019, 2020, 2021, 2022, 2023]
profits = [50000, 55000, 52000, 60000, 65000, 70000]

# Plot line graph
plt.plot(years, profits, marker='o')

# Labels and Title
plt.xlabel("Years")
plt.ylabel("Profit (in ₹)")
plt.title("Company Profit Over the Years")

# Show grid (optional)
plt.grid(True)

# Display the graph
plt.show()
