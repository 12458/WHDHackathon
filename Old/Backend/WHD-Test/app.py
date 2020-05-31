from myproject import app
from flask import render_template


@app.route('/')
def H0():
    return render_template('H0.html')


@app.route('/L0')
def L0():
    return render_template('L0.html')


@app.route('/L3')
def L3():
    return render_template('L3.html')


@app.route('/P1')
def P1():
    return render_template('P1.html')


@app.route('/S1')
def S1():
    return render_template('S1.html')


if __name__ == '__main__':
    app.run(debug=True)
