from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,IntegerField

class FL2(FlaskForm): #Volunteer sign up

    name = StringField('Full Name:')
    password = StringField('Password:')
    contact = IntegerField('Phone Number:')
    area = StringField('General Area:')
    address = StringField('Address:')
    submit = SubmitField('Submit')

class FL5(FlaskForm): #Volunteer log in

    name = StringField('Full Name:')
    password = StringField('Password:')