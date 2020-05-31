#Models.py

from myproject import db

class Elderly(db.Model):

    __tablename__ = 'Elderlies'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    password = db.Column(db.Text)
    contact = db.Column(db.Integer)
    area = db.Column(db.Text)
    address = db.Column(db.Text)
    groceries =db.relationship('Grocery',backref='elderly')
    helper = db.relationship('Helper',backref='elderly')

    def __init__(self,name,password,contact,area,address):
        self.name = name
        self.password = password
        self.contact= contact
        self.area = area
        self.address = address

    def __repr__(self):
        if self.groceries:
            return f" {self.name} would like {self.groceries}"
        else:
            return f"{self.name} has no orders yet"

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
    name = db.Column(db.Text)
    password = db.Column(db.Text)
    contact = db.Column(db.Integer)
    area = db.Column(db.Text)
    address = db.Column(db.Text)
    elderly_id = db.Column(db.Integer,db.ForeignKey('Elderlies.id'))

    def __init__(self,name,password,contact,area,address):
        self.name = name
        self.password = password
        self.contact= contact
        self.area = area
        self.address = address

