import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="root")

db_cursor=mydb.cursor()

db_cursor.execute("select * from  LearnCoding.Emp")
for db_data in db_cursor.fetchall():
    print(db_data) 