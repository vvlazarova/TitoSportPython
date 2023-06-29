from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html" , login=False)

@app.route("/athletes")
def athletes():
    return render_template("athletes.html")

@app.route("/training")
def training():
    return render_template("training.html")

@app.route("/junior")
def junior():
    return render_template("junior.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html" )

