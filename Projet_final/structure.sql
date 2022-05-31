CREATE DATABASE if not exists questionnaire;
  
USE questionnaire


CREATE TABLE IF NOT EXISTS categorie (

`categorieid` INT(10) AUTO_INCREMENT PRIMARY KEY,

`categorie` VARCHAR(256) NOT NULL,

);


CREATE TABLE IF NOT EXISTS QCM (

    `QCMid` INT(10) AUTO_INCREMENT PRIMARY KEY,
    
    `categorieID` INT(10),
    
    FOREIGN KEY (categorieID) REFERENCES cathegorie (categorieID)

    `Question1` VARCHAR(256),

    `Réponse1` VARCHAR(256),

    `Question2` VARCHAR(256),

    `Réponse2` VARCHAR(256),

    `Question3` VARCHAR(256),

    `Réponse3` VARCHAR(256),

    `Question4` VARCHAR(256),

    `Réponse4` VARCHAR(256),

    `Question5` VARCHAR(256),

    `Réponse5` VARCHAR(256),

    `Question6` VARCHAR(256),

    `Réponse6` VARCHAR(256),

);



CREATE TABLE IF NOT EXISTS user (

    `id` INT(10) AUTO_INCREMENT PRIMARY KEY,

    `nom` VARCHAR(256) NOT NULL,

    `password` VARCHAR(16),

);
