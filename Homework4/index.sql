-- database and table dropping 
drop database homework4;
drop table Branch, Client;

-- creating database, followed by the table 
create database homework4;


-- branch table 
create table if no exists Branch(
    ID primary key int,
    BranchName varchar(45),
    EmpID int,

    foregin key (EmpID) references Employee (ID)
);


-- creting client table 
create table if not exists Client (
    ID int primary key, 
    ClientName varchar(45)
);


-- creating  Employee table 
create table if not exists Employee(
    ID int primary key,
    EFname varchar(45),
    ELname  varchar(45),
    Salary decimal(10,2),
    Sex char(1), 
    BirthDay date, 
    BranchID int,

    foregin key (BranchID) references Branch(ID)
);


-- workwith relation table
create table if not exists workWith(
    clientID int, 
    EmployeeID int,
    SoldProduct varchar(45),

    foregin key ()
) 
