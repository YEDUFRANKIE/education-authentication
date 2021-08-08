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

 Date: 07/08/2021 12:33:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Search_Set
-- ----------------------------
DROP TABLE IF EXISTS `Search_Set`;
CREATE TABLE `Search_Set` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NOT NULL,
  `block_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_id` (`student_id`),
  KEY `block_id` (`block_id`),
  CONSTRAINT `search_set_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `edu_record` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `search_set_ibfk_2` FOREIGN KEY (`block_id`) REFERENCES `block` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
