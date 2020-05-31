from flask import Blueprint,render_template, url_for, redirect, request, session
from myproject import db
from myproject.models import Elderly,Grocery,Helper
from myproject.helpers.forms import FL2

helpers_blueprint = Blueprint('helpers',__name__,template_folder='template/helpers')


@helpers_blueprint.route('/L2',methods= ['GET','POST'])
def volunteer_sign_up(): #Helper Sign up
        if request.method == "POST":
            full_name = request.form["full_name"]
            username = request.form["username"]
            password = request.form["pass"]
            pass_verify = request.form["pass_verify"]
            contact1 = request.form["contact1"]
            area = request.form["area"]
            address = request.form["address"]
            if pass_verify == password:
                db.session.add_all([full_name,username,password,contact1,address])
                db.session.commit()
                session["user"] = username
                user_type = "volunteer"
                return redirect(url_for("pick_an_elderly"))
            else:
                return render_template("L2.html")
        else:
            return render_template("L2.html")

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