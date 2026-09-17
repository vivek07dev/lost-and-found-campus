from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lost")
def lost():
    return render_template("lost.html")

@app.route("/found")
def found():
    return render_template("found.html")


if __name__ == "__main__":
    app.run(debug=True)