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

if __name__== "__main__":
    app.run(debug=True)
