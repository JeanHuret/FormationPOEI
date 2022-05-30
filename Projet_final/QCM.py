# Création de la classe QCM
class QCM():
    __nom_du_QCM = ""
    __descriptif = ""
    __categorie  = ''
    __duree = ''

#initialisation

    def __init__(self):
        self.setCategorie('Culture')
        self.__identifiant_du_QCM = 1

    def getIdentifiantDuQCM(self):
        return self.__identifiant_du_QCM

    def setNomDuQCM(self, nom):
        if type(nom) == 'str':
            self.nom_du_QCM = nom
        else :
            return 'Erreur : merci de saisir une chaine de caractère valide'

# Fonction pour lister les QCM disponibles

    def listeQCM(self):
        fichier = open('./QCM.txt','r')
        liste_QCM = fichier.readlines()
        fichier.close()
        return liste_QCM

# Fonction pour ajouter un QCM
 
    def ajoutQCM(self, nom_du_QCM, descriptif, categorie, duree):
        try : 
            nom_du_QCM = str(nom_du_QCM)
            descriptif = str(descriptif)
            categorie= str(categorie)
            duree = int(duree)

        except:
            return 'Les données saisies ne sont pas correctes'
        
        # On vérifie si le QCM existe déjà, sinon on lève une exception
        
        if self.__trouverunQCM(nom_du_QCM) :
            raise Exception('Le QCM existe déjà dans la liste')
        QCM = '\n' + nom_du_QCM + ',' + descriptif + ',' + categorie + ',' + str(duree)
        fichier = open('./QCM.txt','a')
        fichier.write(QCM)
        fichier.close()
        return QCM + 'Le QCM a bien été ajouté'

    def voirQCM(self, identifiant_du_QCM):
        if type(identifiant_du_QCM) == 'str':
            QCM_a_afficher = self.__trouverunQCM(identifiant_du_QCM)
            return QCM_a_afficher

    def supprimerQCM(self, identifiant_du_QCM):
        QCM_a_supprimer = self.__trouverunQCM(identifiant_du_QCM)
        liste_QCM = self.listeQCM()
        for QCM in liste_QCM:
            if QCM_a_supprimer ==  QCM:
                liste_QCM.remove(QCM_a_supprimer)
        fichier = open('./QCM.txt','w')
        fichier.writelines(liste_QCM)
        fichier.close()
        return 'Le QCM a bien été supprimé'

    def __trouverunQCM(self,id):
        liste_QCM = self.listeQCM()
        QCM_a_afficher = ''
        for QCM in liste_QCM:
            QCM_split = QCM.split(',')
            if QCM_split[0] == id:
                QCM_a_afficher = ','.join(QCM_split)
        return QCM_a_afficher