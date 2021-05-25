import pandas
from sklearn.model_selection import *
from sklearn.linear_model import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()


def distance(x1=0, x2=0):
    """
    Arguments: [x1:(float) first position, x2:(float) second position]
    Return: The distance x1/x2
    """
    return abs(x1 - x2)


def main(file, k, age):
    """

    :param file:
    :param k:
    :param age:
    :return:
    """
    csv = get_info(file)
    print(read_info(csv, csv.Age, age))
    return True


def get_info(file):
    """

    :param file:
    :return:
    """
    return pandas.read_csv(file, sep=',')


def read_info(csv, param, reference):
    """

    :param csv:
    :param param:
    :param reference:
    :return:
    """
    closerID, closerDist, closerValue = csv.PassengerId[0], distance(param[0], reference), param[0]
    for i in range(len(param)):
        if (distance(param[i], reference) < closerDist):
            closerID, closerDist, closerValue = csv.PassengerId[i], distance(param[i], reference), param[i]
    return closerID, closerDist, closerValue


def read_infoStr(csv, param, reference):
    """

    :param csv:
    :param param:
    :param reference:
    :return:
    """
    closerID, closerValue = csv.PassengerId[0], param[0]
    for i in range(len(param)):
        if (distance(param[i], reference) == closerDist):
            closerID, closerDist, closerValue = csv.PassengerId[i], distance(param[i], reference), param[i]
    return closerID, closerDist, closerValue


tab = pandas.read_csv("titanic.csv", sep=',')
# tab = tab.values.tolist()
newtab = tab.loc[:, ['Survived', 'Pclass', 'Sex', 'Age', 'Embarked']]
newtab.Age = newtab.Age.fillna(0)
for i in range(len(newtab)):
    if (newtab.Sex[i] == 'male'):
        newtab.Sex[i] = 0
    elif (newtab.Sex[i] == 'female'):
        newtab.Sex[i] = 1
    if (newtab.Embarked[i] == 'S'):
        newtab.Embarked[i] = 0
    elif (newtab.Embarked[i] == 'C'):
        newtab.Embarked[i] = 1
    elif (newtab.Embarked[i] == 'Q'):
        newtab.Embarked[i] = 2
    else:
        newtab.Embarked[i] = 3

newtab2 = newtab.iloc[:, :1]
tab2 = newtab.iloc[:, 1:]
X_train, X_test, y_train, y_test = train_test_split(tab2, newtab2, test_size=0.5, random_state=42)
reg = model.fit(X_train, y_train)
pre = model.predict(X_test)
new = accuracy_score(y_test, pre)
print(X_train, X_test, y_train, y_test, reg, pre)
print(tab2)
print(newtab2)
print(type(tab))
print(tab, new)

main("titanic.csv", 1, 94)