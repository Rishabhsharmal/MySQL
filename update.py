import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="root")

db_cursor=mydb.cursor()

db_Updatedata="update LearnCoding.Emp set roll=%s where Name=%s"
db_value=(20,"Nitin")


db_cursor.execute(db_Updatedata,db_value)
mydb.commit()

print(db_cursor.rowcount,"data Updated!!")