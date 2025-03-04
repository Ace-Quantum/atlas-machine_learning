-- script that creates a table of users

DROP TABLE IF EXISTS 'users';

CREATE TABLE users(
    id int NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    PRIMARY KEY (id)
);