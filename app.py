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

UserLogin = 'Login'
PageIndex = 0

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
    
    global PageIndex
    PageIndex = 1

    return render_template('index.html', Smoothie=SMOOTHIE, Cool=COOL, Hot=HOT, UserLogin=UserLogin)

@app.route('/login')
def login():
    sql = " select uid, name, address, tel_user from user where uid = 'peet123' "
    mycursor.execute(sql)
    userdetail = mycursor.fetchall()
    return render_template('login.html', UserLogin=UserLogin, userdetail=userdetail)

@app.route('/get_login', methods=['POST'])
def get_login():
    user = request.form['uname']
    pwd = request.form['psw']

    uidpass = [user, pwd]

    mycursor.execute("SELECT uid, passwd FROM user")
    myresult = mycursor.fetchall()

    global UserLogin

    sql = " select uid, name, address, tel_user from user where uid = 'peet123' "
    mycursor.execute(sql)
    userdetail = mycursor.fetchall()

    text = ''

    if uidpass[0] in array(myresult) and uidpass[1] in array(myresult):
        UserLogin = uidpass[0]
    else:
        UserLogin = 'Login'
        return render_template('login.html', UserLogin=UserLogin, text='**Login failed')

    temp = 'index.html'
    if PageIndex == 1:
        temp = 'index.html'
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

        return render_template(temp, Smoothie=SMOOTHIE, Cool=COOL, Hot=HOT, UserLogin=UserLogin, userdetail=userdetail)

    elif PageIndex == 2:
        temp = 'index.html'
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

        return render_template(temp, Smoothie=SMOOTHIE, Cool=COOL, Hot=HOT, UserLogin=UserLogin, userdetail=userdetail)
    elif PageIndex == 3:
        summary()
    else:
        return render_template('login.html', UserLogin=UserLogin, userdetail=userdetail)

    

@app.route('/show')
def get_login2():
	return render_template('show.html')

@app.route('/product_detail', methods=['POST','GET'])
def product():
    id = request.form.get('id')
    sql = "SELECT name, price, type, des, path_img FROM coffee_data where prod_id like '"+id+"' "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    data =[id]
    
    global PageIndex
    PageIndex = 2

    return render_template('product_detail.html', data=data, data_info=myresult, UserLogin=UserLogin)

@app.route('/cart')
def cart():
    global PageIndex
    PageIndex = 1

    return render_template('cart.html', UserLogin=UserLogin)

@app.route('/invoice')
def invoice():

    if UserLogin == 'peet123':
        customer_address = ["Mr.Nonthasri  Nonthasri",
                        "83/3 Kud Khanuan Bungkaew Subdistrict",
                        "Non Sa-at District",
                        "Udon Thani Province 41240",
                        "093-1851721"]

    elif UserLogin == 'peng123':
        customer_address = ["anaphut rattanakham",
                        "7/3 ban buangdanag",
                        "patumrat roi-et 45190",
                        "",
                        "0649724822"]

    elif UserLogin == 'tong123':
        customer_address = ["natthapol",
                     "8/3 ban nuang jonggram ",
                     "hell 5555",
                     "",
                     "0666131313"]
    else:
        customer_address = ["",
                     "",
                     "",
                     "",
                     ""]


    META = ["000123", "December 15, 2009", 875.00]

    values = [["SSL Renewals", "Yearly renewals of SSL certificates on main domain and several subdomains", 75.00, 3, 75.00],
          ["SSL Renewals", "Yearly renewals of SSL certificates on main domain and several subdomains", 75.00, 3, 75.00],
          ["SSL Renewals", "Yearly renewals of SSL certificates on main domain and several subdomains", 75.00, 3, 75.00]]

    STAB = [875.00, 875.00, 0.00, 875.00]

    global PageIndex
    PageIndex = 1

    return render_template('invoice.html', META=META, list_data=values, customer_address=customer_address, STAB=STAB, UserLogin=UserLogin)

@app.route('/summary')
def summary():
    values = [['coffee', 1, 30], ['Fresh milk', 40, 50], ['Latte', 40, 50]]
    sum = ["summary", 9, 215]

    global PageIndex
    PageIndex = 3

    return render_template('summary.html', data=values, sum=sum, UserLogin=UserLogin)

@app.route('/summary', methods=['POST'])
def get_summary():

    birthday = request.form['birthday']

    # values = [['coffee', 1, 1], ['Fresh milk', 40, 50], ['Latte', 40, 50]]
    # sum = ["summary", 9, 215]

    values, sum, sql = GET_SUMMARY_fn(str(birthday))

    return render_template('summary.html', data=values, sum=sum, birthday=str(birthday), UserLogin=UserLogin)

@app.route('/logout', methods=['POST'])
def logout():
    global UserLogin
    UserLogin = 'Login'

    return render_template('login.html', UserLogin=UserLogin)



if __name__== "__main__":
    app.run(debug=True)
