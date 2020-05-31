from flask import Blueprint,render_template, url_for, redirect, request, session
from myproject import db
from myproject.models import Elderly,Grocery,Helper

from flask_bcrypt import Bcrypt


bycrypt = Bcrypt()
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
                password = bycrypt.generate_password_hash(password=password)
                new_helper = Helper(full_name,username,password,contact1,area,address)
                db.session.add(new_helper)
                db.session.commit()
                session["user"] = username
                user_type = "volunteer"
                return redirect(url_for("pick_an_elderly"))
            else:
                return render_template("L2.html")
        else:
            return render_template("L2.html")

@helpers_blueprint.route('/L5') #connect HTML plz
def L5():
    if request.method == "POST":
            username = request.form["username"]
            password = request.form["pass"]
            Bleh = Helper.query.filter_by(username=username)
            correct = Bleh.password
            check = bcrypt.check_password_hash(correct,password)
            if check:
                return redirect(url_for("pick_an_elderly"))
            else:
                return render_template("L5.html")
    return render_template('L5.html')

@helpers_blueprint.route('/A1')
def pick_an_elderly():
    if "user" in session:
        elderly_data  = Elderly.query.all()
        name_list = elderly_data.full_name
        area_list = elderly_data.area
        if request.method == "POST":
            selected_elderly = request.form["elderly_selection"]
            selected_elderly_data= Elderly.query.filter_by(username=selected_elderly)
            selected_elderly.helper = session['user']

                        
    else:          
        return render_template('A1.html')

@helpers_blueprint.route('/A2')
def A2():
    return render_template('A2.html')

@helpers_blueprint.route('/A3')
def A3():    
    return render_template('A3.html')

