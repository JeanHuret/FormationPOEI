class Utilisateur:
    # Propriétés de l'utilisateur
    _nom = ""
    _prenom = ''
    _age = int()
    _mail = ""

    # Propriétés et méthodes 
    # Public : accessible en dehors
    # Privé : accessible que dans la classe
    __motdepasse = ''
    # Protégé : pas accessible en dehors de la classe mais accessible dans une classe enfant
    _pseudo = ''

    # Constructeur
    def __init__(self, dictionnaire_de_donnees):
        for cle,valeur in dictionnaire_de_donnees:
            self._cle = valeur
        

    def get_nom(self):
        return self._nom
    
    def set_nom(self, nom):
        self._nom = nom

    # Méthodes la classe utilisateur
  
class Membre(Utilisateur):
    is_membre = True

    def jeMappelle(self):
        self._pseudo
        return 'Je suis un membre'

class Admin( Membre, Utilisateur):
    is_admin = True

    def jeMappelle(self):
        return 'Je suis un administrateur !'
class Utilisateur:

    id = 0
    prenom = ""
    nom = ""
    role = "" 
    presentation = ""
    email = ""
    mot_de_passe = "" 
    connecte = False        

    def ListeUtilisateur(self) : 
        #affiche la liste des utilisateurs depuis un fichier utilisateurs.txt
        fichier = open('./corrige/exercise9/utilisateurs.txt','r')
        liste_utilisateurs = fichier.readlines()
        fichier.close()
        return liste_utilisateurs

    def AjoutUtilisateur(self, nom, prenom, role, presentation, email, mot_de_passe) : 
        #permet l'ajout d'un utilisateur depuis une saisie de l'utilisateur et enregistre l'utilisateur dans le fichier utilisateurs.txt (à la suite des autres)
        user = '\n' + nom + ',' + prenom + ',' + role + ',' + presentation + ',' + email + ',' + mot_de_passe 
        fichier = open('./corrige/exercise9/utilisateurs.txt','a')
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