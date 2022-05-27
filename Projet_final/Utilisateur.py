class Utilisateur:

    _id = 0
    _prenom = ""
    _nom = ""
    _role = "" 
    _email = ""
    __mot_de_passe = "" 
    _connecte = False        

    def ListeUtilisateur(self) : 
        #affiche la liste des utilisateurs depuis un fichier utilisateurs.txt
        fichier = open('./utilisateurs.txt','r')
        liste_utilisateurs = fichier.readlines()
        fichier.close()
        return liste_utilisateurs

    def AjoutUtilisateur(self, nom, prenom, role, email, mot_de_passe) : 
        #permet l'ajout d'un utilisateur depuis une saisie de l'utilisateur et enregistre l'utilisateur dans le fichier utilisateurs.txt (à la suite des autres)
        user = '\n' + nom + ',' + prenom + ',' + role + ',' + email + ',' + mot_de_passe 
        fichier = open('./utilisateurs.txt','a')
        fichier.write(user)
        fichier.close()
        return user + 'L\'utilisateur a bien été ajouté'

    def VoirUtilisateur(self, idutilisateur) :
        # permet d'afficher les informations d'un utilisateur précis en fonction de son identifiant (paramètre à demander à l'utilisateur)
         if type(idutilisateur) == 'str':
            user_a_afficher = self.__trouverunuser(idutilisateur)
            return user_a_afficher

    def SupprimeUtilisateur(self, idutilisateur) :
        # supprime un jeu du fichier utilisateurs.txt à partir de son identifiant
        user_a_supprimer = self.__trouverunuser(idutilisateur)
        liste_users = self.ListeUtilisateur()
        for user in liste_users:
            if user_a_supprimer ==  user:
                liste_users.remove(user_a_supprimer)
        fichier = open('./corrige/exercise9/utilisateurs.txt','w')
        fichier.writelines(liste_users)
        fichier.close()

    def SeConnecter(self, identifiant, motdepasse) : 
        # vérifier si les informations saisies par l'utilisateur correspondent à celle de l'utilisateur puis lui donné le statut connecté
        file = open('./corrige/exercise9/utilisateurs.txt')
        lines = file.readlines()
        for line in lines:
            line_split = line.split(',')
            if identifiant == line_split[0] and motdepasse == line_split[6]:
                print('id ok + password ok')
                self.connecte = True
            else:
                continue

    def __trouverunuser(self,id):
        liste_user = self.ListeUtilisateur()
        user_a_afficher = ''
        for user in liste_user:
            user_split = user.split(',')
            if user_split[0] == id:
                user_a_afficher = ','.join(user_split)
        return user_a_afficher