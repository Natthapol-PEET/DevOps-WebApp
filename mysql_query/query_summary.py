import mysql.connector
from numpy import array

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="coffee_shop"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT prod_id, name, price FROM coffee_data")
myresult = mycursor.fetchall()

prod_id = []
name = []
price = []

for x in array(myresult):
    prod_id.append(x[0])
    name.append(x[1])
    price.append(x[2])


date = '2020-04-26'
count = []

# SELECT COUNT(prod_id) FROM order_hist WHERE prod_id LIKE 1001 and date BETWEEN '2020-04-26 12:00:00' AND '2020-04-26 23:30:00'

for i in prod_id:
    sql = "SELECT COUNT(prod_id) FROM order_hist WHERE prod_id LIKE " +str(i)+ " and date BETWEEN '"+str(date)+" 12:00:00' AND '"+str(date)+" 23:30:00' "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    count.append(myresult[0][0])

d = []
data = []

for i in range(len(prod_id)):
    d.append(name[i])
    d.append(count[i])
    d.append( price[i]*count[i] )
    data.append(d)
    d = []


for x in data:
    if x[2] is '':
        x[2] = 1
    print(x)