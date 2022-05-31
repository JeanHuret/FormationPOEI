import mariadb
class Utilisateurs:
    
    def __init__(self, qcm, liste_categorie, connexion) -> None:
        # Propriété de l'objet utilisateur
        self.__id = ''
        self.__pseudo = ''
        self.__prenom = ''
        self.__nom = ''
        self.__role = ''
        self.__email = 'dubois.thomas@gmail.com'
        self.__password = ''
        self.__qcm = qcm
        self.__connexion = connexion
        
    def get_id(self):
        return self.__id

    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id

    def get_pseudo(self):
        return self.__pseudo

    def set_pseudo(self, pseudo):
        if isinstance(pseudo, str): 
            self.__pseudo = pseudo

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, prenom):
        if isinstance(prenom, str): 
            self.__prenom = prenom       

    def set_nom(self, nom):
        self._nom = nom

    def get_nom(self):
        return self._nom.upper()

    def get_role(self):
        return self.__role

    def set_role(self, role):
        if isinstance(role, str): 
            self.__role = role

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if isinstance(email, str): 
            self.__email = email

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

     # Lister les utilisateurs avec les caractéristiques suivantes : 
    def listeUtilisateurs(self):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM utilisateurs')
        liste_utilisateurs =  cursor.fetchall()
        utilisateurs_liste = []     
        return utilisateurs_liste

    def saisie_utilisateur(self):
        liste_donnees = []
        pseudo = input('Quel est votre pseudo ?')
        liste_donnees.append(pseudo)
        prenom = input('Quel est votre prenom ?')
        liste_donnees.append(prenom)
        nom = input('Quel est votre nom ?')
        liste_donnees.append(nom)
        role = input('Etes-vous admin ou membre ?')
        liste_donnees.append(role)
        email = input('Quel est votre email ?') 
        liste_donnees.append(email)
        mot_de_passe = input('Quel est votre mot de passe ?')
        liste_donnees.append(mot_de_passe)
        return liste_donnees

    # • Permettre l’ajout d’un utilisateur
    def AjouterUtilisateur(self, liste_donnees):
        try: 
            cursor = self.__connexion.cursor()
            cursor.execute('INSERT INTO utilisateurs ( `pseudo`, `prenom`, `nom`, `role`, `email`, `mot_de_passe`)  VALUES (?, ?, ?, ?, ?, ?);',(liste_donnees[0], liste_donnees[1], liste_donnees[2], liste_donnees[3], liste_donnees[4], liste_donnees[5],))
            id_utilisateur = cursor.lastrowid
            self.__connexion.commit()
            return 'L\'utilisateur  a bien été ajouté'
        except mariadb.Error as e:     
            return f'Erreur lors de l\'ajout {e} '


    def __TrouverUtilisateur(self,pseudo):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM utilisateurs WHERE pseudo = ?;',(pseudo,))
        utilisateur_a_afficher = cursor.fetchone()
        return utilisateur_a_afficher

    # Permettre de récupérer les informations d’un utilisateur en saisissant son pseudo
    def voirUtilisateur(self, pseudo) :
        utilisateur_a_afficher = self.__TrouverUtilisateur(pseudo)
        return utilisateur_a_afficher
    
    # Permettre de modifier un utilisateur à partir de son pseudo
    def modifierUtilisateur(self, utilisateur, nouvelles_donnees):
        self.supprimerUtilisateur(utilisateur)
        self.AjouterUtilisateur(nouvelles_donnees)
        return self.voirUtilisateur(utilisateur)

    # Permettre de supprimer une utilisateur
    def supprimerUtilisateur(self, pseudo):
        try :
            cursor = self.__connexion.cursor()
            cursor.execute('SELECT id FROM utilisateurs WHERE pseudo = ? ',(pseudo,))
            id_utilisateur = cursor.fetchone()
            cursor.execute('DELETE FROM utilisateurs WHERE pseudo = ?;',(pseudo,))
            self.__connexion.commit()
            return 'L\'utilisateur a bien été supprimé'
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '
    
    def connexionUtilisateur(self, pseudo, password):
        try:
            cursor=self.__connexion.cursor()
            cursor.execute('SELECT * FROM utilisateurs WHERE pseudo = ? AND password = ?',(pseudo, password,))
            utilisateur_a_afficher = cursor.fetchone()
            return utilisateur_a_afficher + 'Connexion établie'
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '
        
class Admin(Utilisateurs):
    is_admin = True
    def isAdmin(self):
        return True

class Membre(Utilisateurs):
    is_membre = True
    def isMembre(self):
        return True