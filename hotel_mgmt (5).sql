-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 21, 2018 at 01:47 PM
-- Server version: 5.6.34-log
-- PHP Version: 7.1.5

SET SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO';
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = '+00:00';


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: hotel mgmt
--
CREATE DATABASE IF NOT EXISTS hotel_mgmt ;
USE hotel_mgmt;

DELIMITER $$
--
-- Procedures
--
DROP PROCEDURE IF EXISTS autocusid$$
CREATE DEFINER=root@localhost PROCEDURE autocusid (OUT res INT)  NO SQL
BEGIN
select max(k.userid)+1 into @x
from customer as k; 
IF @x IS NULL THEN
	SET @x = 1;
END IF;
SET res=@x;
END$$

DROP PROCEDURE IF EXISTS autoroomno$$
CREATE DEFINER=root@localhost PROCEDURE autoroomno (OUT res INT)  NO SQL
BEGIN
select max(k.roomno)+1 into @x
from customer as k; 
IF @x IS NULL THEN
	SET @x = 1;
END IF;
SET res=@x;
END$$

DELIMITER ;

-- --------------------------------------------------------
DROP TABLE IF EXISTS receptionist;
CREATE TABLE receptionist (
  rec_id int(10)  primary key,
  rec_name varchar(20) NOT NULL,
  rec_address varchar(45) NOT NULL,
  email varchar(45) NOT NULL, 
  salary float(10) not NULL);


--
-- Table structure for table customer
--

DROP TABLE IF EXISTS customer;
CREATE TABLE customer (
  firstname varchar(20) NOT NULL,
  lastname varchar(20) NOT NULL,
  user_address varchar(45) NOT NULL,
  email varchar(45) NOT NULL,  
  checkindate varchar(30) NOT NULL,
  r_type varchar(30) NOT NULL,
  checkoutdate varchar(30) NOT NULL,
  country varchar(45) NOT NULL,
  userid int(11) NOT NULL,
  Noofdays int(11) NOT NULL,
  bill float(10) not NULL,
  rno int(11) UNIQUE not null 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table customer
--

INSERT INTO customer (firstname,lastname,email, user_address,country, checkindate, checkoutdate,Noofdays,rno,userid,bill,r_type) VALUES
('ram','kannan','xxx','abc','India', '02/09/2020', '09/09/2020',7,1800,1,2500,'Double cot'),
('kishore', 'hjjj','yyy','abc','India', '02/09/2020', '05/09/2020',3,200,2,5000,'Double cot');
--
-- Dumping data for table menu



DROP TABLE IF EXISTS rooms;
CREATE TABLE rooms (
  userid int(11) NOT NULL,
  r_type varchar(20) NOT NULL,
  bill float(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table rooms
--

INSERT INTO rooms (userid, r_type, bill) VALUES
(1, 'Double', 2500),
(2, 'Double', 6000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table customer
--
ALTER TABLE customer
  ADD PRIMARY KEY (userid);



--
ALTER TABLE rooms
  ADD PRIMARY KEY (userid,r_type),
  ADD KEY rooms_ibfk_1 (r_type);

--
-- Constraints for dumped tables
--


ALTER TABLE rooms
  ADD CONSTRAINT rooms_ibfk_2 FOREIGN KEY (userid) REFERENCES customer (userid) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
