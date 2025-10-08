from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "I like to live dangerously"

app.run(host="0.0.0.0", port=80)