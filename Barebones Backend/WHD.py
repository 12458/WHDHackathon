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
    else:
        return render_template("H0.html")

@app.route("/L0", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username=request.form["username"]
        password=request.form["pass"]
        #authentication for user goes here
        session["user"] = username
        exis_user_type = "elderly" 
        #change to "elderly" or "volunteer" as necessary
        if exis_user_type == "elderly":
            return redirect(url_for("choose_display"))
        if exis_user_type == "volunteer":
            return redirect(url_for("pick_an_elderly"))
        if exis_user_type == "volunteer":
            return redirect(url_for("dono"))
    else:
        if "user" in session:
            return redirect(url_for("choose_display"))
        return render_template("L0.html")
    
    
@app.route("/L3", methods=["POST", "GET"])
def new_user_type():
    if request.method == "POST":
        new_usr_type = request.form["user_type"]
        if new_usr_type == "elderly":
            return redirect(url_for("L"))
        elif new_usr_type == "volunteer":
            return redirect(url_for("L5"))       
    else:
        return render_template("L3.html")

@app.route("/L1")
def elderly_sign_up():
    
@app.route("/A1")
def pick_an_elderly():

@app.route("/A2")
def selected_grocery_address():

@app.route("/A3")
def thank_you():

@app.route("/B1")
def dono():

@app.route("/C1", methods=["POST", "GET"])
def choose_display():
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            disp_option = request.form["disp_option"]
            if disp_option == "logout":
                return redirect(url_for("logout"))
            elif disp_option == "browsing":
                return redirect(url_for("browsing"))
            elif disp_option == "no_browsing":
                return redirect(url_for("voice_order"))
        else: 
            return render_template("auth_test.html")
    else:
        return redirect(url_for("login"))



@app.route("/C2")
def grocery_shopping():

@app.route("/C3")
def order_and_checkout():

@app.route("/C4")
def order_tracking():

@app.route("/S1")
def supp():

@app.route("/acc", methods=["POST","GET"])
def request():
    if request.method == "POST":
        Name = request.form["nm"]
        Email = request.form["eml"]
        return redirect(url_for("C2"))


if __name__ == "__main__":
    app.run(debug=True)