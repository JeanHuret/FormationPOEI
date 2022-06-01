class categorie_qcm:

    def __init__(self, liste_categorie,connexion) -> None:
        # Propriete de l'objet questionnaire
        self.__IDcategorie = ''
        self.__categorie = ''
        self.__connexion = connexion
        self.__liste_categorie = liste_categorie

    def get_IDcategorie(self):
        return self.__IDcategorie

    def set_IDcathegorie(self, IDcategorie):
        if isinstance(IDcategorie, int): 
            self.__IDcategorie = IDcategorie
    
    def get_cathegorie(self):
        return self.__categorie

    def set_cathegorie(self, categorie):
        if isinstance(categorie, str): 
            self.__categorie = categorie

    def get_liste_categorie(self):
        return self.__liste_categorie

    def set_cathegorie(self, liste_categorie):
        if isinstance(liste_categorie, str): 
            self.__liste_categorie = liste_categorie


# Lister les cathégories 
    def liste_categorie(self):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM categorie')
        liste_categorie =  cursor.fetchall()
        return liste_categorie


# selectionner une categorie

    def afficher_categrorie(self,categorie):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM cathegorie WHERE nom = ?;',(categorie,))
        categorie_a_afficher = cursor.fetchone()
        return categorie_a_afficher

# selectionner un questionnaire avec la categorie

    def afficher_questionnaire(self,questionnaire):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM cathegorie WHERE questionnaire = ?;',(questionnaire,))
        categorie_a_afficher = cursor.fetchone()
        return categorie_a_afficher

# saisie categorie
    def saisie_categorie(self,liste_categorie):
        liste_categorie = []
        Question_nom_categorie = input('Quel est le nom de votre categorie ?')
        liste_categorie.append(Question_nom_categorie)
        Question_questionnaire = input('Quel est le nom du questionnaire ?')
        liste_categorie.append(Question_questionnaire)
        return liste_categorie

# Permettre l’ajout d’une categorie
    def ajoutercategorie(self, liste_categorie):
        try:
            cursor = self.__connexion.cursor()
            cursor.execute('INSERT INTO categorie ( `nom`, `questionnaire`)  VALUES (?, ?);',(liste_categorie[0], liste_categorie[1],))
            self.__connexion.commit()
            return 'La categorie a bien été ajoutée'
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '

# Permettre de modifier categorie à partir de son nom
    def modifiercategorie(self, nouvelle_donnees):
        try: 
            cursor = self.__connexion.cursor()
            cursor.execute('UPDATE categorie SET `nom` = ? , `questionnaire` = ?;',(nouvelle_donnees[0], nouvelle_donnees[1],))
            self.__connexion.commit()
            return self.afficher_categrorie(nouvelle_donnees[0], nouvelle_donnees[1],)
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '

# Permettre de supprimer une categorie
    def supprimecategorie(self,ID_Question_supprimer):
        try :
            ID_Question_supprimer = input('Quel est ID de la categorie a supprimer')
            cursor = self.__connexion.cursor()
            cursor.execute('DELETE FROM categorie WHERE categorieid = ?;',(ID_Question_supprimer,))
            self.__connexion.commit()
            return 'La machine a bien été supprimée'
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '
