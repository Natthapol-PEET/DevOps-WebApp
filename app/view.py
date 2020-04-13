import app from app

@app.route('/')
def home():
	return "hello world"
