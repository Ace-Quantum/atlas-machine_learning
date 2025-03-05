-- creates the table "user" which probably 
-- should have happened before that last one-- script that creates a table of users

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id)
);