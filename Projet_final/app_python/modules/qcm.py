import mariadb

class Questionnaire:

    def __init__(self, utilisateur,connexion) -> None:
        # Propriete de l'objet questionnaire
        self.__IDQuestionnaire = ''
        self.__categorie = ''
        self.__Question1 = ''
        self.__Reponse1 = ''
        self.__Question2 = ''
        self.__Reponse2 = ''
        self.__Question3= ''
        self.__Reponse3 = ''
        self.__Question4 = ''
        self.__Reponse4 = ''
        self.__Question5 = ''
        self.__Reponse5 = ''
        self.__Question6 = ''
        self.__Reponse6 = ''
        self.__connexion = connexion
        self.__utilisateur = utilisateur
    
    def get_IDQuestionnaire(self):
        return self.__IDQuestionnaire

    def set_IDQuestionnaire(self, IDQuestionnaire):
        if isinstance(IDQuestionnaire, int): 
            self.__IDQuestionnaire = IDQuestionnaire

    def get_categorie(self):
        return self.__categorie

    def set_categorie(self, categorie):
        if isinstance(categorie, str): 
            self.__categorie = categorie
    
    def get_Question1(self):
        return self.__Question1

    def set_Question1(self, Question1):
        if isinstance(Question1, str): 
            self.__Question1 = Question1

    def get_Reponse1(self):
        return self.__Reponse1

    def set_Reponse1(self, Reponse1):
        if isinstance(Reponse1, str): 
            self.__Reponse1 = Reponse1

    def get_Question2(self):
        return self.__Question2

    def set_Question2(self, Question2):
        if isinstance(Question2, str): 
            self.__Question2 = Question2

    def get_Reponse2(self):
        return self.__Reponse2

    def set_Reponse2(self, Reponse2):
        if isinstance(Reponse2, str): 
            self.__Reponse2 = Reponse2

    def get_Question3(self):
        return self.__Question3

    def set_Question3(self, Question3):
        if isinstance(Question3, str): 
            self.__Question3 = Question3
    
    def get_Reponse3(self):
        return self.__Reponse3

    def set_Reponse3(self, Reponse3):
        if isinstance(Reponse3, str): 
            self.__Reponse3 = Reponse3
    
    def get_Question4(self):
        return self.__Question4

    def set_Question4(self, Question4):
        if isinstance(Question4, str): 
            self.__Question4 = Question4

    def get_Reponse4(self):
        return self.__Reponse4

    def set_Reponse4(self, Reponse4):
        if isinstance(Reponse4, str): 
            self.__Reponse4 = Reponse4
    
    def get_Question5(self):
        return self.__Question5

    def set_Question5(self, Question5):
        if isinstance(Question5, str): 
            self.__Question5 = Question5
    
    def get_Reponse5(self):
        return self.__Reponse5

    def set_Reponse5(self, Reponse5):
        if isinstance(Reponse5, str): 
            self.__Reponse5 = Reponse5
    
    def get_Question6(self):
        return self.__Question6

    def set_Question6(self, Question6):
        if isinstance(Question6, str): 
            self.__Question6 = Question6
    
    def get_Reponse6(self):
        return self.__Reponse6

    def set_Reeponse6(self, Reponse6):
        if isinstance(Reponse6, str): 
            self.__Reponse6 = Reponse6
    
    
    
    # Lister les questionnaires avec les caracteristiques suivantes : 
    def liste_categorie(self):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM categorie')
        liste_categorie =  cursor.fetchall()
        return liste_categorie
 

    def saisie_Questionnaire(self):
        liste_donnees = []
        IDQuestionnaire = int(IDQuestionnaire+1)
        cathegorie = input('Quel est la cathegorie du questionnaire?')
        liste_donnees.append(cathegorie)
        Question1 = input('Quel est la Question1 du questionnaire ?')
        liste_donnees.append(Question1)
        Reponse1 = input('Quel est la Reponse1 ?')
        liste_donnees.append(Reponse1)
        Question2 = input('Quel est la Question2 du questionnaire ?')
        liste_donnees.append(Question2)
        Reponse2 = input('Quel est la Reponse2 ?')
        liste_donnees.append(Reponse2)
        Question3 = input('Quel est la Question3 du questionnaire ?')
        liste_donnees.append(Question3)
        Reponse3 = input('Quel est la Reponse3 ?')
        liste_donnees.append(Reponse3)
        Question4 = input('Quel est la Question4 du questionnaire ?')
        liste_donnees.append(Question4)
        Reponse4 = input('Quel est la Reponse4 ?')
        liste_donnees.append(Reponse4)
        Question5 = input('Quel est la Question5 du questionnaire ?')
        liste_donnees.append(Question5)
        Reponse5 = input('Quel est la Reponse5 ?')
        liste_donnees.append(Reponse5)
        Question6 = input('Quel est la Question6 du questionnaire ?')
        liste_donnees.append(Question6)
        Reponse6 = input('Quel est la Reponse6 ?')
        liste_donnees.append(Reponse6)
        return liste_donnees

    # Permettre ajout un questionnaire
    def ajouter_Questionnaire(self, liste_donnees):
        try: 
            cursor = self.__connexion.cursor()
            cursor.execute('INSERT INTO machines ( `categorie`, `Question1`, `Reponse1`, `Question2`, `Reponse2`,`Question3`, `Reponse3`,`Question4`, `Reponse4`,`Question5`, `Reponse5`,`Question6`, `Reponse6`)  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',(liste_donnees[0], liste_donnees[1], liste_donnees[2], liste_donnees[3], liste_donnees[4], liste_donnees[5], liste_donnees[6], liste_donnees[7], liste_donnees[8], liste_donnees[9], liste_donnees[10], liste_donnees[11],liste_donnees[12], liste_donnees[13],))
            return 'Le questionnaire a bien ete ajoute'
        except mariadb.Error as e:     
            return f'Erreur lors de l\'envoie {e} '
