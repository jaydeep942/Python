
# Write a program to display a pie chart showing the percentage of employees in each department of a company

import matplotlib.pyplot as plt

# Sample data: Number of employees in each department
departments = ['HR', 'Finance', 'IT', 'Sales', 'Marketing']
employees = [10, 15, 40, 25, 10]

# Plot pie chart
plt.pie(employees, labels=departments, autopct='%1.1f%%', startangle=90)

# Title
plt.title('Percentage of Employees in Each Department')

# Make chart a circle
plt.axis('equal')

# Show chart
plt.show()
