class reponse_qcm:

    def __init__(self, liste_reponses,connexion) -> None:
        # Propriete de l'objet questionnaire
        self.__IDquestionnaire = ''
        self.__reponse1 = ''
        self.__reponse2 = ''
        self.__reponse3 = ''
        self.__connexion = connexion
        self.__liste_reponses = liste_reponses

    def get_IDquestionnaire(self):
        return self.__IDquestionnaire

    def set_IDquestionnaire(self, IDquestionnaire):
        if isinstance(IDquestionnaire, int): 
            self.__IDquestionnaire = IDquestionnaire
    
    def get_reponse1(self):
        return self.__reponse1

    def set_reponse1(self, reponse1):
        if isinstance(reponse1, str): 
            self.__reponse1 = reponse1
    
    def get_reponse2(self):
        return self.__reponse2

    def set_reponse2(self, reponse2):
        if isinstance(reponse2, str): 
            self.__reponse2 = reponse2

    def get_reponse3(self):
        return self.__reponse3

    def set_reponse3(self, reponse3):
        if isinstance(reponse3, str): 
            self.__reponse3 = reponse3


    def saisie_reponse(self,liste_reponses):
        liste_reponses = []
        reponse1 = input('Quel est la reponse1 de la question ?')
        liste_reponses.append(reponse1)
        reponse2 = input('Quel est la reponse2 de la questionnaire ?')
        liste_reponses.append(reponse2)
        reponse3 = input('Quel est la reponse3 de la questionnaire ?')
        liste_reponses.append(reponse3)
        return liste_reponses


# Lister les Questions 
    def liste_reponses(self):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM Question')
        liste_reponses =  cursor.fetchall()
        return liste_reponses


# selectionner une reponse

    def afficher_reponses1(self,reponses1):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM questionnaire WHERE reponses1 = ?;',(reponses1,))
        reponses1_a_afficher = cursor.fetchone()
        return reponses1_a_afficher

    def afficher_reponses2(self,reponses2):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM questionnaire WHERE reponses2 = ?;',(reponses2,))
        reponses2_a_afficher = cursor.fetchone()
        return reponses2_a_afficher

    def afficher_reponses3(self,reponses3):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM questionnaire WHERE reponses3 = ?;',(reponses3,))
        reponses3_a_afficher = cursor.fetchone()
        return reponses3_a_afficher


# Permettre l’ajout d’une reponse
    def ajouterreponse(self, liste_reponses):
        try:
            cursor = self.__connexion.cursor()
            cursor = self.__connexion.cursor()
            cursor.execute('INSERT INTO q1reponse ( `reponse1`, `reponse2`,`reponse3` )  VALUES (?, ?, ?);',(liste_reponses[0], liste_reponses[1],liste_reponses[2] ,))
            self.__connexion.commit()
            return 'La categorie a bien été ajoutée'
        except mariadb.Error as e:     
            return f'Erreur lors de ajoue {e} '

# Permettre de modifier question à partir de son nom
    def modifierreponse(self, nouvelle_donnees, liste_reponses):
        try: 
            cursor = self.__connexion.cursor()
            cursor.execute('INSERT INTO ( `reponse1`, `reponse2`,`reponse3`) VALUES (?, ?, ?,);',(liste_reponses[0], liste_reponses[1], liste_reponses[2],))
            self.__connexion.commit()
            return self.afficher_categrorie(nouvelle_donnees[0], nouvelle_donnees[1],nouvelle_donnees[2],)
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '

# Permettre de supprimer une categorie
    def supprimereponse(self,reponseid):
        try :
            ID_reponse_supprimer = input('Quel est ID de la reponse a supprimer')
            cursor = self.__connexion.cursor()
            cursor.execute('DELETE FROM q1reponse WHERE reponseid = ?;',(ID_reponse_supprimer,))
            self.__connexion.commit()
            return 'La reponse a bien été supprimée'
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '
