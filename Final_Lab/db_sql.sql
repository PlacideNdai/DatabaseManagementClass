-- Phase #1
-- Drop the database if it already exists
DROP DATABASE IF EXISTS poemdbfinal;

-- Create the database
CREATE DATABASE poemdbfinal;
set global local_infile = 1;

-- Use the database
USE poemdbfinal;

------------------------------- Tables ---------------------------------

-- Artist table (1)
CREATE TABLE artist (
    ID INT auto_increment,
    first_name VARCHAR(60) NOT NULL, 
    last_name VARCHAR(60) NOT NULL, 
    email VARCHAR(100) NOT NULL,
    gender VARCHAR(20),
    birthday DATE NOT NULL,
    PRIMARY KEY (ID)
);

-- Genre table (2)
CREATE TABLE genra (
    ID INT AUTO_INCREMENT,
    name varchar(40) not null, 
    category VARCHAR(60) NOT NULL,
    descs VARCHAR(60) NOT NULL,
    
    
    PRIMARY KEY (ID)
);

-- Poems table (3)
CREATE TABLE poems (
    ID INT AUTO_INCREMENT,
    title VARCHAR(60),
    genra_ID INT NOT NULL,
    poem TEXT,
    PRIMARY KEY (ID),
    FOREIGN KEY (genra_ID) REFERENCES genra(ID)
);

-- Audience table (4)
CREATE TABLE audience (
    ID INT AUTO_INCREMENT,
    first_name VARCHAR(60) NOT NULL,
    last_name VARCHAR(60) NOT NULL,
    email VARCHAR(60) NOT NULL,
    gender VARCHAR(40),
    birthday DATE, 
    passwd VARCHAR(255) NOT NULL,
    
    
    PRIMARY KEY (ID)
);


-- Publisher table (5)
CREATE TABLE publisher (
    ID INT AUTO_INCREMENT,
    name VARCHAR(60),
    phoneNumber VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    PRIMARY KEY (ID)
);

-- Tags table (6)
CREATE TABLE tags (
    ID INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY (ID)
);

-- Events table (7)
CREATE TABLE events (
    ID INT AUTO_INCREMENT,
    name VARCHAR(255),
    city VARCHAR(255), 
    state VARCHAR(90),
    street VARCHAR(255),
    details VARCHAR(255),
    event_data DATE,
    PRIMARY KEY (ID)
);

-- Tickets table (8)
CREATE TABLE tickets (
    ID INT AUTO_INCREMENT,
    price DOUBLE(10,2) NOT NULL,
    seatNumber INT NOT NULL,
    PRIMARY KEY (ID)
);

------------------------- Relationships ----------------------------

-- Sold tickets or buys (10)
CREATE TABLE buys (
    customerID INT,
    whenSold DATETIME,
    ticketID INT,
    FOREIGN KEY (customerID) REFERENCES audience(ID),
    FOREIGN KEY (ticketID) REFERENCES tickets(ID)
);

-- Manages (9)
CREATE TABLE maneges (
    publisherID INT,
    clientID INT, 
    FOREIGN KEY (clientID) REFERENCES artist(ID),
    FOREIGN KEY (publisherID) REFERENCES publisher(ID)
);


-- TESTING 
select * from artist;
select * from genra;
