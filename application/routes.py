from application import app, db
from flask import render_template,json, Response,request, redirect, flash, url_for, session
from application.models import User
from application.forms import LoginForm, RegisterForm
from pymongo import MongoClient


# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')

# Access  database
db = client['Users']

# Access collection
collection = db['user']



@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html" , index=True)

@app.route("/athletes")
def athletes():
    return render_template("athletes.html", athletes=True)

@app.route("/welcome")
def welcome ():
    return render_template("welcome.html", athletes=True)

@app.route("/training")
def training():
    return render_template("training.html", training=True)

@app.route("/junior")
def junior():
    return render_template("junior.html", junior=True)

@app.route("/about")
def about():
    return render_template("about.html", junior=True)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect(url_for('user'))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Check if the email exists in the collection
        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            session['user_id'] = str(user.user_id)
            session['username'] = user.first_name
            return redirect(url_for('user'))  # Redirect to the 'user' route
        else:
            flash("Sorry, something went wrong.", "danger")
    return render_template("login.html", title="Login", form=form, login=True)

@app.route("/user")
def user():
    if not session.get('username'):
        return redirect(url_for('login'))
    
    if 'username' in session:
        flash(session['username'] + ", you are successfully logged in!", "success")
        user_id = session['user_id']
        user = User.objects(user_id=user_id).first()
        if user:
            return render_template("user.html", user=user)
        else:
            flash("User not found.", "danger")
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))



@app.route("/logout")
def logout():
    session['user_id']=False
    session.pop('username',None)
    return redirect(url_for('index'))


@app.route("/register", methods=['POST','GET'])
def register():
    if session.get('username'):
        return redirect(url_for('user'))
    form = RegisterForm()
    if form.validate_on_submit():
        user_id     = User.objects.count()
        user_id     += 1

        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data

        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You are successfully registered!","success")
        return redirect(url_for('welcome'))
    return render_template("register.html", title="Register", form=form, register=True)



# Route for testing MongoDB connection
@app.route("/test-db")
def test_mongodb():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017')

    # Access the database
    db = client['Users']

    # Access a collection
    collection = db['user']

    # Test the connection
    documents = collection.find()
    output = ""
    for document in documents:
        output += str(document) + "<br>"

    return output

# Your other Flask routes and code can follow

# Run the Flask application
if __name__ == "__main__":
    app.run()




    











   