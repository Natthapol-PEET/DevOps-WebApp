from flask import  Flask,render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/show', methods=['POST'])
def get_login():
    user = request.form['uname']
    pwd = request.form['psw']

    if user == 'PEET' and pwd == '10042541':
        text = 'Welcome to Shop'
    else:
        text = 'Error !!'

    return render_template('show.html', text=text)

@app.route('/invoice')
def invoice():
    return render_template('invoice.html')

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
