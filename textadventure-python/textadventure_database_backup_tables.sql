-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.2.9-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping structure for table textadventure_database.answer
CREATE TABLE IF NOT EXISTS `answer` (
  `answer_id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  `answer_line_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`answer_id`),
  KEY `FK__line` (`answer_line_id`),
  CONSTRAINT `FK__line` FOREIGN KEY (`answer_line_id`) REFERENCES `line` (`line_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure_database.answer: ~0 rows (approximately)
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;

-- Dumping structure for table textadventure_database.character
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

-- Dumping data for table textadventure_database.character: ~1 rows (approximately)
/*!40000 ALTER TABLE `character` DISABLE KEYS */;
INSERT INTO `character` (`character_id`, `name`, `hp`, `max_hp`, `attack`, `defence`, `money`, `alive`, `inventory`, `location_id`) VALUES
	(1, 'Traveller', 100, 100, 10, 10, 0, 1, 0, 1);
/*!40000 ALTER TABLE `character` ENABLE KEYS */;

-- Dumping structure for table textadventure_database.direction
CREATE TABLE IF NOT EXISTS `direction` (
  `direction_id` char(1) NOT NULL,
  `direction` varchar(10) NOT NULL,
  PRIMARY KEY (`direction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure_database.direction: ~6 rows (approximately)
/*!40000 ALTER TABLE `direction` DISABLE KEYS */;
INSERT INTO `direction` (`direction_id`, `direction`) VALUES
	('d', 'down'),
	('e', 'east'),
	('n', 'north'),
	('s', 'south'),
	('u', 'up'),
	('w', 'west');
/*!40000 ALTER TABLE `direction` ENABLE KEYS */;

-- Dumping structure for table textadventure_database.item
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

-- Dumping data for table textadventure_database.item: ~1 rows (approximately)
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` (`item_id`, `name`, `description`, `attack`, `defence`, `money`, `addhp`, `pickable`, `weight`, `item_location_id`, `item_character_id`) VALUES
	(1, 'Sword', 'A shiny sword', 10, 0, 0, 0, 1, 10, 2, NULL);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;

-- Dumping structure for table textadventure_database.line
CREATE TABLE IF NOT EXISTS `line` (
  `line_id` int(11) NOT NULL AUTO_INCREMENT,
  `line` varchar(100) NOT NULL,
  `line_npc_id` int(11) NOT NULL,
  PRIMARY KEY (`line_id`),
  KEY `FK__npc` (`line_npc_id`),
  CONSTRAINT `FK__npc` FOREIGN KEY (`line_npc_id`) REFERENCES `npc` (`npc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure_database.line: ~0 rows (approximately)
/*!40000 ALTER TABLE `line` DISABLE KEYS */;
/*!40000 ALTER TABLE `line` ENABLE KEYS */;

-- Dumping structure for table textadventure_database.location
CREATE TABLE IF NOT EXISTS `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL DEFAULT 'Room',
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure_database.location: ~5 rows (approximately)
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` (`location_id`, `name`, `description`) VALUES
	(1, 'Room 1', 'This room is the first room. This room is empty.'),
	(2, 'Room 2', 'The second room. Infront of you, you see a sword.'),
	(3, 'Room 3', 'Room 3 is a big hall.'),
	(4, 'Room 4', 'This room is empty and dark. There are stairs leading down.'),
	(5, 'Room 5', 'This is a basement');
/*!40000 ALTER TABLE `location` ENABLE KEYS */;

-- Dumping structure for table textadventure_database.locnpc
CREATE TABLE IF NOT EXISTS `locnpc` (
  `locnpc_npc_id` int(11) DEFAULT NULL,
  `locnpc_loc_id` int(11) DEFAULT NULL,
  KEY `FK_locnpc_npc` (`locnpc_npc_id`),
  KEY `FK_locnpc_location` (`locnpc_loc_id`),
  CONSTRAINT `FK_locnpc_location` FOREIGN KEY (`locnpc_loc_id`) REFERENCES `location` (`location_id`),
  CONSTRAINT `FK_locnpc_npc` FOREIGN KEY (`locnpc_npc_id`) REFERENCES `npc` (`npc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure_database.locnpc: ~1 rows (approximately)
/*!40000 ALTER TABLE `locnpc` DISABLE KEYS */;
INSERT INTO `locnpc` (`locnpc_npc_id`, `locnpc_loc_id`) VALUES
	(1, 5);
/*!40000 ALTER TABLE `locnpc` ENABLE KEYS */;

-- Dumping structure for table textadventure_database.neighbours
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

-- Dumping data for table textadventure_database.neighbours: ~4 rows (approximately)
/*!40000 ALTER TABLE `neighbours` DISABLE KEYS */;
INSERT INTO `neighbours` (`from_location_id`, `to_location_id`, `neighbour_direction_id`) VALUES
	(1, 2, 'n'),
	(2, 3, 'e'),
	(2, 4, 'w'),
	(4, 5, 'd');
/*!40000 ALTER TABLE `neighbours` ENABLE KEYS */;

-- Dumping structure for table textadventure_database.npc
CREATE TABLE IF NOT EXISTS `npc` (
  `npc_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL DEFAULT 'NPC',
  `maxhp` int(5) NOT NULL,
  `line_counter` int(5) NOT NULL,
  PRIMARY KEY (`npc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure_database.npc: ~1 rows (approximately)
/*!40000 ALTER TABLE `npc` DISABLE KEYS */;
INSERT INTO `npc` (`npc_id`, `name`, `maxhp`, `line_counter`) VALUES
	(1, 'Figure', 100, 3);
/*!40000 ALTER TABLE `npc` ENABLE KEYS */;

-- Dumping structure for table textadventure_database.npctype
CREATE TABLE IF NOT EXISTS `npctype` (
  `npctype_npc_id` int(11) DEFAULT NULL,
  `npctype_id` int(11) DEFAULT NULL,
  KEY `FK_npctype_type` (`npctype_id`),
  KEY `FK_npctype_npc` (`npctype_npc_id`),
  CONSTRAINT `FK_npctype_npc` FOREIGN KEY (`npctype_npc_id`) REFERENCES `npc` (`npc_id`),
  CONSTRAINT `FK_npctype_type` FOREIGN KEY (`npctype_id`) REFERENCES `type` (`type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure_database.npctype: ~1 rows (approximately)
/*!40000 ALTER TABLE `npctype` DISABLE KEYS */;
INSERT INTO `npctype` (`npctype_npc_id`, `npctype_id`) VALUES
	(1, 1);
/*!40000 ALTER TABLE `npctype` ENABLE KEYS */;

-- Dumping structure for table textadventure_database.type
CREATE TABLE IF NOT EXISTS `type` (
  `type_id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  `defence` int(5) DEFAULT NULL,
  `attack` int(5) DEFAULT NULL,
  `friendly` tinyint(4) DEFAULT NULL,
  `hp` int(5) DEFAULT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure_database.type: ~1 rows (approximately)
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
INSERT INTO `type` (`type_id`, `description`, `defence`, `attack`, `friendly`, `hp`) VALUES
	(1, 'Dark figure', 10, 10, 1, 100);
/*!40000 ALTER TABLE `type` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
