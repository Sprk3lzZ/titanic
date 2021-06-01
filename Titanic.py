import pandas
from sklearn.neighbors import KNeighborsClassifier

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
    Fonctin qui modifie et selectionne les informations les plus utiles pour la recherche.
    :return: list
    """

    tab, newtab = starter()
    tabmodif = tab.loc[:, ['Survived', 'Pclass', 'Sex', 'Age', 'Embarked']] #Selection des catégories qui nous intéresse.

    tabmodif.Age = tabmodif.Age.fillna(0) #Transforme les ages inconnus à 0.

    for i in range(len(tabmodif)):    #Boucle servant à attribuer aux valeurs du csv des valeurs utilisables/pratiques.
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
    return tabmodif


def main(k, classe,sexe,age,embarquement):
    """
    Fonction qui teste si la personne qui entre ses informations serait en vie après le drame du titanic
    :return: sting
    """
    tabt = modif()
    t_classe = tabt.loc[:, "Pclass"]                         #Créations des tableaux par catégorie.
    t_sexe = tabt.loc[:, "Sex"]
    t_age = tabt.loc[:, "Age"]
    t_embarquement = tabt.loc[:, "Embarked"]
    tab2 = list(zip(t_classe, t_sexe, t_age, t_embarquement)) #Création du tableau de tuples.
    lab = tabt.loc[:, "Survived"]
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(tab2, lab)
    prediction = model.predict([[classe,sexe,age,embarquement]])

    if prediction == 0:
        print("Desolé, mais vous n'auriez pas survecu...")
    else:
        print("Super ! Vous avez l'étoffe d'un survivant !")


def questions():
    """
    Fonction qui demande les informations à l'utilisateur.
    :return:
    """

    classe = float(input("Veuilliez rentrer votre classe : "))
    sexe = float(input("Veuilliez rentrer votre sexe ( 1 : femme / 0 : homme ) : "))
    age = float(input("Veuilliez rentrer votre age : "))
    embarquement = float(input("Veuilliez rentrer votre numero d'embarquement : "))

    main(5,classe,sexe,age,embarquement)



questions()
