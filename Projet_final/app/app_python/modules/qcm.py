from secrets import choice
from click import echo
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
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM QCM')
        liste_qcm = cursor.fetchall()
        return liste_qcm


    def saisie_data_qcm(self, liste_qcm = []):
        if liste_qcm:
            liste_qcm = Qcm(liste_qcm)
            qcm_id = input('Quel est l\'id du qcm?('+str(liste_qcm[1])+')' ) or liste_qcm[1] 
            categorie = input('Quel est la categorie?('+str(liste_qcm[2])+')') or liste_qcm[2] 
            categorie_id = input('Quel est la categorie_id?('+str(liste_qcm[2])+')') or liste_qcm[3] 
            question = input('Quel est la question?('+str(liste_qcm[2])+')') or liste_qcm[4] 
            reponse1 = input('Quel est la premiere reponse possible a la question?('+str(liste_qcm[3])+')') or liste_qcm[5] 
            reponse2 = input('Quel est la deuxieme reponse possible a la question?('+str(liste_qcm[4])+')') or liste_qcm[6]
            reponse3 = input('Quel est la troisieme reponse possible a la question?('+str(liste_qcm[5])+')') or liste_qcm[7]
            ancien_id = liste_qcm[0]
            liste_qcm[0] = qcm_id
            liste_qcm[1] = categorie
            liste_qcm[2] = categorie_id
            liste_qcm[3] = question
            liste_qcm[4] = reponse1
            liste_qcm[5] = reponse2
            liste_qcm[6] = reponse3
            liste_qcm[7] = ancien_id

        else:
            qcm_id = int(input('Quel est l\'id du qcm?'))
            categorie = input('Quel est la categorie?')
            categorie_id = int(input('Quel est la categorie_id?'))
            question = input('Quel est la question?') 
            reponse1 = input('Quel est la premiere reponse possible a la question?')
            reponse2 = input('Quel est la deuxieme reponse possible a la question?')
            reponse3 = input('Quel est la troisieme reponse possible a la question?')
            liste_qcm.append(qcm_id)
            liste_qcm.append(categorie)
            liste_qcm.append(categorie_id)
            liste_qcm.append(question)
            liste_qcm.append(reponse1)
            liste_qcm.append(reponse2)
            liste_qcm.append(reponse3)

        return liste_qcm

    # • Permettre l’ajout d’une application
    def ajouter_data_qcm(self, liste_qcm):
        print(liste_qcm)
        try:
            cursor = self.__connexion.cursor()
            cursor.execute('INSERT INTO QCM ( `categorie`, `categorie_id`, `question`, `reponse1`, `reponse2`, `reponse3`)  VALUES (?, ?, ?, ?, ?, ?);',(liste_qcm[1], liste_qcm[2], liste_qcm[3], liste_qcm[4], liste_qcm[5], liste_qcm[6]))
            self.__connexion.commit()
            return 'La question a bien été ajoutée'
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '

    def trouver_data_qcm(self, qcm_id):
        cursor = self.__connexion.cursor()
        cursor.execute('SELECT * FROM QCM WHERE qcm_id = ?;',(qcm_id,))
        qcm_a_afficher = cursor.fetchone()
        return qcm_a_afficher

    # Permettre de récupérer les informations d’une application en saisissant son hostname
    def voir_data_qcm(self, qcm_id) :
        qcm_a_afficher = self.trouver_data_qcm(qcm_id)
        return qcm_a_afficher
    
    # Permettre de modifier une application à partir de son hostname
    def modifier_data_qcm(self, nouvelle_donnees):
        print(nouvelle_donnees)
        try: 
            cursor = self.__connexion.cursor()
            cursor.execute('UPDATE QCM SET `categorie` = ?, `categorie_id` = ?, `question` = ?, `reponse1` = ?, `reponse2` = ?, `reponse3` = ? WHERE `qcm_id` = ?;',(nouvelle_donnees[1], nouvelle_donnees[2], nouvelle_donnees[3], nouvelle_donnees[4], nouvelle_donnees[5], nouvelle_donnees[6], nouvelle_donnees[0]))
            self.__connexion.commit()
            return self.voir_data_qcm(nouvelle_donnees[0])
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '

    # Permettre de supprimer une application
    def supprimer_data_qcm(self, qcm_id):
        try :
            cursor = self.__connexion.cursor()
            cursor.execute('DELETE FROM QCM WHERE qcm_id = ?;',(qcm_id,))
            self.__connexion.commit()
            return 'La question a bien été supprimée'
        except mariadb.Error as e:     
            return f'Erreur lors de la suppression {e} '
    
    # répondre au QCM
    def repondre_qcm(self, question):
        for qcm in question:
            print(qcm["question"])
            for answer in question["answers"].split(","):
                print("- ", answer)
            user_answer = input("Write the corrert answer: ")
            # loop back if answers is not in answers
            if user_answer == question["correct_answer"]:
                print("You are correct!")
            else:
                print("Sorry but the correct answer was ", 
                question["correct_answer"])
            print("\n")
