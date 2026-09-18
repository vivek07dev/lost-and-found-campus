from flask import Flask, render_template, request
import sqlite3

from database import create_database

app = Flask(__name__)

create_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/lost")
def lost():
    return render_template("lost.html")


@app.route("/submit-lost", methods=["POST"])
def submit_lost():
    item_name = request.form["item_name"]
    category = request.form["category"]
    location = request.form["location"]
    date = request.form["date"]
    description = request.form["description"]
    contact = request.form["contact"]

    conn = sqlite3.connect("lost_found.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO items
        (item_name, category, location, date, description, contact, item_type)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        item_name,
        category,
        location,
        date,
        description,
        contact,
        "Lost"
    ))

    conn.commit()
    conn.close()

    return "Lost Item Successfully Submitted!"

@app.route("/lost-items")
def lost_items():
    conn = sqlite3.connect("lost_found.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items WHERE item_type = 'Lost'")
    items = cursor.fetchall()

    conn.close()

    return render_template("lost_items.html", items=items)


@app.route("/found")
def found():
    return render_template("found.html")


if __name__ == "_main_":
    app.run(debug=True)