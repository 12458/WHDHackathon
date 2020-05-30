# forms.py

# Elderly
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField


class L1(FlaskForm):  # elderly sign up

    name = StringField('Full Name:')
    password = StringField('Password:')
    confirm_password = StringField('Confirm Password:')
    contact = IntegerField('Phone Number:')
    area = StringField('General Area:')
    address = StringField('Address:')
    submit = SubmitField('Submit')


class L4(FlaskForm):  # elderly log in

    name = StringField('Full Name:')
    password = StringField('Password:')


class C2(FlaskForm):  # purchase forms

    purchases = StringField('Enter what you want here')
    elderlies_id = IntegerField("Enter_ID")  # TO FIND WORKAROUND
    # add voice to text here
    submit = SubmitField('Add Owner')

# Volunteer Forms


class L2(FlaskForm):  # Volunteer sign up

    name = StringField('Full Name:')
    password = StringField('Password:')
    confirm_password = StringField('Confirm Password:')
    contact = IntegerField('Phone Number:')
    area = StringField('General Area:')
    address = StringField('Address:')
    submit = SubmitField('Submit')


class L5(FlaskForm):  # Volunteer log in

    name = StringField('Full Name:')
    password = StringField('Password:')
