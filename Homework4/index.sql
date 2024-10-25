-- database and table dropping 
drop database if exists homework4;

-- creating database, followed by the table 
create database homework4;

use homework4;

-- creating  Employee table 
create table if not exists Employee(
    ID int primary key,
    EFname varchar(45),
    ELname  varchar(45),
    Salary decimal(10,2),
    Sex char(1), 
    BirthDay date, 
    BranchID int
);



-- branch table 
CREATE TABLE IF NOT EXISTS Branch (
    ID INT PRIMARY KEY,
    BranchName VARCHAR(45),
    EmpID INT
);

create table if not exists WorkBranch(
	EmpID INT,
    BranchID INT,
    
    primary key(EmpID, BranchID),
	FOREIGN key (BranchID) references Branch(ID),
	FOREIGN KEY (EmpID) REFERENCES Employee(ID)
);

-- creting client table 
create table if not exists Client (
    ID int primary key, 
    ClientName varchar(45)
);


-- workwith relation table
create table if not exists workWith(
    clientID int, 
    EmployeeID int,
    SoldProduct varchar(45),

    primary key(clientID, EmployeeID),

    foreign key (EmployeeID) references Employee(ID),
    foreign key (clientID) references Client(ID)
); 

create TABLE if not EXISTS BranchSupply(
    ptype varchar(45),
    cname varchar(45),

    primary key(ptype, cname)
)
