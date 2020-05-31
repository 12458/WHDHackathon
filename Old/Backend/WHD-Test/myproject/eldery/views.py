from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Elderly,Grocery
from myproject.eldery.forms import FL1,FC2

elderly_blueprints = Blueprint('elderly',__name__, template_folder='templates/elderly')

@elderly_blueprints.route('/L1',methods=['GET','POST'])
def L1():

    form = FL1

    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        contact = form.contact.data
        area = form.area.data
        address = form.address.data

        # Add new Elderly to database
        new_Elderly = Elderly(name)
        pw = Elderly(password)
        contact = Elderly(contact)
        area = Elderly(area)
        add = Elderly(address)
        db.session.add_all([new_Elderly, pw, contact, area, add]) # USE DATABASE HERE
        db.session.commit()

        return redirect(url_for('elderly.C1'))

    return render_template('L1.html', form=form)

@elderly_blueprints.route('/C2',methods=['GET','POST'])
def C2():
    form = FC2()

    if form.validate_on_submit():
        purchases = form.purchases.data
        Elderlies_id = form.Elderlies_id.data

        grocer = Grocery(purchases,Elderlies_id)
        db.session.add(grocer)
        db.session.commit()

        return redirect(url_for('elderly.C3'))
    return render_template('C2.html', form=form)

@elderly_blueprints.route('/C3')
def C3():
    return render_template('C3.html')

@elderly_blueprints.route('/L4')
def L4():
    return render_template('L4.html')



