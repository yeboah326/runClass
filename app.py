#! /usr/bin/env python

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import date

# -------------Custom-Imports-------------------

from classesDatabases import findClass
classNames = findClass.findClassNames('./classesDatabases')

from scripts import excelToDF
# -------------Custom-Imports-------------------


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


@app.route('/listClassesSession', methods=['POST', 'GET'])
def listClassesSession():
    return render_template("listClassesSession.html", today=today, classes=classNames)

# ------------------Random-Students--------------------------
@app.route('/randomComputerYear1', methods=['POST', 'GET'])
def listClassesSession1():
    return render_template("listStudentsRandom.html", today=today, currentClass=excelToDF.convertExcelToDataframe("./classesDatabases/Computer_Engineering_Year1.xlsx"))

@app.route('/randomComputerYear2', methods=['POST', 'GET'])
def listClassesSession2():
    return render_template("listStudentsRandom.html", today=today, currentClass=excelToDF.convertExcelToDataframe("./classesDatabases/Computer_Engineering_Year2.xlsx"))

@app.route('/randomComputerYear3', methods=['POST', 'GET'])
def listClassesSession3():
    return render_template("listStudentsRandom.html", today=today, currentClass=excelToDF.convertExcelToDataframe("./classesDatabases/Computer_Engineering_Year3.xlsx"))

@app.route('/randomComputerYear4', methods=['POST', 'GET'])
def listClassesSession4():
    return render_template("listClassesSession.html", today=today, currentClass=excelToDF.convertExcelToDataframe("./classesDatabases/Computer_Engineering_Year4.xlsx"))
# ------------------Random-Students--------------------------


@app.route('/listClassesRecords', methods=['POST', 'GET'])
def listClassesRecords():
    return render_template("listClassesRecords.html", today=today, classes=classNames)


@app.route('/records')
def records():
    return render_template('records.html', today=today)

@app.route('/listStudentsRandom')
def listStudentsRandom():
    return render_template('listStudentsRandom.html', today=today, classes=classNames)

@app.route('/complete')
def complete():
    render_template('complete.html' , today=today)


if __name__ == "__main__":
    # ---------Today's Date------------

    app.run(debug=True, use_reloader=True)