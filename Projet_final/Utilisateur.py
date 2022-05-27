class Utilisateur:
    # Propriétés de l'utilisateur
    _nom = ""
    _prenom = ''
    _age = int()

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
    def jeMappelle(self):
        nom_complet = self.nom + self.prenom
        return 'Je m\'appelle' + nom_complet

    def jaiXAge(self):
        return 'J\'ai ' + self.age + 'ans'

    # Destructeur appelé à la suppression de l'objet 
    def __del__(self):
        return 'L objet a bien été supprimé'

class Membre(Utilisateur):
    is_membre = True

    def jeMappelle(self):
        self._pseudo
        return 'Je suis un membre'


class Visiteur():
    adresse = ''
    def __init__(self, nom="Anonyme", prenom="Anonymous"):
        self.adresse = "10.0.0.1"

class Admin(Visiteur, Membre, Utilisateur):
    is_admin = True

    def jeMappelle(self):
        return 'Je suis un administrateur !!!!!!'
