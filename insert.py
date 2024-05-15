import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="root",database="LearnCoding")

db_cursor=mydb.cursor()

db_insert= "insert into Emp(Roll,Name) values(%s,%s)"

db_list=[(30,"ANil"),(40,"Nitin"),(50,"kittu")]
db_cursor.executemany(db_insert,db_list)
mydb.commit()


print(db_cursor.rowcount,"Record Inserted")