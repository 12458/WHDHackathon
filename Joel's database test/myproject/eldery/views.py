from flask import Blueprint,render_template, url_for, redirect, request, session
from myproject import db
from myproject.models import Elderly,Grocery
from myproject.eldery.forms import FL1,FC2

elderly_blueprints = Blueprint('elderly',__name__, template_folder='templates/elderly')

@elderly_blueprints.route('/L1',methods=['GET','POST'])
def elderly_sign_up():
    if request.method == "POST":
        full_name = request.form["full_name"]
        email = request.form["email"]
        password = request.form["pass"]
        pass_verify = request.form["pass_verify"]
        contact1 = request.form["contact1"]
        address = request.form["address"]
        area = request.form["area"]
        if pass_verify == password:
            new_elderly = Elderly(full_name,email,password,contact1,address,area)
            db.session.add(new_elderly)
            db.session.commit()
            session["user"] = name
            user_type = "elderly"
            return redirect(url_for("choose_display"))
        else:
            return render_template("L1.html")
    else:
        return render_template("L1.html")

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



