import pandas as pd
from scripts import randomNumberGenerator as rng
# import randomNumberGenerator as rng

m = rng.generateRandom(15, 30)
# print(m)

def convertExcelToDataframe(xlsxFileDirectory: str):
    xlsx_file = pd.ExcelFile(xlsxFileDirectory)
    df = xlsx_file.parse(xlsx_file.sheet_names[0])
    temp = df.loc[m ,['STUDENT NAME']]
    newDict = temp.to_dict()
    for i in newDict.values():
        return i
    # return newDict.values()
    # return xlsx_file.parse(xlsx_file.sheet_names[0])
def returnIndex(classDict):
    unfortunatePeople = []
    for key,value in classDict.items():
        unfortunatePeople.append(key)
    return unfortunatePeople
# ndf = convertExcelToDataframe("../classesDatabases/Computer_Engineering_Year1.xlsx")
# print(ndf)
# for i in ndf.values():
#     print(i)
# print(df.loc[m ,['STUDENT NAME']])    
