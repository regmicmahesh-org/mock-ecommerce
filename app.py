from flask import Flask, render_template


import os
from utils import retry


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buy/<id>')
def buy(id):
    return render_template("item.html")


if __name__ == "__main__":
    app.run()
