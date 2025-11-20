# Write a program to increase the salary (sal) of an employee in the employee table by accepting the employee identity number (eid) from the user.


import mysql.connector

# connect to MySQL
con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shashwat@8866",  # for the university we add that password
    unix_socket=None,     # disable named pipe completely
    use_pure=True, #
    database="Sample_DB"
)

cur = con.cursor()

# take employee id from user
eid = int(input("Enter Employee ID to increase salary: "))

# check if employee exists
cur.execute("SELECT sal FROM EMPLOYEE WHERE eid = %s", (eid,))
row = cur.fetchone()

if row is None:
    print("Employee not found!")
else:
    old_sal = row[0]
    inc = float(input("Enter amount to increase salary: "))
    new_sal = old_sal + inc

    # update salary
    cur.execute("UPDATE EMPLOYEE SET sal = %s WHERE eid = %s", (new_sal, eid))
    con.commit()

    print(f"Salary updated successfully! New Salary = {new_sal}")

cur.close()
con.close()
