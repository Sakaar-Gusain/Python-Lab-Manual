# Importing module 
import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "root",
    database = "sakaar"
)
cursorObject = mydb.cursor()
query1 = "INSERT INTO marks VALUES (5,'Aloo', 79)" 
query2 = "SELECT* FROM marks"
 


cursorObject.execute(query1)
mydb.commit()
 
myresult = cursorObject.fetchall()
 
for x in myresult:
    print(x)
 
# disconnecting from server
mydb.close()
