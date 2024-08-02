import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")



"""
conn.execute('''CREATE TABLE emp1
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print ("Table created successfully")



conn.execute("INSERT INTO emp1 (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Ram', 32, 'Vellore', 20000.00 )");

conn.execute("INSERT INTO emp1 (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Sam', 25, 'Katpadi', 15000.00 )");

conn.execute("INSERT INTO emp1 (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Kavi', 23, 'Ranipet', 20000.00 )");

conn.execute("INSERT INTO emp1 (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Ravi', 25, 'Arcot', 65000.00 )");

conn.commit()
print ("Records created successfully")


cursor = conn.execute("SELECT id, name, address, salary from emp1")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")

# for update
conn.execute("UPDATE emp1 set SALARY = 25000.00 where ID = 1")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from table1")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")

# delete
conn.execute("DELETE from emp1 where ID = 1;")
conn.commit()
print ("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from table1")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")
conn.close()
"""

