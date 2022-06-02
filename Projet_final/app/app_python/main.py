import configdb
import mariadb
import modules.connexiondb as db
from modules.qcm import Qcm
import modules.utilisateurs as utilisateurs

bdd = db.ConnexionDb(configdb.config)
connexion = bdd.connect()

choix_donnees = input('Choisir : 1 - Membre, 2 - Admin : ')
if choix_donnees == "1":
    questionnaire = Qcm(utilisateurs, connexion)
    membre = utilisateurs.Membre(utilisateurs, connexion)
    choix = input('Choisir : 1 - Liste des QCM, 2 - \
     Faire un QCM 3 - Modifier ses informations : ')
    if choix == "1":
        for un_qcm in questionnaire.liste_data_qcm():
            print(un_qcm)
    elif choix == "2":
        donnees_qcm = questionnaire.saisie_data_qcm()
        print(questionnaire.ajouter_data_qcm(donnees_qcm))
    elif choix == "3":
        identifiant = input('Quel est le pseudo à modifier ? : ')
        donnees_utilisateur = membre.saisie_utilisateur()
        print(membre.modifierUtilisateur(identifiant, donnees_utilisateur))
    else:
        print("Merci de saisir un choix valide")
elif choix_donnees == "2":
    questionnaire = Qcm(connexion)
    admin = utilisateurs.Admin(utilisateurs, connexion)
    choix_utilisateur_qcm = input('Choisir : 1 - Gérer les utilisateurs \
    2 - Gérer les QCM : ')
    if choix_utilisateur_qcm == "1":
        choix = input('Choisir : 1 - Liste des utilisateurs, \
         2 - Ajouter un utilisateur, 3 - Voir un utilisateur,\
         4 - Modifier un utilisateur, 5 - Supprimer un utilisateur : ')
        if choix == "1":
            for un_utilisateur in admin.listeUtilisateurs():
                print(un_utilisateur)
        elif choix == "2":
            donnees_utilisateur = admin.saisie_utilisateur()
            print(admin.AjouterUtilisateur(donnees_utilisateur))
        elif choix == "3":
            identifiant = input('Pseudo de l\'utilisateur : ')
            print(admin.voirUtilisateur(identifiant))
        elif choix == "4":
            identifiant = input('Quel est le pseudo à modifier ? ')
            donnees_utilisateur = admin.saisie_utilisateur()
            print(admin.modifierUtilisateur(identifiant, donnees_utilisateur))
        elif choix == "5":
            identifiant = input('Pseudo de l\'utilsateur à supprimer : ')
            print(admin.supprimerUtilisateur(identifiant))
        else:
            print("Merci de saisir un choix valide")
    elif choix_utilisateur_qcm == "2":
        choix = input('Choisir : 1 - Liste QCM,  2 - Ajouter un QCM,\
            3 - Voir un QCM, 4 - Modifier un QCM , 5 - Supprimer un QCM : ')
        if choix == "1":
            for un_qcm in questionnaire.liste_data_qcm():
                print(un_qcm)
        elif choix == "2":
            donnees_QCM = questionnaire.saisie_data_qcm()
            print(questionnaire.ajouter_data_qcm(donnees_QCM))
        elif choix == "3":
            identifiant = input('Id du QCM : ')
            print(questionnaire.voir_data_qcm(identifiant))
        elif choix == "4":
            identifiant = input('quel est l id du QCM ? ')
            donnees_QCM = questionnaire.trouver_data_qcm(qcm_id=identifiant)
            print(questionnaire.modifier_data_qcm(donnees_QCM))
        elif choix == "5":
            identifiant = input('id du QCM à supprimer : ')
            print(questionnaire.supprimer_data_qcm(identifiant))
        else:
            print("Merci de saisir un choix valide")
    else:
        print("Merci de saisir un choix valide") 
else:
    print("Merci de saisir un choix valide")

