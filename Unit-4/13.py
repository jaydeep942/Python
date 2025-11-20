# Write a program to display employee id numbers on X-axis and their salaries on Y- axis in the form of bar graph for two departments of a company
import matplotlib.pyplot as plt
import numpy as np

# Department 1 data
emp_id_dept1 = [101, 102, 103]
salary_dept1 = [25000, 30000, 28000]

# Department 2 data
emp_id_dept2 = [201, 202, 203]
salary_dept2 = [27000, 32000, 35000]

# Create positions for bars
x1 = np.arange(len(emp_id_dept1))
x2 = np.arange(len(emp_id_dept2)) + len(emp_id_dept1)  # shift for 2nd dept

# Combine x-axis labels
all_emp_ids = emp_id_dept1 + emp_id_dept2
all_positions = np.concatenate((x1, x2))

# Plot bar graph
plt.bar(x1, salary_dept1, label="Department 1")
plt.bar(x2, salary_dept2, label="Department 2")

# Labels and Title
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.title("Employee Salary Comparison of Two Departments")

# X-axis labels
plt.xticks(all_positions, all_emp_ids)

# Show legend
plt.legend()

# Display graph
plt.show()
