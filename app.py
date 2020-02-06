#! /usr/bin/env python

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import date


app = Flask(__name__)
# ------------------Database Configurations----------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class ProgrammeYear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    indexNumber = db.Column(db.Integer, nullable=False)
    studentName = db.Column(db.String(100), nullable=False)
    presentState = db.Column(db.Integer, nullable=False)

# ------------------Database Configurations----------------------

today = str(date.today())


# ------------------Application Routes-----------------------
@app.route('/')
def index():
    return render_template("index.html", today = today)


@app.route('/listClassesSession')
def listClassesSession():
    return render_template("listClassesSession.html", today=today)

@app.route('/listClassesRecords')
def listClassesRecords():
    return render_template("listClassesRecords.html", today=today)


@app.route('/records')
def records():
    return render_template('records.html', today=today)

@app.route('/listStudentsRandom')
def listStudentsRandom():
    return render_template('listStudentsRandom.html', today=today)

@app.route('/complete')
def complete():
    render_template('complete.html' , today=today)


if __name__ == "__main__":
    # ---------Today's Date------------

    app.run(debug=True, use_reloader=True)