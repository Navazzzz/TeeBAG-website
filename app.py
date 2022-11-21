from flask import Flask, render_template, redirect, request, session
from cs50 import SQL


# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///info.db")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/submit", methods=["POST"])
def submit():
    if not request.form.get("name") or not request.form.get("email") or request.form.get("genre") not in ["Horror", "Murder-Mystery", "Fantasy", "Other"]:
        return render_template("nope.html")
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        genre = request.form.get("genre")

        db.execute("INSERT INTO submit (emails, names, genres) VALUES (?, ?, ?)", email, name, genre)
        return render_template("yep.html")

@app.route("/request", methods=["POST"])
def requestus():
    if not request.form.get("namer") or not request.form.get("emailr") or request.form.get("genrer") not in ["Horror", "Murder-Mystery", "Fantasy", "Other"]:
        return render_template("nope.html")
    else:
        namer = request.form.get("namer")
        emailr = request.form.get("emailr")
        genrer = request.form.get("genrer")

        db.execute("INSERT INTO request (emailr, namer, genrer) VALUES (?, ?, ?)", emailr, namer, genrer)
        return render_template("yep.html")

@app.route("/list")
def list():
    return render_template("list.html")

@app.route("/tryout")
def tryout():
    return render_template("tryout.html")

@app.route("/creator")
def creator():
    return render_template("creator.html")

@app.route("/login", methods=["POST"])
def login():
    usern = db.execute("SELECT user FROM creators")
    passw = db.execute("SELECT pass FROM creators")

    if not request.form.get("user") or not request.form.get("pass"):
        return render_template("nope.html")

    return redirect("/logins")

@app.route("/logins")
def logins():

    submitdb = db.execute("SELECT * FROM submit")
    requestdb = db.execute("SELECT * FROM request")
    return render_template("login.html", databases = submitdb, databaser = requestdb)
