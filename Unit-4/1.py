# Write a program to create a database named “Sample_DB” in MySQL(). And create an EMPLOYEE Table in it with fields like eid,name and sal. Also enter some valid records in table. First ensure connection is made or not and then check if the database Sample_DB already exists or not, if yes then print appropriate message. Also display all records of Employee table.
import mysql.connector

# connect to MySQL
print("Before connect") # debugging line
con = mysql.connector.connect(
    host="127.0.0.1",   # OR localhost
    user="root",
    password="Shashwat@8866",
    unix_socket=None,     # disable named pipe completely
    use_pure=True, # when you have not start and not connect the DB like my case that time must be add this line
    port=3306
) 
print("Connected!") # debugging line
cur = con.cursor()

print("\nConnection Successful!\n")

# check database exists or not
cur.execute("SHOW DATABASES")
dblist = [d[0] for d in cur.fetchall()] # this is for tuple convert into list the dblist = ['sample_db', 'information_schema', 'mysql', 'performance_schema']


if "sample_db" in dblist:
    print("Database 'Sample_DB' already exists.")
else:
    cur.execute("CREATE DATABASE Sample_DB")
    print("Database 'Sample_DB' created.")

# use database
cur.execute("USE Sample_DB")

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS EMPLOYEE(
    eid INT PRIMARY KEY,
    name VARCHAR(30),
    sal FLOAT
)
""")
print("EMPLOYEE table ready.")

# insert records
try:
    cur.execute("INSERT INTO EMPLOYEE VALUES(1,'Raj',25000)")
    cur.execute("INSERT INTO EMPLOYEE VALUES(2,'Priya',30000)")
    cur.execute("INSERT INTO EMPLOYEE VALUES(3,'Amit',28000)")
    con.commit()
    print("Sample records inserted.")
except:
    print("Records already exist, skipping insertion.")

# display table data
cur.execute("SELECT * FROM EMPLOYEE")
data = cur.fetchall()

print("\n--- EMPLOYEE TABLE DATA ---")
for row in data:
    print(row)

# close connection
cur.close()
con.close()
