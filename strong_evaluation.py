import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

header = []
rows = []
groupedTrainings = []
np_array = []
df = []

def parseFile():
    file = open('strong.csv')
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
    file.close()


def organizeArray():
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
        training[0] = pd.to_datetime(training[0])
        training[3:] = [training[3:]]

def groupByMonth(df):
    return df.groupby([df['date'].dt.year.rename('year'), df['date'].dt.month.rename('month')]).agg({'count'}).iloc[:,2]

def groupByMuscleGroup(df):
    return df.groupby(['musclegroup']).count()




def main():
    parseFile()
    organizeArray()
    np_array = np.array(groupedTrainings, dtype=object)
    df = pd.DataFrame(np_array, columns = ['date', 'musclegroup', 'duration', 'sets'])
    groupedByMonths = groupByMonth(df)
    groupedByMuscleGroup = groupByMuscleGroup(df)
    groupedByMonths.plot(kind='bar')
    plt.show()
    groupedByMuscleGroup.plot.pie(y='date')
    plt.show()

    print(groupedByMonths)
    



main()



