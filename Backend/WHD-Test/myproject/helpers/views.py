from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Elderly,Grocery,Helper
from myproject.helpers.forms import FL2

helpers_blueprint = Blueprint('helpers',__name__,template_folder='template/helpers')


@helpers_blueprint.route('/L2',methods= ['GET','POST'])
def L2(): #Helper Sign up
    form = FL2()

    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
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

        return redirect(url_for('helpers.A1'))

    return render_template('L2.html',form=form)

@helpers_blueprint.route('/L5')
def L5():
    return render_template('L5.html')

@helpers_blueprint.route('/A1')
def A1():
    return render_template('A1.html')

@helpers_blueprint.route('/A2')
def A2():
    return render_template('A2.html')

@helpers_blueprint.route('/A3')
def A3():
    return render_template('A3.html')

@helpers_blueprint.route('/A4')
def A4():
    return render_template('A4.html')