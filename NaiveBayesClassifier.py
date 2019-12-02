import csv
import os
import sys

columnDict = dict()
resultDict = dict()
columnOrder = []

class Statics:
    def __init__(self, val):
        self.Yes = 0
        self.No = 0
        if val == RESULT_YES:
            self.Yes = 1
        elif val == RESULT_NO:
            self.No = 1

    def add(self, val):
        if val == RESULT_YES:
            self.Yes = self.Yes + 1
        elif val == RESULT_NO:
            self.No = self.No + 1

    def getPYes(self):
        if resultDict[RESULT_YES] > 0:
            return self.Yes / resultDict[RESULT_YES]
        else:
            return 0

    def getPNo(self):
        if resultDict[RESULT_NO] > 0:
            return self.No / resultDict[RESULT_NO]
        else:
            return 0

def read_csv(resultColumnName):
    with open('test_data.csv') as csvfile:
        dictReader = csv.DictReader(csvfile, delimiter=',')
        executeFirstTime = True
        for row in dictReader:
        #    print(row)
            columnsName = row.keys()
         #   print(columnsName)
            for columnName in columnsName:
                if executeFirstTime:
                    columnDict[columnName] = dict()
                
                if columnName == resultColumnName:
                    if row[columnName] in resultDict:
                        resultDict[row[columnName]] =  resultDict[row[columnName]] + 1
                    else:
                        resultDict[row[columnName]] = 1
                else:
                    if executeFirstTime:
                        columnOrder.append(columnName)
                    if row[columnName] in columnDict[columnName]:
                        columnDict[columnName][row[columnName]].add(row[resultColumnName])
                    else:
                        columnDict[columnName][row[columnName]] = Statics(row[resultColumnName])
            executeFirstTime = False

def today(argu):
    pYesToday = 1
    pNoToday = 1
    count = 0
    try:
        for arg in argu:
            pYesToday = pYesToday * columnDict[columnOrder[count]][arg].getPYes()
            pNoToday = pNoToday * columnDict[columnOrder[count]][arg].getPNo()
            count = count + 1
    except:
        print("Invalid arguments passed")
        return

    pYesToday = pYesToday * (resultDict[RESULT_YES]/(resultDict[RESULT_YES]+resultDict[RESULT_NO]))
    pNoToday = pNoToday * (resultDict[RESULT_NO]/(resultDict[RESULT_YES]+resultDict[RESULT_NO]))
    #print('Prob Yes: '+str(pYesToday)+' Prob No: '+str(pNoToday))
    # print(ss)
    probYesToday = pYesToday/(pYesToday + pNoToday)
    probNoToday = pNoToday/(pYesToday + pNoToday)
    print('Prob Yes: '+str(probYesToday)+' Prob No: '+str(probNoToday))
    if probYesToday > probNoToday:
        print('So, prediction that golf would be played is = Yes.')
    else:
        print('So, prediction that golf would be played is = No.')


def readInput():
    text = input(
        "Enter outlook, temperature,humidity,wind with comma seperator: ")
    arr = text.split(",")
    return arr


# start---------
RESULT_YES = 'Yes'
RESULT_NO = 'No'
RESULT_COLUMN_NAME = 'Play'
read_csv(RESULT_COLUMN_NAME)
# print(playDict['Yes']/(playDict['Yes']+playDict['No']))
# testdata = readInput()
# today(testdata[0],testdata[1],testdata[2],testdata[3])
testdata = readInput()
today(testdata)
