# ----------------Libraries-To-Be-Imported-------------------------
import pandas as pd
from scripts import randomNumberGenerator as rng
# import randomNumberGenerator as rng
'''
randomNumberGenerator is imported twice. The first instance on Line[3]
and this is for external scripts. The second on Line[4] which for testing
within the found in which this script is found
'''
# ----------------Libraries-To-Be-Imported-------------------------


# Generating random numbers for the students
m = rng.generateRandom(15, 30)
# print(m)

def convertExcelToDataframe(xlsxFileDirectory: str):
    '''
    xlsxFileDirectory - This is the directory for the excel spreadsheet
    containing the students record

    convertExcelToDataframe() - takes the directory of the excel spreadsheet
    as input and returns a pandas dataframe
    '''
    xlsx_file = pd.ExcelFile(xlsxFileDirectory)
    df = xlsx_file.parse(xlsx_file.sheet_names[0])
    return df

def randomStdList(dataframe, random):
    '''
    dataframe - pandas dataframe which contains the names, index numbers
    and (present state) of the students in the class

    random - a list of random numbers generated

    randomStdList() - takes a dataframe and a list of random numbers as input
    and returns a dictionary which contains the names of the students found
    at (random) indexes
    '''
    temp = dataframe.loc[random ,['STUDENT NAME']]
    newDict = temp.to_dict()
    for i in newDict.values():
        return i
    # return newDict.values()
    # return xlsx_file.parse(xlsx_file.sheet_names[0])

def returnRandomStdDF(dataframe, randomNumbers):
    '''
    dataframe - pandas dataframe which contains the names, index numbers
    and (present state) of the students in the class

    randomNumbers - a list of random numbers generated

    returnRandomStdDF() - takes a dataframe and a list of random numbers as input
    and returns a datafame which contains the names, index numbers and
    present state of the students found at (randomNumbers) indexes
    '''
    return dataframe.loc[randomNumbers, ['STUDENT NAME','INDEX NO.','PRESENT STATE']]

def returnIndex(classDict):
    '''
    classDict - a dictionary which contains indexes as key and student names
    as values

    returnIndex() - takes a dictionary as input and returns a list of the keys
    '''
    unfortunatePeople = []
    for key,value in classDict.items():
        unfortunatePeople.append(key)
    return unfortunatePeople

def markStudents(dataframe, presentStudents):
    '''
    dataframe - pandas dataframe representing the random students with
    all their present states set to 0

    presentStudents - a list of students who have been marked present

    markStudents() - takes a dataframe and list containing the students
    who were marked present
    '''
    for i in presentStudents:
        dataframe.loc[[i], ['PRESENT STATE']] = 1


def convertDFToExcel2(filename, dataframe):
    '''
    filename(str) - name of the excel spreadsheet to be created

    dataframe - pandas dataframe to be converted to an excel spreadsheet
    '''
    writer = pd.ExcelWriter(filename)
    dataframe.to_excel(writer, 'attendance')
    writer.save()


# ndf = convertExcelToDataframe("../classesDatabases/Computer_Engineering_Year1.xlsx")
# print(ndf)
# for i in ndf:
#     print(i)
# print(ndf.loc[m ,['STUDENT NAME', 'PRESENT STATE']])
# ndf.loc[[4], ['PRESENT STATE']] = 1    
# print(ndf.loc[[4], ['STUDENT NAME','INDEX NO.','PRESENT STATE']])
