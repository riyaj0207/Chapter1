import flask
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    return "hello"
app.run()