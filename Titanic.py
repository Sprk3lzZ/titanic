import pandas
from sklearn.model_selection import *
from sklearn.linear_model import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

tab = pandas.read_csv("titanic.csv", sep=',')

newtab = tab.loc[:, ['Survived', 'Pclass', 'Sex', 'Age', 'Embarked']]
newtab.Age = newtab.Age.fillna(0)

def modif():
    """

    :return:
    """

    newtab = tab.loc[:, ['Survived', 'Pclass', 'Sex', 'Age', 'Embarked']]
    newtab.Age = newtab.Age.fillna(0)

    for i in range(len(newtab)):
        if newtab.Sex[i] == 'male':
            newtab.Sex[i] = 0
        elif newtab.Sex[i] == 'female':
            newtab.Sex[i] = 1
        if newtab.Embarked[i] == 'S':
            newtab.Embarked[i] = 0
        elif newtab.Embarked[i] == 'C':
            newtab.Embarked[i] = 1
        elif newtab.Embarked[i] == 'Q':
            newtab.Embarked[i] = 2
        else:
            newtab.Embarked[i] = 3

def main(k,longueur, largeur,a,b):
    """

    :return:
    """
    modif()
    x = newtab.loc[:, "Pclass"]
    y = newtab.loc[:, "Sex"]
    z = newtab.loc[:, "Age"]
    w = newtab.loc[:, "Embarked"]
    tab2 = list(zip(x,y,z,w))
    lab = newtab.loc[:, "Survived"]
    model = KNeighborsClassifier(n_neighbors=k)
    print("model v1: ", model)
    model.fit(tab2, lab)
    print("model v2: ", model)
    prediction = model.predict([[longueur, largeur,a,b]])
    print("prediction : ", prediction)



main(2,2,2,2,2)