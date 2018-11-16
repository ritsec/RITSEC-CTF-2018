CREATE DATABASE challenge;
USE challenge;

CREATE TABLE test (
    username varchar(15),
    passwd varchar(40),
    CONSTRAINT test_pk PRIMARY KEY(username)
);

INSERT INTO test (username, passwd) VALUES
('joe', 'bob'),
('rick', 'james'),
('bobby', 'hunter2'),
('flag', 'RITSEC{fucking_sucks}');

CREATE USER 'webserver'@'%' IDENTIFIED BY 'password2';
GRANT SELECT ON challenge.* to 'webserver'@'%';

FLUSH PRIVILEGES;