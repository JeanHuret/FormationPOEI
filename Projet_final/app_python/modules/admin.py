from utilisateur import Utilisateur

class Admin(Utilisateur):
    is_admin = True
    def isAdmin(self):
        return True