import mariadb

class Qcm:

    def __init__(self, connexion) -> None:
        # Propriété de l'objet application
        self.__qcm_id = ''
        self.__categorie = ''
        self.__categorie_id = ''
        self.__question = ''
        self.__reponse1 = ''
        self.__reponse2 = ''
        self.__reponse3 = ''
        self.__connexion = connexion


    def get_qcm_id(self):
        return self.__qcm_id

    def set_qcm_id(self, qcm_id):
        if isinstance(qcm_id, str): 
            self.__qcm_id = qcm_id

    def get_categorie(self):
        return self.__categorie

    def set_categorie(self, categorie):
        if isinstance(categorie, str): 
            self.__categorie = categorie

    def get_categorie_id(self):
        return self.__categorie_id

    def set_categorie_id(self, categorie_id):
        if isinstance(categorie_id, str): 
            self.__categorie_id = categorie_id

    def get_question(self):
        return self.__question

    def set_question(self, question):
        if isinstance(question, str): 
            self.__question = question
    
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

    # Lister les questionnaire avec les caractéristiques suivantes : 
    def liste_data_qcm(self):
        cursor = self.__data_qcm.cursor()
        cursor.execute('SELECT * FROM QCM;')
        liste_questionnaire = cursor.fetchall()
        return liste_questionnaire


    def saisie_data_qcm(self, liste_donnees = []):
        if liste_donnees:
            liste_donnees = list(liste_donnees)
            qcm_id = input('Quel est l\'id du qcm?('+str(liste_donnees[1])+')' ) or liste_donnees[1] 
            categorie = input('Quel est la categorie?('+str(liste_donnees[2])+')') or liste_donnees[2] 
            categorie_id = input('Quel est la categorie_id?('+str(liste_donnees[2])+')') or liste_donnees[3] 
            question = input('Quel est la question?('+str(liste_donnees[2])+')') or liste_donnees[4] 
            reponse1 = input('Quel est la premiere reponse possible a la question?('+str(liste_donnees[3])+')') or liste_donnees[5] 
            reponse2 = input('Quel est la deuxieme reponse possible a la question?('+str(liste_donnees[4])+')') or liste_donnees[6]
            reponse3 = input('Quel est la troisieme reponse possible a la question?('+str(liste_donnees[5])+')') or liste_donnees[7]
            ancien_id = liste_donnees[0]
            liste_donnees[0] = qcm_id
            liste_donnees[1] = categorie
            liste_donnees[2] = categorie_id
            liste_donnees[3] = question
            liste_donnees[4] = reponse1
            liste_donnees[5] = reponse2
            liste_donnees[6] = reponse3
            liste_donnees[7] = ancien_id

        else: 
            qcm_id = input('Quel est l\'id du questionnaire?')
            categorie = input('Quel est la categorie?')
            categorie_id = input('Quel est la categorie_id?')
            question = input('Quel est la question?') 
            reponse1 = input('Quel est la premiere reponse possible a la question?')
            reponse2 = input('Quel est la deuxieme reponse possible a la question?')
            reponse3 = input('Quel est la troisieme reponse possible a la question?')
            liste_donnees.append(qcm_id)
            liste_donnees.append(categorie)
            liste_donnees.append(categorie_id)
            liste_donnees.append(question)
            liste_donnees.append(reponse1)
            liste_donnees.append(reponse2)
            liste_donnees.append(reponse3)

        return liste_donnees

    # • Permettre l’ajout d’une application
    def ajouter_data_qcm(self, liste_donnees):
        try:
            cursor = self.__connexion.cursor()
            cursor.execute('INSERT INTO QCM ( `categorie`, `categorie_id`, `question`, `reponse1`, `reponse2`, `reponse3`)  VALUES (?, ?, ?, ?, ?, ?);',(liste_donnees[0], liste_donnees[1], liste_donnees[2], liste_donnees[3], liste_donnees[4], liste_donnees[5], liste_donnees[6]))
            self.__connexion.commit()
            return 'La question a bien été ajoutée'
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '


    def trouver_data_qcm(self,questionnaire):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM QCM WHERE qcm_id = ?;',(questionnaire,))
        qcm_a_afficher = cursor.fetchone()
        return qcm_a_afficher

    # Permettre de récupérer les informations d’une application en saisissant son hostname
    def voir_data_qcm(self, questionnaire) :
        qcm_a_afficher = self.trouver_unqcm(questionnaire)
        return qcm_a_afficher
    
    # Permettre de modifier une application à partir de son hostname
    def modifier_data_qcm(self, nouvelle_donnees):
        print(nouvelle_donnees)
        try: 
            cursor = self.__connexion.cursor()
            cursor.execute('UPDATE QCM SET `categorie` = ?, `categorie_id` = ?, `question` = ?, `reponse1` = ?, `reponse2` = ?, `reponse3` = ? WHERE `qcm_id` = ?;',(nouvelle_donnees[1], nouvelle_donnees[2], nouvelle_donnees[3], nouvelle_donnees[4], nouvelle_donnees[5], nouvelle_donnees[6], nouvelle_donnees[0],))
            self.__connexion.commit()
            return self.voir_data_qcm(nouvelle_donnees[0])
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '

    # Permettre de supprimer une application
    def supprimer_data_qcm(self, questionnaire):
        try :
            cursor = self.__connexion.cursor()
            cursor.execute('DELETE FROM QCM WHERE qcm_id = ?;',(questionnaire,))
            self.__connexion.commit()
            return 'La question a bien été supprimée'
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '
