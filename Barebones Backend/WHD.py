from flask import Flask, render_template, url_for, redirect, request, session

app = Flask(__name__)
app.secret_key="Greetings"

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        exis_check=request.form["exis_check"]
        if exis_check == "exis_user":
            return redirect(url_for("login"))
        elif exis_check == "new_user":
            return redirect(url_for("new_user_type"))
    else:
        return render_template("H0.html")

@app.route("/L0", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username=request.form["username"]
        password=request.form["pass"]
        login_or_signup=request.form["submit"]
<<<<<<< Updated upstream
        if len(username)>2 & len(password)>2:
=======
        if login_or_signup == "submit":
>>>>>>> Stashed changes
            #authentication for user goes here
            session["user"] = username
            exis_user_type = "elderly" 
            #change to "elderly" or "volunteer" as necessary
            if exis_user_type == "elderly":
                return redirect(url_for("choose_display"))
<<<<<<< Updated upstream
            if exis_user_type == "volunteer":
                return redirect(url_for("pick_an_elderly"))
            if exis_user_type == "dono":
=======
            elif exis_user_type == "volunteer":
                return redirect(url_for("pick_an_elderly"))
            elif exis_user_type == "dono":
>>>>>>> Stashed changes
                return redirect(url_for("dono"))
        if login_or_signup == "new_user":
            return redirect(url_for("new_user_type"))
    else:
        if "user" in session:
            return redirect(url_for("choose_display"))
        return render_template("L0.html")
    
    
@app.route("/L3", methods=["POST", "GET"])
def new_user_type():
    if request.method == "POST":
        new_usr_type = request.form["user_type"]
        if new_usr_type == "elderly":
            return redirect(url_for("elderly_sign_up"))
        elif new_usr_type == "volunteer":
            return redirect(url_for("volunteer_sign_up"))
        elif new_usr_type == "dono":
            return redirect(url_for("dono"))       
    else:
        return render_template("L3.html")

@app.route("/L1", methods=["POST", "GET"])
def elderly_sign_up():
    if request.method == "POST":
        full_name = request.form["full_name"]
        username = request.form["username"]
        password = request.form["pass"]
        pass_verify = request.form["pass_verify"]
        contact1 = request.form["contact1"]
        contact2 = request.form["contact2"]
        email = request.form["email"]
        address = request.form["address"]
        if pass_verify == password:
            session["user"] = username
            user_type = "elderly"
            return redirect(url_for("choose_display"))
        else:
            return render_template("L1.html")
    else:
        return render_template("L1.html")


@app.route("/L2", methods=["POST", "GET"])
def volunteer_sign_up():
        if request.method == "POST":
            full_name = request.form["full_name"]
            username = request.form["username"]
            password = request.form["pass"]
            pass_verify = request.form["pass_verify"]
            contact1 = request.form["contact1"]
<<<<<<< Updated upstream
            contact2 = request.form["contact2"]
            email = request.form["email"]
=======
            area = request.form["area"]
>>>>>>> Stashed changes
            address = request.form["address"]
            if pass_verify == password:
                session["user"] = username
                user_type = "volunteer"
                return redirect(url_for("pick_an_elderly"))
            else:
                return render_template("L2.html")
        else:
            return render_template("L2.html")

    
@app.route("/A1")
def pick_an_elderly():
    pass
    
@app.route("/A2")
def selected_grocery_address():
    pass

@app.route("/A3")
def thank_you():
    pass

@app.route("/B1")
def dono():
    return render_template("B1.html")

@app.route("/C1", methods=["POST", "GET"])
def choose_display():
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            disp_option = request.form["disp_option"]
            if disp_option == "logout":
                return redirect(url_for("logout"))
            elif disp_option == "browsing":
<<<<<<< Updated upstream
                return redirect(url_for("browsing"))
=======
                return redirect(url_for("grocery_shopping"))
>>>>>>> Stashed changes
            elif disp_option == "no_browsing":
                return redirect(url_for("voice_order"))
        else: 
            return render_template("C1.html")
    else:
<<<<<<< Updated upstream
        return redirect(url_for("login"))


@app.route("/C2")
def grocery_shopping():
    pass

=======
        return redirect(url_for("home"))


@app.route("/C2a")
def grocery_shopping():
    pass

@app.route("/C2b")
def voice_order():
    pass

>>>>>>> Stashed changes
@app.route("/C3")
def order_and_checkout():
    pass

@app.route("/C4")
def order_tracking():
    pass

@app.route("/S1")
def supp():
    pass

@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.pop("user", None)
<<<<<<< Updated upstream
    return redirect(url_for("login"))
=======
    return redirect(url_for("home"))
>>>>>>> Stashed changes

if __name__ == "__main__":
    app.run(debug=True)