import mysql.connector
from numpy import array

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="coffee_shop"
)
mycursor = mydb.cursor()


def group(data):
  ar0, ar1, arr3d = [], [], []
  i = 0

  for x in array(data):
    if i < 4:
      ar0.append( x )
    else:
      ar1.append( x )
    i += 1

  arr3d.append( ar0 )
  arr3d.append( ar1 )

  return arr3d



TYPE = ['cool', 'hot', 'smoothie']
COOL, HOT, SMOOTHIE = [], [], []
j = 0

for i in TYPE:
  sql = "SELECT prod_id, path_img, name, price FROM coffee_data where type like '"+i+"' "
  mycursor.execute(sql)
  myresult = mycursor.fetchall()

  if j == 0:
    COOL.append(myresult)
  elif j == 1:
    HOT.append(myresult)
  else:
    SMOOTHIE.append(myresult)
  j += 1

COOL = group(COOL)
HOT = group(HOT)
SMOOTHIE = group(SMOOTHIE)

print(COOL[0][0])
