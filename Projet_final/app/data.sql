CREATE DATABASE IF NOT EXISTS data_qcm;
USE data_qcm;

CREATE TABLE IF NOT EXISTS QCM (

    `qcm_id` INT(10) AUTO_INCREMENT PRIMARY KEY,

    `categorie` VARCHAR(256),

    `categorie_id` INT(10),

    `question` VARCHAR(256),

    `reponse1` VARCHAR(256),

    `reponse2` VARCHAR(256),

    `reponse3` VARCHAR(256)

);
INSERT INTO QCM(categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('geographie','001','Quelle est la capitale de France','Lyon','Paris','Lisbonne');
INSERT INTO QCM(categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('Traduction','002','Comment dit-on salut en Anglais','Enrevoir','Hello','Jacket');
INSERT INTO QCM(categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('geographie','001','Combien d étoile possède le drapeau européen','2','12','30');
INSERT INTO QCM(categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('nature','003','Combien d espece d insecte a t on découvert à ce jour','500 000','1 million','Plus de 5 millions');
INSERT INTO QCM(categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('geek','004','En quelle année est sortie la 1er console salon de jeux vidéo','1982','1972','1990');
INSERT INTO QCM(categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('geek','004','En quelle année est sortie la console nes','1975','1983','1991');
INSERT INTO QCM(categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('histoire','005','En quelle année le TITANIC a t il coulé','2010','1912','1850');
INSERT INTO QCM(categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('histoire','005','Dans quel pays se trouve les jardins suspendus de Babylone (1 des 7 merveilles)','Iran','Irak','Bilbéis');
INSERT INTO QCM(categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('nature','003','Combien de couleur y a til dans l arc en ciel','10','7','5');
INSERT INTO QCM(categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('geographie','001','Dans qulle ville de france se situe la tour effeil','Lyon','Paris','Marseille');
INSERT INTO QCM(categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('sport','006','En quelle année la france remporte t ell la premiere coupe du monde','2000','1998','1990');
INSERT INTO QCM(categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('sdsds','054','eded','sdd','ffdffg','fgdfgfd');

CREATE TABLE IF NOT EXISTS utilisateurs (

    `id` INT(10) AUTO_INCREMENT PRIMARY KEY,
    `pseudo` VARCHAR(256) NOT NULL,
    `prenom` VARCHAR(256) NOT NULL,
    `nom` VARCHAR(256) NOT NULL,
    `role` VARCHAR(256) NOT NULL,
    `email` VARCHAR(256) NOT NULL,
    `mot_de_passe` VARCHAR(16)

);
