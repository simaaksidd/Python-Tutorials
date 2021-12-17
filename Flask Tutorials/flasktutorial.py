#This file is a combination of code for the purpose of showing what flask can do. DO NOT USE THIS FILE. Use flaskhtml.py for a comprehensible website.
from flask import Flask, redirect, url_for

app = Flask(__name__)
a = True

@app.route("/")
def home():
    return "<h1>Hello!</h1> This is the main page"

@app.route("/<name>")
def user(name):
    return F"Hello {name}!"

@app.route("/admin/")
def admin():
    if a:
        return redirect(url_for("user", name="Admin!"))
if __name__ == "__main__":
    app.run()
