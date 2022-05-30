import qcm
import utilisateur
import membre
import admin

user_or_qcm = input('1 - User, 2 - QCM : ')

if user_or_qcm == "1":
    choix = input('1- liste, 2- Se connecter : ')
    dico = {'id':'jeannot','_nom':'Huret','_prenom':'Jean','role':'membre','email':'jean.huret@gmail.com', '__mot_de_passe':'shuuuut4'}
    user = utilisateur.Utilisateur(dico)
    if choix == '1':
        liste_utilisateurs = user.ListeUtilisateur()
        for one_user in liste_utilisateurs:
            print(one_user)
    elif choix == "2":
        login = input('Identifiant : ')
        password = input('Mot de passe : ')
        user.connecte(login, password)
        print('Utilisateur connecté')
    else :
        print('Merci de choisir un id ou un mot de passe valide')    
        if user.connecte :
            if user.role == "membre":
                print('Modification de votre fiche')
                membre1 = membre.Membre(dico)
                membre1.connecte = True
                membre1.modifieMesInfos(dico)
            elif user.role == 'admin':
                choix_admin = input('1-Ajouter un membre 2-Supprimer un membre')
                if choix_admin == "1":
                    dico['_nom'] = input('Nom')
                    dico['_prenom'] = input('prenom')
                    nouvelle_donnees = ','.join(dico.values())
                    user.AjoutUtilisateur(nouvelle_donnees)
                elif choix_admin == "2":
                    id_user_supp = input('Quel est le pseudo de l\'utilisateur que vous voulez supprimer?')
                    user.SupprimeUtilisateur(id_user_supp)





elif user_or_QCM == "2":
    qcm = qcm.QCM()
    choix = input('Choisir 1 - Liste, 2 - Ajout, 3 - Voir un QCM, 4 - Supprimer')
    if choix == "1":
        for un_QCM in qcm.listeQCM():
            print(un_QCM)
    elif choix == "2":
        nom_du_QCM = input('Nom du QCM')
        descriptif = input('descriptif')
        categorie = input('categorie')
        duree = input ('duree')
        print(qcm.ajoutQCM(nom_du_QCM, descriptif, categorie, duree))
    elif choix == "3":
        identifiant = input('Nom du QCM')
        print(qcm.voirQCM(identifiant))
    elif choix == "4":
        identifiant = input('Nom du QCM')
        print(qcm.supprimerQCM(identifiant))
    else :
        print("Merci de saisir  un choix valide")
else :
        print("Merci de saisir  un choix valide")