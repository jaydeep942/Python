# Create a program name “employee.py” and implement the
# functions DA, HRA, PF, and ITAX. Create another program that
# uses the function of employee module and calculates gross and
# net salaries of an employee

# creating that required module in this folder
import practical_10_module as emp


basic_salary = float(input("Enter the basic salary: "))

da = emp.DA(basic_salary)
hra = emp.HRA(basic_salary)
pf = emp.PF(basic_salary)
gross_salary = basic_salary + da + hra 
itax = emp.ITAX(gross_salary)

net_salary = gross_salary - (pf + itax)

print("==============Real salary without cuts==============")
print(f"Gross Salary: {gross_salary}")

print("==============salary with cuts==============")
print(f"Net Salary: {net_salary}")


print("==============Breakdown of components==============")
print(f"DA: {da}, HRA: {hra}, PF: {pf}, ITAX: {itax}")
