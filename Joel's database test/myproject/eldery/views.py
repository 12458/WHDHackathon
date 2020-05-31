from flask import Blueprint,render_template, url_for, redirect, request, session
from myproject import db
from myproject.models import Elderly,Grocery

from flask_bcrypt import Bcrypt
from hashlib import sha256
bcrypt = Bcrypt()
elderly_blueprints = Blueprint('elderly',__name__, template_folder='templates/elderly')

@elderly_blueprints.route('/L1',methods=['GET','POST'])
def elderly_sign_up():
    if request.method == "POST":
        full_name = request.form["full_name"]
        username = request.form["username"]
        password = request.form["pass"]
        pass_verify = request.form["pass_verify"]
        contact1 = request.form["contact1"]
        address = request.form["address"]
        area = request.form["area"]
        if sha256(pass_verify.encode()).hexdigest() == sha256(password.encode()).hexdigest(): # Check if SHA256 Hashes match 
            password = bcrypt.generate_password_hash(password=password)
            new_elderly = Elderly(full_name,username,password,contact1,address,area)
            db.session.add(new_elderly)
            db.session.commit()
            session["user"] = username
            user_type = "elderly"
            return redirect(url_for("elderly.groceries"))
        else:
            return render_template("L1.html")
    else:
        return render_template("L1.html")

@elderly_blueprints.route('/L4',methods=['GET','POST']) #done #Yuki connect this to HTML
def elderly_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["pass"]
        login_or_sign = request.form["login_or_sign"]
        if login_or_sign == "sign_up":
            return redirect(url_for("new_user_type"))
        elif login_or_sign == "submit":        
            Bleh = Elderly.query.filter_by(username=username).first()
            correct = Bleh.password
            check = bcrypt.check_password_hash(correct,password)
            if check:
                session["user"] = username
                return redirect(url_for("elderly.groceries")) #THIS ONE TO BE CHANGED IF DEF C2 is changed  
            else:
                return f"<h1>Invalid credentials</h1>"    
        else:
            return render_template("L4.html")
    else:
        return render_template("L4.html")


@elderly_blueprints.route('/C2',methods=['GET','POST'])
def groceries(): #DO NOT CHANGE THIS FUNCTION NAME WITHOUT CHANGING URL ABOVE
    if "user" in session:
        if request.method == "POST":
            purchases=request.form["order_box"] #note to faith, here is where the user's text input will be
            elderly = Elderly.query.filter_by(username= session["user"]).first()
            Elderlies_id = elderly.id # need help here - call when going through - Joel - Take out elderlies.id
            grocer = Grocery(purchases,Elderlies_id)
            db.session.add(grocer)
            db.session.commit()
            return redirect(url_for('elderly.order_checkout'))
        else:
            return render_template("C2.html")
    else:
        return redirect(url_for("home"))

@elderly_blueprints.route('/C3')
def order_checkout():
    if "user" in session:
        bleh = Elderly.query.filter_by(username=session["user"])
        groceies_ordered = bleh.groceries
        return render_template('C3.html')

@elderly_blueprints.route('/C4')
def C4():
    order_status = 'on the way'
    return render_template('C4.html') #Done as C4 already hardcoded 


