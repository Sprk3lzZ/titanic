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

    tabmodif = tab.loc[:, ['Survived', 'Pclass', 'Sex', 'Age', 'Embarked']]
    tabmodif.Age = tabmodif.Age.fillna(0)

    for i in range(len(tabmodif)):
        if tabmodif.Sex[i] == 'male':
            tabmodif.Sex[i] = 0
        elif tabmodif.Sex[i] == 'female':
            tabmodif.Sex[i] = 1
        if tabmodif.Embarked[i] == 'S':
            tabmodif.Embarked[i] = 0
        elif tabmodif.Embarked[i] == 'C':
            tabmodif.Embarked[i] = 1
        elif tabmodif.Embarked[i] == 'Q':
            tabmodif.Embarked[i] = 2
        else:
            tabmodif.Embarked[i] = 3
    return tabmodif

def main(k,longueur, largeur,a,b):
    """
    :return:
    """
    tabt = modif()
    x = tabt.loc[:, "Pclass"]
    y = tabt.loc[:, "Sex"]
    z = tabt.loc[:, "Age"]
    w = tabt.loc[:, "Embarked"]
    tab2 = list(zip(x,y,z,w))
    print(tab2)
    lab = tabt.loc[:, "Survived"]
    model = KNeighborsClassifier(n_neighbors=k)
    print("model v1: ", model)
    model.fit(tab2, lab)
    print("model v2: ", model)
    prediction = model.predict([[longueur, largeur,a,b]])
    print("prediction : ", prediction)



main(5,1,0,80,1)