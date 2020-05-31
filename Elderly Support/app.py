from myproject import app
from flask import Flask, render_template, url_for, redirect, request, session
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        exis_check=request.form["exis_check"]
        if exis_check == "exis_user":
            return redirect(url_for("login_user_type"))
        elif exis_check == "new_user":
            return redirect(url_for("new_user_type"))
    else:
        return render_template("H0.html")

@app.route('/L0', methods=["POST", "GET"])
def login_user_type():
    if request.method == "POST":
        exis_user_type=request.form["exis_user_type"]
        if exis_user_type == "exis_elderly":
            return redirect(url_for("elderly.elderly_login"))
        elif exis_user_type == "exis_volunteer":
            return redirect(url_for("helpers.volunteer_login"))
        elif exis_user_type == "dono":
            return redirect(url_for("dono"))
        else:
            return render_template("L0.html")
    else:
        return render_template("L0.html")

@app.route('/L3', methods=["POST", "GET"])
def new_user_type():
    if request.method == "POST":
        new_usr_type = request.form["user_type"]
        if new_usr_type == "elderly":
            return redirect(url_for("elderly.elderly_sign_up"))
        elif new_usr_type == "volunteer":
            return redirect(url_for("helpers.volunteer_sign_up"))
        elif new_usr_type == "dono":
            return redirect(url_for("dono"))       
    else:
        return render_template("L3.html")

@app.route('/P1', methods=["POST", "GET"])
def P1():
    return render_template('P1.html')



@app.route('/S1')
def S1():
    return render_template('S1.html')

@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
