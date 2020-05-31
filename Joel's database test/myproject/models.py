#Models.py

from myproject import db

class Elderly(db.Model):

    __tablename__ = 'Elderlies'

    id = db.Column(db.Integer,primary_key = True)
    full_name = db.Column(db.Text)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    contact1 = db.Column(db.Integer)
    area = db.Column(db.Text)
    address = db.Column(db.Text)
    groceries =db.relationship('Grocery',backref='elderly')
    helper = db.relationship('Helper',backref='elderly')

    def __init__(self,full_name,username,password,contact1,area,address):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.contact1= contact1
        self.area = area
        self.address = address

    def __repr__(self):
        if self.helper:
            return f" {self.full_name} is helped by {self.helper}"
        else:
            return f"{self.password}"

class Grocery(db.Model):

    __tablename__ = "Groceries"

    id = db.Column(db.Integer,primary_key=True)
    groceries= db.Column(db.Text)
    elderly_id = db.Column(db.Integer,db.ForeignKey('Elderlies.id'))

    def __init__(self,groceries,elderlies_id):
        self.groceries = groceries
        self.elderlies = elderlies_id

class Helper(db.Model):

    __tablename__ = "Helpers"

    id = db.Column(db.Integer,primary_key=True)
    full_name = db.Column(db.Text)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    contact1 = db.Column(db.Integer)
    area = db.Column(db.Text)
    address = db.Column(db.Text)
    elderly_id = db.Column(db.Integer,db.ForeignKey('Elderlies.id'))

    def __init__(self,full_name,username,password,contact1,area,address):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.contact1= contact1
        self.area = area
        self.address = address

