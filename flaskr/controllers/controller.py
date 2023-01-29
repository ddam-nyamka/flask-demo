from flask import redirect, render_template, request, url_for

from flaskr import app


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>Hello {usr}</>"


@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html")
