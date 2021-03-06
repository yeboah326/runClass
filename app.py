#! /usr/bin/env python

from flask import Flask, render_template, request, send_from_directory, send_file
from flask_sqlalchemy import SQLAlchemy

# -------------Custom-Imports-------------------

from datetime import date, datetime

from scripts import excelToDF, moveClass, findClass, downloadFile, deleteRecord
from scripts import randomNumberGenerator as rng

classNames = findClass.findClassNames('./classesDatabases')
# -------------Custom-Imports-------------------

# -------------Custom-Variables-----------------
computerFirstYearRecord = 0
computerSecondYearRecord = 0
computerThirdYearRecord = 0
computerFourthYearRecord = 0

currentYear = ""
# -------------Custom-Variables-----------------

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
    global computerFirstYearRecord
    global currentYear

    currentClass = excelToDF.convertExcelToDataframe("./classesDatabases/Computer_Engineering_Year1.xlsx")
    random = rng.generateRandom(15, len(currentClass))
    computerFirstYearRecord = excelToDF.returnRandomStdDF(currentClass, random)
    randomStudentList = excelToDF.randomStdList(currentClass, random)
    currentYear="Year1"
    return render_template(
        "listStudentsRandom.html", 
        today=today, 
        currentClass=randomStudentList, 
        year="Year1",
        selectedStudents=excelToDF.returnIndex(currentClass))

@app.route('/randomComputerYear2', methods=['POST', 'GET'])
def listClassesSession2():
    global computerSecondYearRecord
    global currentYear

    currentClass = excelToDF.convertExcelToDataframe("./classesDatabases/Computer_Engineering_Year2.xlsx")
    random = rng.generateRandom(15, len(currentClass))
    computerSecondYearRecord = excelToDF.returnRandomStdDF(currentClass, random)
    randomStudentList = excelToDF.randomStdList(currentClass, random)
    currentYear = "Year2"
    return render_template(
        "listStudentsRandom.html", 
        today=today, 
        currentClass=randomStudentList, 
        year="Year2",
        selectedStudents=excelToDF.returnIndex(currentClass))

@app.route('/randomComputerYear3', methods=['POST', 'GET'])
def listClassesSession3():
    global computerThirdYearRecord
    global currentYear

    currentClass = excelToDF.convertExcelToDataframe("./classesDatabases/Computer_Engineering_Year3.xlsx") 
    random = rng.generateRandom(15, len(currentClass))
    computerThirdYearRecord = excelToDF.returnRandomStdDF(currentClass, random)
    randomStudentList = excelToDF.randomStdList(currentClass, random)
    currentYear ="Year3"
    return render_template(
        "listStudentsRandom.html", 
        today=today, 
        currentClass=randomStudentList, 
        year="Year3",
        selectedStudents=excelToDF.returnIndex(currentClass))

@app.route('/randomComputerYear4', methods=['POST', 'GET'])
def listClassesSession4():
    global computerFourthYearRecord
    global currentYear

    currentClass = excelToDF.convertExcelToDataframe("./classesDatabases/Computer_Engineering_Year4.xlsx")
    random = rng.generateRandom(15, len(currentClass))
    computerFourthYearRecord = excelToDF.returnRandomStdDF(currentClass, random)
    randomStudentList = excelToDF.randomStdList(currentClass, random)
    currentYear = "Year4"
    return render_template(
        "listStudentsRandom.html", 
        today=today, 
        currentClass=randomStudentList, 
        year="Year4",
        selectedStudents=excelToDF.returnIndex(currentClass))
# ------------------Random-Students--------------------------

# ---------------------Records-------------------------------
@app.route('/listClassesRecords', methods=['POST', 'GET'])
def listClassesRecords():
    classRecords = findClass.findRecords('./records')
    return render_template("listClassesRecords.html", today=today, records=classRecords)

@app.route('/deleteClassesRecords')
def deleteClassesRecords():
    classRecords = findClass.findRecords('./records')
    return render_template("deleteClassesRecords.html", today=today, records=classRecords)

@app.route('/download/<string:filename>', methods=['GET', 'POST'])
def downloadFileFromServer(filename):
    filename = './records/' + filename
    # path = './records/ComputerEngineeringYear2-2020-02-12-13:26.xlsx'
    return send_file( filename, as_attachment=True)

    # return send_file( path, as_attachment=True)
@app.route('/<string:filename>',methods=['GET', 'POST'])
def removeFileFromServer(filename):
    filename = './records/' + filename
    deleteRecord.deleteFile(filename)
    return render_template('complete.html', today=today )
# ---------------------Records-------------------------------

@app.route('/recordsPage')
def records():
    return render_template('records.html', today=today)



@app.route('/listStudentsRandom')
def listStudentsRandom():
    return render_template('listStudentsRandom.html', today=today, classes=classNames)

# ----------------------Complete-Page-Route-----------------------------
@app.route('/complete', methods=['POST', 'GET'])
def complete():
    
    if request.method == 'POST':
        presentStudents = request.form.getlist("student")
        presentStudents = list(map(lambda x: int(x), presentStudents))
        if currentYear == 'Year1':
            excelToDF.markStudents(computerFirstYearRecord, presentStudents)
            filename = 'ComputerEngineeringYear1' + '-' + str(today) + '-' + str(datetime.now())[11:16] + '.xlsx'
            excelToDF.convertDFToExcel2(filename, computerFirstYearRecord)
            moveClass.moveClass(filename)
        elif currentYear == 'Year2':
            excelToDF.markStudents(computerSecondYearRecord, presentStudents)
            filename = 'ComputerEngineeringYear2' + '-' + str(today) + '-' + str(datetime.now())[11:16] + '.xlsx'
            excelToDF.convertDFToExcel2(filename, computerSecondYearRecord)
            moveClass.moveClass(filename)
        elif currentYear == 'Year3':
            excelToDF.markStudents(computerThirdYearRecord, presentStudents)
            filename = 'ComputerEngineeringYear3' + '-' + str(today) + '-' + str(datetime.now())[11:16] + '.xlsx'
            excelToDF.convertDFToExcel2(filename, computerThirdYearRecord)
            moveClass.moveClass(filename)
        elif currentYear == 'Year4':
            excelToDF.markStudents(computerFourthYearRecord, presentStudents)
            filename = 'ComputerEngineeringYear4' + '-' + str(today) + '-' + str(datetime.now())[11:16] + '.xlsx'
            excelToDF.convertDFToExcel2(filename, computerFourthYearRecord)
            moveClass.moveClass(filename)
        return render_template('complete.html', today=today)
    else:
        return render_template('index.html' , today=today)
        
# ----------------------Complete-Page-Route-----------------------------


if __name__ == "__main__":
    # ---------Today's Date------------

    app.run(debug=True, use_reloader=True)