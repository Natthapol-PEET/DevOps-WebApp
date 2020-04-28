import mysql.connector
from numpy import array

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="coffee_shop"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT uid, passwd FROM user")

myresult = mycursor.fetchall()

uidpass = ['peet123', 'natthapol123']

if uidpass[0] in array(myresult) and uidpass[1] in array(myresult):
  print('PASS !!!')
else:
  print('No PASS !!!')