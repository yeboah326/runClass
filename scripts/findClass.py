import os
import re




def findClassNames(destinationDirectory):
    '''
    destinationDirectory - name of the directory that contains the records of the students

    findClassNames() - takes the directory as input and returns a dictionary of
    of all files ending in '.xlsx' 
    '''
    files = [f for f in os.listdir(destinationDirectory) if str(f).endswith('xlsx')]
    classes = []
    classDict = {}
    for _ in files:
        classes.append(list(re.sub('\.xlsx$', '', _).split("_")))
    for i in range(len(classes)):
        classDict[i] = {'name' : classes[i][0] + " " + classes[i][1], 'year' : classes[i][-1]} 
    
    return classDict



