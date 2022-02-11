import csv

header = []
rows = []
groupedTrainings = []

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

def main():
    parseFile()
    groupByTraining()
    
    

main()



