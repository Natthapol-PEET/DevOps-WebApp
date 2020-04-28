from flask import  Flask,render_template, request
from flask_bootstrap import Bootstrap
import mysql.connector

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'coffee_shop'
    }
mydb = mysql.connector.connect(**config)
mycursor = mydb.cursor()
app = Flask(__name__)
Bootstrap(app)

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
    sql = "SELECT * FROM coffee_data where type like 'smoothie' "
	
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
	
    array= [    [myresult[0],
		     myresult[1],
		     myresult[2],
		     myresult[3]],
		     
                    [myresult[4],
		     myresult[5],
		     myresult[6],
		     myresult[7]]
		]

    return render_template('index.html', Smoothie=array)

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
	
	sql = "SELECT * FROM coffee_data where type like 'smoothie' "
	
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	
	array= [    [myresult[0],
		     myresult[1],
		     myresult[2],
		     myresult[3]],
		     
                    [myresult[4],
		     myresult[5],
		     myresult[6],
		     myresult[7]]
		]
	array2=myresult[0][1]
	
	return render_template('show.html', datadb=array)	



@app.route('/product_detail', methods=['POST'])
def product():
    product = request.form['product']

    data = [product, "ร้อน", "1001", 45]

    return render_template('product_detail.html', data=data)

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
    values = [['coffee', 20, 30], ['Fresh milk', 40, 50], ['Latte', 40, 50]]
    sum = ["summary", 9, 215]

    return render_template('summary.html', data=values, sum=sum)

@app.route('/summary', methods=['POST'])
def get_summary():

    birthday = request.form['birthday']

    values = [['coffee', 1, 1], ['Fresh milk', 40, 50], ['Latte', 40, 50]]
    sum = ["summary", 9, 215]

    return render_template('summary.html', data=values, sum=sum, birthday=str(type(birthday)) + str(birthday))

if __name__== "__main__":
    app.run(debug=True)
