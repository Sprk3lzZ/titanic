  
import pandas
from sklearn.model_selection import *
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

def starter():
    """
    Fonction qui initialise le tableeau via le csv.
    :return: lists
    """
    tab = pandas.read_csv("titanic.csv", sep=',')

    newtab = tab.loc[:, ['Survived', 'Pclass', 'Sex', 'Age', 'Embarked']]

    return tab, newtab

def modif():
    """
    Fonction qui modifie et selectionne les informations les plus utiles pour la recherche.
    :return: list
    """
    tab, newtab = starter()
    tabmodif = tab.loc[:,['Survived', 'Pclass', 'Sex', 'Age', 'Embarked']]  # Selection des catégories qui nous intéresse.

    tabmodif.Age = tabmodif.Age.fillna(0)  # Transforme les ages inconnus à 0.

    for i in range(len(tabmodif)):  # Boucle servant à attribuer aux valeurs du csv des valeurs utilisables/pratiques.
        if (tabmodif.Age[i] == 0):
            nb = 0
            for e in range(i):
                nb += tabmodif.Age[e]
            nb = nb / (i + 1)
            newtab.Age[i] = int(nb)
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
            tabmodif.Embarked[i] = tabmodif.Embarked[i - 1]
    calcul(tabmodif)

def calcul(newtab):
    """
    Fonction qui calcule le pourcentage de fiabililté.
    :return: pourcentage
    """
    newtab2 = newtab.iloc[:, :1]
    tab2 = newtab.iloc[:, 1:]
    X_train, X_test, y_train, y_test = train_test_split(tab2, newtab2, test_size=0.5, random_state=42)
    reg = model.fit(X_train, y_train)
    pre = model.predict(X_test)
    pourcentage = accuracy_score(y_test, pre)

    print('Pourcentage : ', round(pourcentage * 100, 2), "%")

modif()
