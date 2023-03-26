DROP TABLE IF EXISTS companies;

CREATE TABLE IF NOT EXISTS companies (
  Index INT,
  Id VARCHAR(255) UNIQUE,
  Name VARCHAR(255) NOT NULL,
  Website VARCHAR(255),
  Country VARCHAR(255),
  Description VARCHAR(255),
  Founded INT,
  Industry VARCHAR(255),
  Employees INT
);