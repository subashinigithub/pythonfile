import pymysql as mysql
""" connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.execute()
cursor.execute("create database hello") """
connection=mysql.connect(host="localhost",user="root",password="livewire",database="hello")
cursor=connection.cursor()
""" cursor.execute("CREATE TABLE user9(userid Int primary key,username varchar(60))")
cursor.execute("show tables")
print("number of tables in database: ")
for x in cursor:
    print("\t",x) """

""" cursor.execute("CREATE TABLE admin(adminid int primary key,adminname varchar(100),userid int)")
cursor.execute("show tables")
print("Number of tables in database: ")
for x in cursor:
    print("\t",x) """

""" s="insert into admin values(%s,%s,%s)"
t=[(2,"harish",1),(3,"harish",2)]
cursor.executemany(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted",cursor.lastrowid)

 """
cursor.execute("select * from admin")
result=cursor.fetchall()
print("content in the python: ")
for x in result:
    print("\t",x)

""" sql="update admin set adminname='bala' where adminid=2;"
cursor.execute(sql)
connection.commit()
 """
""" sql="DELETE From admin WHERE adminid=3;"
cursor.execute(sql)
connection.commit()
print(cursor.rowcount,"record(s)deleted")
 """