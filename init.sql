-- 1 建库 
CREATE DATABASE `heLocalDB` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci; 

-- 2 建表 
USE heLocalDB;
CREATE TABLE IF NOT EXISTS Contact(
    `id` bigint(20) NOT NULL AUTO_INCREMENT,                 -- 唯一ID
    `name` varchar(20) NOT NULL default '',-- 姓名
    `telHome` varchar(20),  -- 家庭电话
    `telWork` varchar(20),  -- 工作电话
    `telWork1` varchar(20),  
    `telCell` varchar(20),  -- 移动电话
    `telCell1` varchar(20), 
    `telCell2` varchar(20), 
    `email` varchar(100),   -- email地址
    `c_group` varchar(100) ,-- 分组
    `qq` varchar(30),       -- QQ号
    `department` varchar(100), -- 部门
    `team` varchar(100),       -- 团队
    `address` varchar(200),    -- 地址
    `birthday` varchar(20),    -- 生日
    `mem` varchar(200),        -- 备注 
    `flag` varchar(10),        -- 来源标识 android-手机通讯录 - contact
    PRIMARY KEY  (`id`),
    KEY `name`(`name`),
    KEY `telHome`(`telHome`),
    KEy `telWork`(`telWork`)
);

-- 3 初始化数据
INSERT INTO Contact (name,telCell) VALUES ('test1', '12345678');
INSERT INTO Contact (name,telCell) VALUES ('test2', '22345678');
