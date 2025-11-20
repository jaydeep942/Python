# Write a program to delete a row from an employee table by accepting the employee identity number (eid) from the use

import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shashwat@8866",  # for the university we add that password
    unix_socket=None,     
    use_pure=True, 
    database="Sample_DB"
)

cursor = con.cursor()

# Take employee id from user
eid = int(input("Enter Employee ID to delete: "))

# SQL query to delete the row
query = "DELETE FROM employee WHERE eid = %s"

cursor.execute(query, (eid,))
con.commit()

print("Record deleted successfully!")

# Close connection
cursor.close()
con.close()
