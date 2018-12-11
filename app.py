from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("Main Page.html")


@app.route("/Login Page")
def loginpage():
    return render_template("Login_Page.html")


@app.route("/Register Page")
def registerpage():
    return render_template("Register.html")


@app.route("/Reminder Page")
def reminderpage():
    return render_template("Reminder page.html")


@app.route("/CCTV")
def cctv():
    return render_template("CCTV.html")


@app.route("/CCTV_1")
def cctv1():
    return render_template("CCTV_1.html")


@app.route("/CCTV_2")
def cctv2():
    return render_template("CCTV_2.html")


@app.route("/CCTV_3")
def cctv3():
    return render_template("CCTV_3.html")

@app.route("/CCTV_4")
def cctv4():
    return render_template("CCTV_4.html")

@app.route("/Aircon")
def aircon():
    return render_template("AirconDesign.html")

@app.route("/Lighting")
def lighting():
    return render_template("Lighting-control.html")

@app.route('/')
def index():
    return render_template('tracker.html')

@app.route('/items')
def items():
    return render_template('items.html')

@app.route('/history')
def history():
    return render_template('history.html')



if __name__ == "__main__":
    app.run()

