import os
import shutil

def moveClass(filename):
    '''
    
    filename - name of the file to be moved

    moveClass() - takes the filename of a file and moves it to the records directory
    
    '''
    currentPath = './' + filename
    destination = './records'
    shutil.move(currentPath, destination)



