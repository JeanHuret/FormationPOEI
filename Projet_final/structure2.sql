CREATE DATABASE if not exists questionnaire;
  
USE questionnaire

CREATE TABLE IF NOT EXISTS categorie (

`categorieid` INT(10) AUTO_INCREMENT PRIMARY KEY,

`nom` VARCHAR(256) NOT NULL,

'questionnaire' VARCHAR(256),

);


CREATE TABLE IF NOT EXISTS question (

`questionid` INT(10) AUTO_INCREMENT PRIMARY KEY,
    
`question1`VARCHAR(256),

`question2`VARCHAR(256),

`question3`VARCHAR(256),

`question4`VARCHAR(256),

`question5`VARCHAR(256),

`question6`VARCHAR(256),
    
FOREIGN KEY (`categorieid`) REFERENCES 'questionnaire' (`id`) ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS q1reponse (

`reponseid` INT(10) AUTO_INCREMENT PRIMARY KEY,
    
`reponse1`VARCHAR(256),

`reponse2`VARCHAR(256),

`reponse3`VARCHAR(256),    
FOREIGN KEY (`questionid`) REFERENCES 'question' (`id`) ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS q2reponse2 (

`reponseid` INT(10) AUTO_INCREMENT PRIMARY KEY,
    
`reponse1`VARCHAR(256),

`reponse2`VARCHAR(256),

`reponse3`VARCHAR(256),    
FOREIGN KEY (`questionid`) REFERENCES 'question' (`id`) ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS q3reponse3 (

`reponseid` INT(10) AUTO_INCREMENT PRIMARY KEY,
    
`reponse1`VARCHAR(256),

`reponse2`VARCHAR(256),

`reponse3`VARCHAR(256),    
FOREIGN KEY (`questionid`) REFERENCES 'question' (`id`) ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS q4reponse4 (

`reponseid` INT(10) AUTO_INCREMENT PRIMARY KEY,
    
`reponse1`VARCHAR(256),

`reponse2`VARCHAR(256),

`reponse3`VARCHAR(256),    
FOREIGN KEY (`questionid`) REFERENCES 'question' (`id`) ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS q5reponse5 (

`reponseid` INT(10) AUTO_INCREMENT PRIMARY KEY,
    
`reponse1`VARCHAR(256),

`reponse2`VARCHAR(256),

`reponse3`VARCHAR(256),    
FOREIGN KEY (`questionid`) REFERENCES 'question' (`id`) ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS q6reponse6 (

`reponseid` INT(10) AUTO_INCREMENT PRIMARY KEY,
    
`reponse1`VARCHAR(256),

`reponse2`VARCHAR(256),

`reponse3`VARCHAR(256),    
FOREIGN KEY (`questionid`) REFERENCES 'question' (`id`) ON DELETE CASCADE

);
