from application import app, db
from flask import render_template
from application.models import User
@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html" , index=True)

@app.route("/athletes")
def athletes():
    return render_template("athletes.html", athletes=True)

@app.route("/training")
def training():
    return render_template("training.html", training=True)

@app.route("/junior")
def junior():
    return render_template("junior.html", junior=True)

@app.route("/about/")
def about():
    return render_template("about.html", about=True)

@app.route("/login")
def login():
    return render_template("login.html", login=True )


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    
    return Response(json.dumps(jdata), mimetype="application/json")

@app.route("/user")
def user():
     #User(user_id=1, first_name="Stoil", last_name="Panchev", email="tito@gmail.vom", password="pass123").save()
     #User(user_id=2, first_name="vlazarova", last_name="Lazarova", email="vlazarova@gmail.com", password="pass456").save()
     users = User.objects.all()
     return render_template("user.html", users=users)
