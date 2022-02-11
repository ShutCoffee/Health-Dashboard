import csv
import pandas as pd
import numpy as np

header = []
rows = []
groupedTrainings = []
np_array = []

def parseFile():
    file = open('strong.csv')
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
    file.close()


def groupByTraining():
    groupedTrainings.append([rows[0]])
    for i in range(1, len(rows)):
        appended = False
        for training in groupedTrainings:
             if training[0][0] == rows[i][0]:
                training.append(rows[i])
                appended = True
        if(not appended):
            groupedTrainings.append([rows[i]])
    for training in groupedTrainings:
        for i in range(0,3):
            training.insert(i, training[i][i])
        for i in range(3, len(training)):
            del training[i][4]
            for j in range(0,3):
                del training[i][0]
            for h in range(0,5):
                del training[i][-1]


def main():
    parseFile()
    groupByTraining()
    print(groupedTrainings[-1])
    
    

main()



