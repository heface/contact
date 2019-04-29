--1 建库 
CREATE DATABASE `heLocalDB` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci; 

--2 建表 
USE heLocalDB;
CREATE TABLE IF NOT EXISTS Contact( 
    name varchar(20) NOT NULL default '',
    telHome varchar(20), 
    telWork varchar(20), 
    telWork1 varchar(20), 
    telCell varchar(20), 
    telCell1 varchar(20), 
    telCell2 varchar(20), 
    email varchar(30), 
    c_group varchar(100) ,
    qq varchar(30), 
    departmeny varchar(200),
    address varchar(200),
    birthday varchar(200),
    mem varchar(200),
    PRIMARY KEY  (name) 
); 


--3 初始化数据
INSERT INTO Contact (name,telCell) VALUES ('test1', '12345678');
INSERT INTO Contact (name,telCell) VALUES ('test2', '22345678');
