/*
 Navicat Premium Data Transfer

 Source Server         : Local_Server
 Source Server Type    : MySQL
 Source Server Version : 80017
 Source Host           : 127.0.0.1:3306
 Source Schema         : EducationVerification

 Target Server Type    : MySQL
 Target Server Version : 80017
 File Encoding         : 65001

 Date: 07/08/2021 12:32:58
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Edu_Record
-- ----------------------------
DROP TABLE IF EXISTS `Edu_Record`;
CREATE TABLE `Edu_Record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` char(255) NOT NULL,
  `Gender` char(64) NOT NULL,
  `University` char(255) NOT NULL,
  `Birthday` date NOT NULL,
  `AdmissionDate` date NOT NULL,
  `isGraduated` tinyint(1) DEFAULT NULL,
  `GraduationDate` date DEFAULT NULL,
  `Classification` char(255) DEFAULT NULL,
  `Style` char(255) DEFAULT NULL,
  `Major` char(255) DEFAULT NULL,
  `isVerify` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
