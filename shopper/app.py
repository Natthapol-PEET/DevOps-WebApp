from flask import  Flask,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product_detail')
def product():
    return render_template('product_detail.html')

if __name__== "__main__":
    app.run(debug=True)
