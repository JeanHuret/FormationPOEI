class Utilisateur:
    id = 0
    _prenom = ""
    _nom = "" # protégé
    role = "" # public
    email = ""
    __mot_de_passe = "" # private mot_de_passe
    connecte = False
    _keys = ['_nom', '_prenom' ]

    def __init__(self, dictionnaire) :
        for cle, valeur in dictionnaire.items():
            setattr(self, cle, valeur)
        
    def get_nom(self):
        return self._nom.upper()

    def set_nom(self, nom):
        self._nom = nom

    def get_mot_de_passe(self):
        mot_de_passe = ''
        for caractere in self.__mot_de_passe:
            mot_de_passe += '*'
        return mot_de_passe

    def set_mot_de_passe(self,valeur):
        if(len(valeur) > 8 and not valeur.isalpha() and not valeur.isnumeric() ):
            self.__mot_de_passe = valeur
            print('ok')
            return 'ok'
        else:
            print('Merci de respecter les conditions')
            return 'Merci de respecter les conditions'

    def ListeUtilisateur(self) : 
        #affiche la liste des utilisateurs depuis un fichier utilisateurs.txt
        fichier = open('utilisateurs.txt','r')
        liste_utilisateurs = fichier.readlines()
        fichier.close()
        return liste_utilisateurs

    def AjoutUtilisateur(self, chaine_caractere_donnees) : 
        #permet l'ajout d'un utilisateur depuis une saisie de l'utilisateur et enregistre l'utilisateur dans le fichier utilisateurs.txt (à la suite des autres)
        user = '\n' + chaine_caractere_donnees
        fichier = open('utilisateurs.txt','a')
        fichier.write(user)
        fichier.close()
        return user + 'L\'utilisateur a bien été ajouté'

    def VoirUtilisateur(self, idutilisateur) :
        # permet d'afficher les informations d'un utilisateur précis en fonction de son identifiant (paramètre à demander à l'utilisateur)
        user_a_afficher = self.__trouverunuser(idutilisateur)
        return user_a_afficher

    def SupprimeUtilisateur(self, idutilisateur) :
        # supprime un jeu du fichier utilisateurs.txt à partir de son identifiant
        user_a_supprimer = self.__trouverunuser(idutilisateur)
        liste_users = self.ListeUtilisateur()
        for user in liste_users:
            if user_a_supprimer ==  user:
                liste_users.remove(user_a_supprimer)
        fichier = open('utilisateurs.txt','w')
        fichier.writelines(liste_users)
        fichier.close()

    def __trouverunuser(self,id):
        liste_user = self.ListeUtilisateur()
        user_a_afficher = ''
        for user in liste_user:
            user_split = user.split(',')
            if user_split[0] == id:
                user_a_afficher = ','.join(user_split)
        return user_a_afficher

    def connexion(self, id, password):
# vérifier si les informations saisies par l'utilisateur correspondent à celle de l'utilisateur puis lui donné le statut connecté
        file = open('utilisateurs.txt')
        lines = file.readlines()
        for line in lines:
            print (line)
            line_split = line.split(',')           
            if id == line_split[0] and password == line_split[5]:
                    print('id OK + password ok')
                    self.connecte = True
                    self.role = line_split[3]
            
               
    nom = property(fget = get_nom, fset = set_nom)
    mot_de_passe = property (fget =  get_mot_de_passe, fset=set_mot_de_passe)


