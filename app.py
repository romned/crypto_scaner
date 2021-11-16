from flask import Flask, render_template
from patterns import patterns
app = Flask(__name__)

@app.route("/")
def hello_rom():
    return render_template("index.html", patterns=patterns)


@app.route("/second")
def second():
    return {
        'code': 'second'
    }
