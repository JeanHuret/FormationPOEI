import mariadb
from utilisateurs import Utilisateurs

class Admin(Utilisateurs):
    is_admin = True
    def isAdmin(self):
        return True