import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="root")

db_cursor=mydb.cursor()

db_delteData="delete from LearnCoding.Emp where Name=%s"
db_value=("Nitin",)

db_cursor.execute(db_delteData,db_value)

mydb.commit()

print(db_cursor.rowcount,"Record Deleted!!")