import pandas
from sklearn.model_selection import *
from sklearn.linear_model  import *
from numpy import * 
def distance(x1 = 0,x2 = 0):
    """
    Arguments: [x1:(float) first position, x2:(float) second position]
    Return: The distance x1/x2
    """
    return abs(x1 - x2)
def main(file, k, age):
    csv = get_info(file)
    print(read_info(csv, csv.Age, age))
    return True
def get_info(file):
    return pandas.read_csv(file, sep = ',')
def read_info(csv, param, reference):
    closerID, closerDist,closerValue= csv.PassengerId[0], distance(param[0],reference),param[0]
    for i in range(len(param)):
        if(distance(param[i], reference) < closerDist):
            closerID, closerDist,closerValue= csv.PassengerId[i], distance(param[i],reference),param[i]
    return closerID,closerDist,closerValue
def read_infoStr(csv, param, reference):
    closerID, closerValue= csv.PassengerId[0], param[0]
    for i in range(len(param)):
        if(distance(param[i], reference) == closerDist):
            closerID, closerDist,closerValue= csv.PassengerId[i], distance(param[i],reference),param[i]
    return closerID,closerDist,closerValue
tab = pandas.read_csv("titanic.csv", sep = ',')
#tab = tab.values.tolist()
newtab = tab.loc[:,['PassengerId','Survived','Pclass','Sex','Age','Embarked']]
newtab.Age = newtab.Age.fillna(0)
for i in range(len(newtab)):
    if(newtab.Sex[i] == 'male'):
        newtab.Sex[i] = 0
    elif(newtab.Sex[i] == 'female'):
        newtab.Sex[i] = 1
    if(newtab.Embarked[i] == 'S'):
        newtab.Embarked[i] = 0
    elif(newtab.Embarked[i] == 'C'):
        newtab.Embarked[i] = 1
    elif(newtab.Embarked[i] == 'Q'):
        newtab.Embarked[i] = 2
    if(newtab.Age[i] == 0):
        for e in range(int(len(newtab)/2)):
            if(newtab.Age[i-e] != 0 and newtab.Age[i+e] != 0):
                newtab.Age[i] = int((newtab.Age[i-e] + newtab.Age[i+e])/2)
                break

print(newtab)
print(type(tab))
print(tab)

main("titanic.csv", 1, 94)