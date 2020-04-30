import mysql.connector
from numpy import array

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="coffee_shop"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM chart_data ch INNER JOIN coffee_data co WHERE ch.prod_id = co.prod_id and uid like 'peet123' ")

myresult = mycursor.fetchall()

data = array(myresult)

print(data)