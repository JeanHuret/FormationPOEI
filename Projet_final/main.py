import QCM
import Utilisateur

user_or_QCM = input('1 - User, 2 - QCM : ')

if user_or_QCM == "1":
    liste = {'_nom':'david','_prenom':'vanessa','role':'membre'}
    user = Utilisateur.Utilisateur(liste)
elif user_or_QCM == "2":
    qcm = QCM.QCM()
    choix = input('Choisir 1 - Liste, 2 - Ajout, 3 - Voir un QCM, 4 - Supprimer')
    if choix == "1":
        for un_QCM in QCM.listeQCM():
            print(un_QCM)
    elif choix == "2":
        nom_du_QCM = input('Nom du QCM')
        descriptif = input('descriptif')
        categorie = input('categorie')
        duree = input ('duree')
        print(QCM.ajoutQCM(nom_du_QCM, descriptif, categorie, duree))
    elif choix == "3":
        identifiant = input('Nom du QCM')
        print(QCM.voirQCM(identifiant))
    elif choix == "4":
        identifiant = input('Nom du QCM')
        print(QCM.supprimerQCM(identifiant))
    else :
        print("Merci de saisir  un choix valide")
else :
        print("Merci de saisir  un choix valide")