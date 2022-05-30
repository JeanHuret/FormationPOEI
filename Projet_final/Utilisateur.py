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

    def set_nom(self, valeur):
        self._nom = " ma regle a moi " + valeur

    def get_mot_de_passe(self):
        mot_de_passe = ''
        for caractere in self.__mot_de_passe:
            mot_de_passe += '*'
        return mot_de_passe

    def set_mot_de_passe(self,valeur):
        if(str(valeur) and '?' in valeur ):
            self.__mot_de_passe = valeur
            return 'ok'
        else:
            return 'Erreur'

    def connexion(self, identifiant, password):
        file = open('utilisateurs.txt')
        lines = file.readlines()
        for line in lines:
            line_split = line.split(',')
            if identifiant == line_split[0] and password == line_split[5]:
                print('id ok + password ok')
                self.connecte = True
            else:
                continue
    
    nom = property(fget = get_nom, fset = set_nom)
    mot_de_passe = property (fget =  get_mot_de_passe, fset=set_mot_de_passe)

class Membre(Utilisateur):
    is_membre = True
    def isMembre(self):
        return True

class Admin(Membre, Utilisateur):
    is_admin = True

    def jeMappelle(self):
        return 'Je suis un administrateur !'

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
        fichier = open('./utilisateurs.txt','w')
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