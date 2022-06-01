class questionnaire_qcm:

    def __init__(self, liste_Questions,connexion) -> None:
        # Propriete de l'objet questionnaire
        self.__IDquestionnaire = ''
        self.__cathegorie = ''
        self.__Question1 = ''
        self.__Question2 = ''
        self.__Question3= ''
        self.__Question4 = ''
        self.__Question5 = ''
        self.__Question6 = ''
        self.__connexion = connexion
        self.__liste_Questions = liste_Questions

    def get_IDquestionnaire(self):
        return self.__IDquestionnaire

    def set_IDquestionnaire(self, IDquestionnaire):
        if isinstance(IDquestionnaire, int): 
            self.__IDquestionnaire = IDquestionnaire
    
    def get_categorie(self):
        return self.__cathegorie

    def set_categorie(self, cathegorie):
        if isinstance(cathegorie, str): 
            self.__cathegorie = cathegorie
    
    def get_Question1(self):
        return self.__Question1

    def set_Question1(self, Question1):
        if isinstance(Question1, str): 
            self.__Question1 = Question1

    def get_Question2(self):
        return self.__Question2

    def set_Question2(self, Question2):
        if isinstance(Question2, str): 
            self.__Question2 = Question2

    def get_Question3(self):
        return self.__Question3

    def set_Question3(self, Question3):
        if isinstance(Question3, str): 
            self.__Question3 = Question3

    def get_Question4(self):
        return self.__Question4

    def set_Question4(self, Question4):
        if isinstance(Question4, str): 
            self.__Question4 = Question4

    def get_Question5(self):
        return self.__Question5

    def set_Question5(self, Question5):
        if isinstance(Question5, str): 
            self.__Question5 = Question5

    def get_Question6(self):
        return self.__Question6

    def set_Question6(self, Question6):
        if isinstance(Question6, str): 
            self.__Question6 = Question6

# saisir un questionnaire

    def saisie_Questionnaire(self,liste_Question):
        liste_Question = []
        Question1 = input('Quel est la Question1 du questionnaire ?')
        liste_Question.append(Question1)
        Question2 = input('Quel est la Question2 du questionnaire ?')
        liste_Question.append(Question2)
        Question3 = input('Quel est la Question3 du questionnaire ?')
        liste_Question.append(Question3)
        Question4 = input('Quel est la Question4 du questionnaire ?')
        liste_Question.append(Question4)
        Question5 = input('Quel est la Question5 du questionnaire ?')
        liste_Question.append(Question5)
        Question6 = input('Quel est la Question6 du questionnaire ?')
        liste_Question.append(Question6)
        return liste_Question


# Lister les Questions 
    def liste_Questions(self):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM Questionnaire')
        liste_Questions =  cursor.fetchall()
        return liste_Questions


# selectionner une Question

    def afficher_Question1(self,Question1):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM questionnaire WHERE question1 = ?;',(Question1,))
        Question1_a_afficher = cursor.fetchone()
        return Question1_a_afficher

    def afficher_Question2(self,Question2):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM questionnaire WHERE question2 = ?;',(Question2,))
        Question2_a_afficher = cursor.fetchone()
        return Question2_a_afficher

    def afficher_Question3(self,Question3):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM questionnaire WHERE question3 = ?;',(Question3,))
        Question3_a_afficher = cursor.fetchone()
        return Question3_a_afficher

    def afficher_Question4(self,Question4):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM questionnaire WHERE question4 = ?;',(Question4,))
        Question4_a_afficher = cursor.fetchone()
        return Question4_a_afficher

    def afficher_Question5(self,Question5):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM questionnaire WHERE question5 = ?;',(Question5,))
        Question5_a_afficher = cursor.fetchone()
        return Question5_a_afficher

    def afficher_Question6(self,Question6):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM questionnaire WHERE question6 = ?;',(Question6,))
        Question6_a_afficher = cursor.fetchone()
        return Question6_a_afficher


# Permettre l’ajout d’un questionnaire
    def ajouterQuestion(self, liste_Questions):
        try:
            cursor = self.__connexion.cursor()
            cursor = self.__connexion.cursor()
            cursor.execute('INSERT INTO questionnaire (`cathegorie`, `Question1`, `Question2`,`Question3`,`Question4`,`Question5`,`Question6` )  VALUES (?, ?, ?, ?, ?, ?, ?);',(liste_Questions[0], liste_Questions[1],liste_Questions[2], liste_Questions[3],liste_Questions[4], liste_Questions[5],liste_Questions[6],))
            self.__connexion.commit()
            return 'La categorie a bien été ajoutée'
        except mariadb.Error as e:     
            return f'Erreur lors de ajoue {e} '

# Permettre de modifier question à partir de son nom
    def modifierQuestion(self, nouvelle_donnees, liste_Questions):
        try: 
            cursor = self.__connexion.cursor()
            cursor.execute('INSERT INTO (`cathegorie`, `Question1`, `Question2`,`Question3`,`Question4`,`Question5`,`Question6`) VALUES (?, ?, ?, ?, ?, ?, ?);',(liste_Questions[0], liste_Questions[1], liste_Questions[2], liste_Questions[3], liste_Questions[4], liste_Questions[5], liste_Questions[6],))
            self.__connexion.commit()
            return self.afficher_categrorie(nouvelle_donnees[0], nouvelle_donnees[1],nouvelle_donnees[2], nouvelle_donnees[3],nouvelle_donnees[4], nouvelle_donnees[5],liste_Questions[6],)
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '

# Permettre de supprimer une categorie
    def supprimeQuestion(self,Questionsid):
        try :
            ID_Question_supprimer = input('Quel est ID de la question a supprimer')
            cursor = self.__connexion.cursor()
            cursor.execute('DELETE FROM questionnaire WHERE questionid = ?;',(ID_Question_supprimer,))
            self.__connexion.commit()
            return 'La question a bien été supprimée'
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '
