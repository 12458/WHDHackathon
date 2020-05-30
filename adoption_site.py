import os
from forms import  L1,L2,L4,L5,C2
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'Password'

############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

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




############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')
def H0():
    return render_template('H0.html')

@app.route('/L1', methods=['GET', 'POST'])
def L1(): #Elderly Sign up

    form = L1()

    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        confirm_password = form.password2.data
        contact = form.contact.data
        area = form.area.data
        address = form.address.data


        # Add new Elderly to database
        new_Elderly = Elderly(name)
        pw = Elderly(password)
        contact = Elderly(contact)
        area = Elderly(area)
        add = Elderly(address)
        db.session.add_all([new_Elderly,pw,contact,area,add])
        db.session.commit()

        return redirect(url_for('C1'))

    return render_template('L0.html',form=form)

@app.route('/L2', methods=['GET', 'POST'])
def L2(): #Helper Sign up
    form = L2()

    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        confirm_password = form.password2.data
        contact = form.contact.data
        area = form.area.data
        address = form.address.data


        # Add new Elderly to database
        new_Helper = Helper(name)
        pw = Helper(password)
        contact = Helper(contact)
        area = Helper(area)
        add = Helper(address)
        db.session.add_all([new_Helper,pw,contact,area,add])
        db.session.commit()

        return redirect(url_for('A1'))

    return render_template('L2.html',form=form)


@app.route('/C2', methods =['GET','POST'])
def C2():
    form = C2()

    if form.validate_on_submit():
        purchases = form.purchases.data
        Elderlies_id = form.Elderlies_id.data

        new_owner = Grocery(purchases,Elderlies_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('C3'))
    return render_template('C2.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)