import mysql.connector
from numpy import array

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="coffee_shop"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT bill_id FROM bill")
myresult = mycursor.fetchall()
data = array(myresult)

bill_id = []

for x in data:
    bill_id.append( int(x[0]) )

newBill = max(bill_id) + 1
newBill = '00' + str(newBill)

print(newBill)


# sql = "INSERT INTO bill (bill_id, balance) VALUES (%s, %s)"
# val = ("00124", 20)
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")