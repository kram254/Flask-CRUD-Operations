from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CustomerModel(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key= True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    gender = db.Column(db.String())
    occupations = db.Column(db.String())
    country = db.Column(db.String(80))

    def __init__(self, first_name, last_name,email, password, gender, occupations, country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.gender = gender
        self.occupations = occupations
        self.country = country

    def __repr__(self):
        return f"{self.first_name}:{self.last_name}"