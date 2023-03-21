
import pymysql
import MySQLdb
mydb = MySQLdb.connect(host="192.168.30.93",user="root",password="root")
mycursor = mydb.cursor()
mycursor.execute("show databases")
data =mycursor.fetchall()
print(data)

"""
import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.1.23",
  user="Madhav",
  password="Madhav@1996",
  database="madhav"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Sharma;")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
"""
