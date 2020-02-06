#! /usr/bin/env python

from flask import Flask, render_template
from datetime import date


app = Flask(__name__)
today = str(date.today())

@app.route('/')

def index():
    return render_template("list2.html", today = today)


if __name__ == "__main__":
    # ---------Today's Date------------

    app.run(debug=True, use_reloader=True)