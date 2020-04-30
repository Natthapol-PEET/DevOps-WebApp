import mysql.connector
from numpy import array

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="coffee_shop"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM coffee_data")

myresult = mycursor.fetchall()

data = array(myresult)

print(data)