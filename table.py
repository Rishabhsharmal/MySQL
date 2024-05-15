import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="root",database="LearnCoding")

db_cursor=mydb.cursor()

db_cursor.execute("create table Emp2(Roll int,Name varchar(20))")

print("table created")


db_cursor.execute("show tables")
for i in db_cursor:
    print(i)
 