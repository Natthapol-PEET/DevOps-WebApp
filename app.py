from flask import  Flask,render_template, request
from flask_bootstrap import Bootstrap
from numpy import array
import mysql.connector

app = Flask(__name__)
Bootstrap(app)

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'coffee_shop'
    }
mydb = mysql.connector.connect(**config)
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

def GET_SUMMARY_fn(date):
    mycursor.execute("SELECT prod_id, name, price FROM coffee_data")
    myresult = mycursor.fetchall()

    prod_id = []
    name = []
    price = []

    vsql = []

    for x in array(myresult):
        prod_id.append(x[0])
        name.append(x[1])
        price.append(x[2])

    count = []

    for i in prod_id:
        sql = "SELECT COUNT(prod_id) FROM order_hist WHERE prod_id LIKE " +str(i)+ " and date BETWEEN '"+str(date)+" 00:00:00' AND '"+str(date)+" 23:59:00' "
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        count.append(myresult[0][0])
        vsql.append(sql)

    d = []
    data = []

    for i in range(len(prod_id)):
        d.append(name[i])
        d.append(count[i])
        d.append( price[i]*count[i] )
        data.append(d)
        d = []

    value = []
    NUM = 0
    TOTAL = 0
    summary = []

    for x in data:
        if x[2] is '':
            x[2] = 0
        value.append(x)
        NUM += int(x[1])
        TOTAL += float(x[2])
    summary.append('summary')
    summary.append(NUM)
    summary.append(TOTAL)

    return value, summary, vsql


@app.route('/')
def index():

    Smoothie = [   [["Americano Smoothie", "static/coffeeimg/smoothie/americano.jpg", 45],
                    ["Cappucino Smoothie", "static/coffeeimg/smoothie/cappuccino.jpg", 40],
                    ["Cocoa Smoothie", "static/coffeeimg/smoothie/cocoashake.jpg", 45],
                    ["Espresso Smoothie", "static/coffeeimg/smoothie/expresso.jpg", 45]],

                    [["Green Tea Smoothie", "static/coffeeimg/smoothie/Green-Smoothie.jpg", 45],
                    ["Milk Smoothie", "static/coffeeimg/smoothie/milk-smoothie.jpg", 45],
                    ["Mocha Smoothie", "static/coffeeimg/smoothie/mocha.jpg", 35],
                    ["Thai Milk Tea Smoothie", "static/coffeeimg/smoothie/thai-milk-tea.jpg", 35]]
                ]

    TYPE = ['cool', 'hot', 'smoothie']
    COOL, HOT, SMOOTHIE = [], [], []
    j = 0

    for i in TYPE:
        sql = "SELECT prod_id, path_img, name, price FROM coffee_data where type like '"+i+"' "
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        if j == 0:
            COOL = myresult
        elif j == 1:
            HOT = myresult
        else:
            SMOOTHIE = myresult
        j += 1

    COOL = group(COOL)
    HOT = group(HOT)
    SMOOTHIE = group(SMOOTHIE)


    return render_template('index.html', Smoothie=SMOOTHIE, Cool=COOL, Hot=HOT)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/show', methods=['POST'])
def get_login():
    user = request.form['uname']
    # pwd = request.form['psw']

    # if user == 'PEET' and pwd == '10042541':
    #     text = 'Welcome to Shop'
    # else:
    #     text = 'Error !!'

    return render_template('show.html', text=user)

@app.route('/show')
def get_login2():
	return render_template('show.html')

@app.route('/product_detail', methods=['POST'])
def product():
    product = request.form['product']

    data = [product, "ร้อน", "1001", 45]

    return render_template('product_detail.html', data=data)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/invoice')
def invoice():
    customer_address = ["Mr.Nonthasri  Nonthasri", "83/3 Kud Khanuan Bungkaew Subdistrict", "Non Sa-at District", "Udon Thani Province 41240", "093-1851721"]
    META = ["000123", "December 15, 2009", 875.00]
    values = [["SSL Renewals", "Yearly renewals of SSL certificates on main domain and several subdomains", 75.00, 3, 75.00],
          ["SSL Renewals", "Yearly renewals of SSL certificates on main domain and several subdomains", 75.00, 3, 75.00],
          ["SSL Renewals", "Yearly renewals of SSL certificates on main domain and several subdomains", 75.00, 3, 75.00]]
    STAB = [875.00, 875.00, 0.00, 875.00]

    return render_template('invoice.html', META=META, list_data=values, customer_address=customer_address, STAB=STAB)

@app.route('/summary')
def summary():
    values = [['coffee', 1, 30], ['Fresh milk', 40, 50], ['Latte', 40, 50]]
    sum = ["summary", 9, 215]

    return render_template('summary.html', data=values, sum=sum)

@app.route('/summary', methods=['POST'])
def get_summary():

    birthday = request.form['birthday']

    # values = [['coffee', 1, 1], ['Fresh milk', 40, 50], ['Latte', 40, 50]]
    # sum = ["summary", 9, 215]

    values, sum, sql = GET_SUMMARY_fn(str(birthday))

    return render_template('summary.html', data=values, sum=sum, birthday=str(birthday), sql=sql)

if __name__== "__main__":
    app.run(debug=True)
