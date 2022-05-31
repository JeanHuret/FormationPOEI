import mariadb
from utilisateurs import Utilisateurs

class Membre(Utilisateurs):
    is_membre = True
    def isMembre(self):
        return True

    def modifieMesInfos(self, dictionnaire_donnes):
        # On vérifie que l'utilisateur est connecté
        if self.connecte :
            print('connecte')
            # Vérifie que les informations saisies par l'utilisateur correspondent aux siennes, on utilise l'id
            if self.id == dictionnaire_donnes['id']:
                print('identifiant ok')
                dictionnaire_donnes['_nom'] = input('Nom')
                dictionnaire_donnes['_prenom'] = input('prenom')
                dictionnaire_donnes['email'] = input('email')
                nouvelles_donnees = ','.join(dictionnaire_donnes.values())
                self.SupprimeUtilisateur(self.id)
                self.AjoutUtilisateur(nouvelles_donnees)
                return self.VoirUtilisateur(self.id) 
            else :
                return 'Vous ne pouvez modifier que vos propres données'
        else:
            return 'Merci de vous connecter'