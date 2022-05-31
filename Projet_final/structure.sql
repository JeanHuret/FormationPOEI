CREATE DATABASE if not exists questionnaire;
  
USE questionnaire


CREATE TABLE IF NOT EXISTS categorie (

`categorieid` INT(10) AUTO_INCREMENT PRIMARY KEY,

`categorie` VARCHAR(256) NOT NULL,

);


CREATE TABLE IF NOT EXISTS QCM (

    `QCMid` INT(10) AUTO_INCREMENT PRIMARY KEY,
    
    `categorieID` INT(10),
    
    FOREIGN KEY (categorieID) REFERENCES categorie (categorieID)

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

    `Reponse6ter` VARCHAR(256),

);


CREATE TABLE IF NOT EXISTS utilisateur (

    `id` INT(10) AUTO_INCREMENT PRIMARY KEY,
    `pseudo` VARCHAR(256) NOT NULL,
    `prenom` VARCHAR(256) NOT NULL,
    `nom` VARCHAR(256) NOT NULL,
    `role` VARCHAR(256) NOT NULL,
    `email` VARCHAR(256) NOT NULL,
    `password` VARCHAR(16),

);
