from flask import Flask,render_template, request 
import sqlite3

from database import create_database

app = Flask(__name__)
create_database

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lost")
def lost():
    return render_template("lost.html")


@app.route("/submit-lost",methods=["POST"])
def submit_lost():


@app.route("/found")
def found():
    return render_template("found.html")


if __name__ == "__main__":
    app.run(debug=True)

