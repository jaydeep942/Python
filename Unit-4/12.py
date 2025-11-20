# Write a program to display employee id numbers on X-axis and their salaries on Y- axis in the form of bar graph
import matplotlib.pyplot as plt

# Sample data
employee_ids = [101, 102, 103, 104, 105]
salaries = [25000, 30000, 28000, 35000, 40000]

# Plot bar graph
plt.bar(employee_ids, salaries)

# Labels and Title
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.title("Employee Salary Chart")

# Show graph
plt.show()
