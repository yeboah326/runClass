import pandas as pd
from randomNumberGenerator import generateRandom as gr
# from scripts import randomNumberGenerator as rng

m = gr(15, 30)
print(m)

def convertExcelToDataframe(xlsxFileDirectory: str):
    xlsx_file = pd.ExcelFile(xlsxFileDirectory)
    return xlsx_file.parse(xlsx_file.sheet_names[0])

df = convertExcelToDataframe("../ClassList.xlsx")
print(df.loc[m ,['STUDENT NAME','INDEX NO.']])    
