import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class coffe_data(db.Model):
	__tablename__ = 'coffe'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	price = db.Column(db.Integer)
	cup_type = db.Column(db.String(20))

class user_data(db.Model):
	__tablename__ = 'User'
	id = db.Column(db.Integer , primary_key=True)
	id_user = db.Column(db.String(24), nullable = False , unique = True)
	password = db.Column(db.String(30),nullable = False)
	addresses = db.relationship("Address",uselist=False,back_populates="User")
	info = db.relationship("Info",uselist = False,back_populates = "User")

class Address(db.Model):
	__tablename__= 'address'
	id = db.Column(db.Integer , primary_key=True)
	address_id = db.Column(db.String(255), nullable = False)
	ban = db.Column(db.String(50))
	city = db.Column(db.String(40))

class Info(db.Model):
	__tablename__ = 'info'
	id = db.Column(db.Integer , primary_key=True)
	name = db.Column(db.String(255),nullable=False )
	email = db.Column(db.String(100))

