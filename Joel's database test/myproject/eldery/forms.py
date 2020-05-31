from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,IntegerField

class FL1(FlaskForm): #elderly sign up

    name = StringField('Full Name:')
    password = StringField('Password:')
    contact = IntegerField('Phone Number:')
    area = StringField('General Area:')
    address = StringField('Address:')
    submit = SubmitField('Submit')


class FL4(FlaskForm): #elderly log in

    name = StringField('Full Name:')
    password = StringField('Password:')


class FC2(FlaskForm): #purchase forms

    purchases = StringField('Enter what you want here')
    elderlies_id =IntegerField("Enter_ID") #TO FIND WORKAROUND
    #add voice to text here
    submit = SubmitField('Add Owner')