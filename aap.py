from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Lost and Found Campus"

if __name__ == "__main__":
    app.run(debug=True)