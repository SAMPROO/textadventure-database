-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.2.10-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping structure for table textadventure-empty-data.answer
CREATE TABLE IF NOT EXISTS `answer` (
  `answer_id` int(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  `previous_answer_line_id` int(20) DEFAULT NULL,
  `next_answer_line_id` int(20) DEFAULT NULL,
  PRIMARY KEY (`answer_id`),
  KEY `FK_answer_line` (`previous_answer_line_id`),
  KEY `FK_answer_line_2` (`next_answer_line_id`),
  CONSTRAINT `FK_answer_line` FOREIGN KEY (`previous_answer_line_id`) REFERENCES `line` (`line_id`),
  CONSTRAINT `FK_answer_line_2` FOREIGN KEY (`next_answer_line_id`) REFERENCES `line` (`line_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-empty-data.answer: ~0 rows (approximately)
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;

-- Dumping structure for table textadventure-empty-data.character
CREATE TABLE IF NOT EXISTS `character` (
  `character_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) DEFAULT NULL,
  `hp` int(10) NOT NULL DEFAULT 0,
  `max_hp` int(10) NOT NULL DEFAULT 0,
  `attack` int(5) NOT NULL DEFAULT 0,
  `defence` int(5) NOT NULL DEFAULT 0,
  `money` int(5) NOT NULL DEFAULT 0,
  `alive` tinyint(4) NOT NULL DEFAULT 0,
  `inventory` int(10) NOT NULL DEFAULT 0,
  `location_id` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`character_id`),
  KEY `FK__location` (`location_id`),
  CONSTRAINT `FK__location` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-empty-data.character: ~0 rows (approximately)
/*!40000 ALTER TABLE `character` DISABLE KEYS */;
/*!40000 ALTER TABLE `character` ENABLE KEYS */;

-- Dumping structure for table textadventure-empty-data.direction
CREATE TABLE IF NOT EXISTS `direction` (
  `direction_id` char(1) NOT NULL,
  `direction` varchar(10) NOT NULL,
  PRIMARY KEY (`direction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-empty-data.direction: ~0 rows (approximately)
/*!40000 ALTER TABLE `direction` DISABLE KEYS */;
/*!40000 ALTER TABLE `direction` ENABLE KEYS */;

-- Dumping structure for table textadventure-empty-data.item
CREATE TABLE IF NOT EXISTS `item` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `description` varchar(50) NOT NULL,
  `attack` int(5) DEFAULT 0,
  `defence` int(5) DEFAULT 0,
  `money` int(5) DEFAULT 0,
  `addhp` int(5) DEFAULT 0,
  `pickable` tinyint(4) DEFAULT NULL,
  `weight` int(5) DEFAULT NULL,
  `item_location_id` int(11) NOT NULL,
  `item_character_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  KEY `FK_item_location` (`item_location_id`),
  KEY `FK_item_character` (`item_character_id`),
  CONSTRAINT `FK_item_character` FOREIGN KEY (`item_character_id`) REFERENCES `character` (`character_id`),
  CONSTRAINT `FK_item_location` FOREIGN KEY (`item_location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-empty-data.item: ~0 rows (approximately)
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
/*!40000 ALTER TABLE `item` ENABLE KEYS */;

-- Dumping structure for table textadventure-empty-data.line
CREATE TABLE IF NOT EXISTS `line` (
  `line_id` int(11) NOT NULL AUTO_INCREMENT,
  `line` varchar(100) NOT NULL DEFAULT '1',
  `line_npc_id` int(11) NOT NULL,
  PRIMARY KEY (`line_id`),
  KEY `FK__npc` (`line_npc_id`),
  CONSTRAINT `FK__npc` FOREIGN KEY (`line_npc_id`) REFERENCES `npc` (`npc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-empty-data.line: ~0 rows (approximately)
/*!40000 ALTER TABLE `line` DISABLE KEYS */;
/*!40000 ALTER TABLE `line` ENABLE KEYS */;

-- Dumping structure for table textadventure-empty-data.location
CREATE TABLE IF NOT EXISTS `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `location_name` varchar(20) NOT NULL DEFAULT 'Room',
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-empty-data.location: ~0 rows (approximately)
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
/*!40000 ALTER TABLE `location` ENABLE KEYS */;

-- Dumping structure for table textadventure-empty-data.locnpc
CREATE TABLE IF NOT EXISTS `locnpc` (
  `locnpc_npc_id` int(11) DEFAULT NULL,
  `locnpc_loc_id` int(11) DEFAULT NULL,
  KEY `FK_locnpc_npc` (`locnpc_npc_id`),
  KEY `FK_locnpc_location` (`locnpc_loc_id`),
  CONSTRAINT `FK_locnpc_location` FOREIGN KEY (`locnpc_loc_id`) REFERENCES `location` (`location_id`),
  CONSTRAINT `FK_locnpc_npc` FOREIGN KEY (`locnpc_npc_id`) REFERENCES `npc` (`npc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-empty-data.locnpc: ~0 rows (approximately)
/*!40000 ALTER TABLE `locnpc` DISABLE KEYS */;
/*!40000 ALTER TABLE `locnpc` ENABLE KEYS */;

-- Dumping structure for table textadventure-empty-data.neighbours
CREATE TABLE IF NOT EXISTS `neighbours` (
  `from_location_id` int(11) DEFAULT NULL,
  `to_location_id` int(11) DEFAULT NULL,
  `neighbour_direction_id` char(1) DEFAULT NULL,
  KEY `FK_neighbours_location` (`from_location_id`),
  KEY `FK_neighbours_direction` (`neighbour_direction_id`),
  KEY `FK_neighbours_location_2` (`to_location_id`),
  CONSTRAINT `FK_neighbours_direction` FOREIGN KEY (`neighbour_direction_id`) REFERENCES `direction` (`direction_id`),
  CONSTRAINT `FK_neighbours_location` FOREIGN KEY (`from_location_id`) REFERENCES `location` (`location_id`),
  CONSTRAINT `FK_neighbours_location_2` FOREIGN KEY (`to_location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-empty-data.neighbours: ~0 rows (approximately)
/*!40000 ALTER TABLE `neighbours` DISABLE KEYS */;
/*!40000 ALTER TABLE `neighbours` ENABLE KEYS */;

-- Dumping structure for table textadventure-empty-data.npc
CREATE TABLE IF NOT EXISTS `npc` (
  `npc_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL DEFAULT 'NPC',
  `description` varchar(50) NOT NULL,
  `maxhp` int(5) NOT NULL,
  `line_counter` int(5) NOT NULL,
  PRIMARY KEY (`npc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-empty-data.npc: ~0 rows (approximately)
/*!40000 ALTER TABLE `npc` DISABLE KEYS */;
/*!40000 ALTER TABLE `npc` ENABLE KEYS */;

-- Dumping structure for table textadventure-empty-data.npctype
CREATE TABLE IF NOT EXISTS `npctype` (
  `npctype_npc_id` int(11) DEFAULT NULL,
  `npctype_id` int(11) DEFAULT NULL,
  KEY `FK_npctype_type` (`npctype_id`),
  KEY `FK_npctype_npc` (`npctype_npc_id`),
  CONSTRAINT `FK_npctype_npc` FOREIGN KEY (`npctype_npc_id`) REFERENCES `npc` (`npc_id`),
  CONSTRAINT `FK_npctype_type` FOREIGN KEY (`npctype_id`) REFERENCES `type` (`type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-empty-data.npctype: ~0 rows (approximately)
/*!40000 ALTER TABLE `npctype` DISABLE KEYS */;
/*!40000 ALTER TABLE `npctype` ENABLE KEYS */;

-- Dumping structure for table textadventure-empty-data.type
CREATE TABLE IF NOT EXISTS `type` (
  `type_id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  `defence` int(5) DEFAULT NULL,
  `attack` int(5) DEFAULT NULL,
  `friendly` tinyint(4) DEFAULT NULL,
  `hp` int(5) DEFAULT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-empty-data.type: ~0 rows (approximately)
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
/*!40000 ALTER TABLE `type` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
