from random import randint 

def generateRandom(n, numOfStudents):
    """
    n - Number of random numbers to be generated

    numOfStudents - NUmber of students in list
    
    """
    randomNumList =[]

    while len(randomNumList) < n:
        y = randint(0, numOfStudents - 1)
        if y not in randomNumList: randomNumList.append(y)

    return randomNumList