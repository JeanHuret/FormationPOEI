import configdb
import modules.connexiondb as db
import modules.qcm as qcm
import modules.utilisateurs as utilisateurs

bdd = db.ConnectDb(configdb.config)
connexion = bdd.connect()

choix = input('1- Se connecter, 2- S\'inscrire : ')
dico = {'id':'jeannot','_nom':'Huret','_prenom':'Jean','role':'membre','email':'jean.huret@gmail.com', '__mot_de_passe':'shuuuut4'}
user = utilisateurs.Utilisateurs(dico)
if choix == '1':
    pseudo = input('Identifiant : ')
    password = input('Mot de passe : ')
    user.connexionUtilisateur(pseudo, password)   
    if user.connecte:
        print('Utilisateur connecté')
        if user.role == 'membre':
                choix_membre = input('1-Modification de votre fiche, 2-Liste QCM, 3-Choisir QCM : ')
                if choix_membre == '1':
                    membre1 = membre.Membre(dico)
                    membre1.connecte = True
                    membre1.modifieMesInfos(dico)
                elif choix_membre == '2':
                    for un_QCM in qcm.listeQCM():
                        print(un_QCM)
               # elif choix_membre == '3':
        elif user.role == 'admin':
                choix_admin = input('1-Supprimer un membre, 2-Liste Utilisateur, 3-Liste QCM, 4-Ajouter QCM, 5-Modifier QCM, 6-Supprimer un QCM : ')
                if choix_admin == "1":
                    id_user_supp = input('Quel est le pseudo de l\'utilisateur que vous voulez supprimer?')
                    user.SupprimeUtilisateur(id_user_supp)              
                elif choix_admin == "2":
                    id_user_supp = input('Quel est le pseudo de l\'utilisateur que vous voulez supprimer?')
                    user.SupprimeUtilisateur(id_user_supp)
               # elif choix_membre == '4': 
elif choix == '2':
    id = input('Identifiant : ')
    prenom = input('Prénom : ')
    nom = input('Nom : ')
    role = input('role : ')
    email = input('email : ')
    mot_de_passe = input('mot de passe : ')
    print(user.AjoutUtilisateur(id, prenom, nom, role, email, mot_de_passe ))
else: 
    print('Merci de rentrer un identifiant ou un mot de passe valide')








    # qcm = qcm.QCM()
    # choix = input('Choisir 1 - Liste, 2 - Ajout, 3 - Voir un QCM, 4 - Supprimer')
    # if choix == "1":
    #     for un_QCM in qcm.listeQCM():
    #         print(un_QCM)
    # elif choix == "2":
    #     nom_du_QCM = input('Nom du QCM')
    #     descriptif = input('descriptif')
    #     categorie = input('categorie')
    #     duree = input ('duree')
    #     print(qcm.ajoutQCM(nom_du_QCM, descriptif, categorie, duree))
    # elif choix == "3":
    #     identifiant = input('Nom du QCM') 
#        print(qcm.voirQCM(identifiant))
#    elif choix == "4":
#        identifiant = input('Nom du QCM')
#        print(qcm.supprimerQCM(identifiant))
 #   else :
 #        print("Merci de saisir  un choix valide")
# else :
        # print("Merci de saisir  un choix valide")"