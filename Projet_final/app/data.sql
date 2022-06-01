CREATE DATABASE if not exists questionnaire;
  
USE questionnaire;

CREATE TABLE IF NOT EXISTS QCM (

    `qcm_id` INT(10) AUTO_INCREMENT PRIMARY KEY,

    `categorie_id` INT(10) AUTO_INCREMENT,

    `categorie` VARCHAR(256),

    `Question1` VARCHAR(256),

    `Reponse1` VARCHAR(256),

    `Reponse1bis` VARCHAR(256),

    `Reponse1ter` VARCHAR(256),

    `Question2` VARCHAR(256),

    `Reponse2` VARCHAR(256),

    `Reponse2bis` VARCHAR(256),

    `Reponse2ter` VARCHAR(256),

    `Question3` VARCHAR(256),

    `Reponse3` VARCHAR(256),

    `Reponse3bis` VARCHAR(256),

    `Reponse3ter` VARCHAR(256),

    `Question4` VARCHAR(256),

    `Reponse4` VARCHAR(256),

    `Reponse4bis` VARCHAR(256),

    `Reponse4ter` VARCHAR(256),

    `Question5` VARCHAR(256),

    `Reponse5` VARCHAR(256),

    `Reponse5bis` VARCHAR(256),

    `Reponse5ter` VARCHAR(256),

    `Question6` VARCHAR(256),

    `Reponse6` VARCHAR(256),

    `Reponse6bis` VARCHAR(256),

    `Reponse6ter` VARCHAR(256)

);
INSERT INTO QCM(qcm_id,categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('0000','geographie','001','Quelle est la capitale de France','Lyon','Paris','Lisbonne');
INSERT INTO QCM(qcm_id,categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('1000','Traduction','002','Comment dit-on salut en Anglais','Enrevoir','Hello','Jacket');
INSERT INTO QCM(qcm_id,categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('0001','geographie','001','Combien d étoile possède le drapeau européen','2','12','30');
INSERT INTO QCM(qcm_id,categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('4000','nature','003','Combien d espece d insecte a t on découvert à ce jour','500 000','1 million','Plus de 5 millions');
INSERT INTO QCM(qcm_id,categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('3000','geek','004','En quelle année est sortie la 1er console salon de jeux vidéo','1982','1972','1990');
INSERT INTO QCM(qcm_id,categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('3001','geek','004','En quelle année est sortie la console nes','1975','1983','1991');
INSERT INTO QCM(qcm_id,categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('2000','histoire','005','En quelle année le TITANIC a t il coulé','2010','1912','1850');
INSERT INTO QCM(qcm_id,categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('2001','histoire','005','Dans quel pays se trouve les jardins suspendus de Babylone (1 des 7 merveilles)','Iran','Irak','Bilbéis');
INSERT INTO QCM(qcm_id,categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('4001','nature','003','Combien de couleur y a til dans l arc en ciel','10','7','5');
INSERT INTO QCM(qcm_id,categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('0002','geographie','001','Dans qulle ville de france se situe la tour effeil','Lyon','Paris','Marseille');
INSERT INTO QCM(qcm_id,categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('5000','sport','006','En quelle année la france remporte t ell la premiere coupe du monde','2000','1998','1990');
INSERT INTO QCM(qcm_id,categorie,categorie_id,question,reponse1,reponse2,reponse3) VALUES ('5449','sdsds','054','eded','sdd','ffdffg','fgdfgfd');

CREATE TABLE IF NOT EXISTS utilisateurs (

    `id` INT(10) AUTO_INCREMENT PRIMARY KEY,
    `pseudo` VARCHAR(256) NOT NULL,
    `prenom` VARCHAR(256) NOT NULL,
    `nom` VARCHAR(256) NOT NULL,
    `role` VARCHAR(256) NOT NULL,
    `email` VARCHAR(256) NOT NULL,
    `mot_de_passe` VARCHAR(16)

);
