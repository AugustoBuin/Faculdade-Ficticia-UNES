DROP DATABASE IF EXISTS d20; 

CREATE DATABASE d20; 

USE d20; 

CREATE TABLE tb_contato (
    id_contato INT PRIMARY KEY AUTO_INCREMENT, 
    email VARCHAR(255) NOT NULL, 
    assunto VARCHAR(255) NOT NULL, 
    descricao VARCHAR(1025) , 
)