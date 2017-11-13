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

-- Dumping structure for table textadventure-database.answer
CREATE TABLE IF NOT EXISTS `answer` (
  `answer_id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  `npc_id` int(11) NOT NULL DEFAULT 0,
  `previous_answer_line_id` int(11) DEFAULT NULL,
  `next_answer_line_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`answer_id`),
  KEY `FK__line` (`previous_answer_line_id`),
  KEY `FK_answer_line_2` (`next_answer_line_id`),
  KEY `FK_answer_line_3` (`npc_id`),
  CONSTRAINT `FK_answer_line` FOREIGN KEY (`previous_answer_line_id`) REFERENCES `line` (`line_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_answer_line_2` FOREIGN KEY (`next_answer_line_id`) REFERENCES `line` (`line_id`) ON UPDATE CASCADE,
  CONSTRAINT `FK_answer_line_3` FOREIGN KEY (`npc_id`) REFERENCES `line` (`line_npc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-database.answer: ~9 rows (approximately)
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` (`answer_id`, `description`, `npc_id`, `previous_answer_line_id`, `next_answer_line_id`) VALUES
	(1, 'figure answer 1.1', 1, 1, 2),
	(2, 'figure answer 1.2', 1, 1, 5),
	(3, 'figure answer 2.1', 1, 2, 3),
	(4, 'figure answer 2.2', 1, 2, 4),
	(5, 'figure answer 3.1', 1, 3, 4),
	(6, 'figure answer 3.2', 1, 3, 5),
	(7, 'figure answer 4.1', 1, 4, 5),
	(8, 'figure answer 4.2', 1, 4, 6),
	(9, 'figure answer 5', 1, 5, 6);
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;

-- Dumping structure for table textadventure-database.articles
CREATE TABLE IF NOT EXISTS `articles` (
  `article` varchar(10) NOT NULL,
  PRIMARY KEY (`article`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-database.articles: ~3 rows (approximately)
/*!40000 ALTER TABLE `articles` DISABLE KEYS */;
INSERT INTO `articles` (`article`) VALUES
	('a'),
	('an'),
	('the');
/*!40000 ALTER TABLE `articles` ENABLE KEYS */;

-- Dumping structure for table textadventure-database.character
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

-- Dumping data for table textadventure-database.character: ~0 rows (approximately)
/*!40000 ALTER TABLE `character` DISABLE KEYS */;
INSERT INTO `character` (`character_id`, `name`, `hp`, `max_hp`, `attack`, `defence`, `money`, `alive`, `inventory`, `location_id`) VALUES
	(1, 'Traveller', 100, 100, 10, 10, 0, 1, 0, 1);
/*!40000 ALTER TABLE `character` ENABLE KEYS */;

-- Dumping structure for table textadventure-database.dictionary
CREATE TABLE IF NOT EXISTS `dictionary` (
  `dictionary` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-database.dictionary: ~0 rows (approximately)
/*!40000 ALTER TABLE `dictionary` DISABLE KEYS */;
INSERT INTO `dictionary` (`dictionary`) VALUES
	('sword'),
	('note');
/*!40000 ALTER TABLE `dictionary` ENABLE KEYS */;

-- Dumping structure for table textadventure-database.direction
CREATE TABLE IF NOT EXISTS `direction` (
  `direction_id` char(1) NOT NULL,
  `direction` varchar(10) NOT NULL,
  PRIMARY KEY (`direction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-database.direction: ~6 rows (approximately)
/*!40000 ALTER TABLE `direction` DISABLE KEYS */;
INSERT INTO `direction` (`direction_id`, `direction`) VALUES
	('d', 'down'),
	('e', 'east'),
	('n', 'north'),
	('s', 'south'),
	('u', 'up'),
	('w', 'west');
/*!40000 ALTER TABLE `direction` ENABLE KEYS */;

-- Dumping structure for table textadventure-database.item
CREATE TABLE IF NOT EXISTS `item` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `description` varchar(200) NOT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-database.item: ~1 rows (approximately)
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` (`item_id`, `name`, `description`, `attack`, `defence`, `money`, `addhp`, `pickable`, `weight`, `item_location_id`, `item_character_id`) VALUES
	(1, 'Sword', 'A shiny sword', 10, 0, 0, 0, 1, 10, 2, NULL),
	(2, 'note', 'This is the text within the note. This note tells many secrets and untold stories..', 0, 0, 0, 0, 1, 1, 1, NULL);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;

-- Dumping structure for table textadventure-database.item_word_table
CREATE TABLE IF NOT EXISTS `item_word_table` (
  `Column 1` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-database.item_word_table: ~0 rows (approximately)
/*!40000 ALTER TABLE `item_word_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `item_word_table` ENABLE KEYS */;

-- Dumping structure for table textadventure-database.line
CREATE TABLE IF NOT EXISTS `line` (
  `line_npc_id` int(11) NOT NULL,
  `line_id` int(11) NOT NULL AUTO_INCREMENT,
  `line` varchar(100) DEFAULT '0',
  PRIMARY KEY (`line_id`,`line_npc_id`),
  KEY `FK__npc` (`line_npc_id`),
  CONSTRAINT `FK__npc` FOREIGN KEY (`line_npc_id`) REFERENCES `npc` (`npc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-database.line: ~12 rows (approximately)
/*!40000 ALTER TABLE `line` DISABLE KEYS */;
INSERT INTO `line` (`line_npc_id`, `line_id`, `line`) VALUES
	(1, 1, 'figure line 1'),
	(2, 1, 'bob line 1'),
	(1, 2, 'figure line 2'),
	(2, 2, 'bob line 2'),
	(1, 3, 'figure line 3'),
	(2, 3, 'bob line 3'),
	(1, 4, 'figure line 4'),
	(2, 4, 'bob line 4'),
	(1, 5, 'figure line 5'),
	(2, 5, 'bob line 5'),
	(1, 6, '0'),
	(1, 12, '131');
/*!40000 ALTER TABLE `line` ENABLE KEYS */;

-- Dumping structure for table textadventure-database.location
CREATE TABLE IF NOT EXISTS `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `location_name` varchar(20) NOT NULL DEFAULT 'Room',
  `description` varchar(200) NOT NULL,
  `difficulty` int(3) NOT NULL DEFAULT 1,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-database.location: ~5 rows (approximately)
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` (`location_id`, `location_name`, `description`, `difficulty`) VALUES
	(1, 'Room 1', 'This room is the first room. This room is empty.', 1),
	(2, 'Room 2', 'The second room. Infront of you, you see a sword.', 2),
	(3, 'Room 3', 'Infront of you, you see a person', 3),
	(4, 'Room 4', 'This room is empty and dark. There are stairs leading down.', 3),
	(5, 'Room 5', 'This is a basement', 2);
/*!40000 ALTER TABLE `location` ENABLE KEYS */;

-- Dumping structure for table textadventure-database.locnpc
CREATE TABLE IF NOT EXISTS `locnpc` (
  `locnpc_npc_id` int(11) DEFAULT NULL,
  `locnpc_loc_id` int(11) DEFAULT NULL,
  KEY `FK_locnpc_npc` (`locnpc_npc_id`),
  KEY `FK_locnpc_location` (`locnpc_loc_id`),
  CONSTRAINT `FK_locnpc_location` FOREIGN KEY (`locnpc_loc_id`) REFERENCES `location` (`location_id`),
  CONSTRAINT `FK_locnpc_npc` FOREIGN KEY (`locnpc_npc_id`) REFERENCES `npc` (`npc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-database.locnpc: ~2 rows (approximately)
/*!40000 ALTER TABLE `locnpc` DISABLE KEYS */;
INSERT INTO `locnpc` (`locnpc_npc_id`, `locnpc_loc_id`) VALUES
	(1, 3),
	(2, 4),
	(2, 3);
/*!40000 ALTER TABLE `locnpc` ENABLE KEYS */;

-- Dumping structure for table textadventure-database.neighbours
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

-- Dumping data for table textadventure-database.neighbours: ~6 rows (approximately)
/*!40000 ALTER TABLE `neighbours` DISABLE KEYS */;
INSERT INTO `neighbours` (`from_location_id`, `to_location_id`, `neighbour_direction_id`) VALUES
	(1, 2, 'n'),
	(2, 3, 'e'),
	(2, 4, 'w'),
	(4, 5, 'd'),
	(3, 2, 'w'),
	(4, 2, 'e');
/*!40000 ALTER TABLE `neighbours` ENABLE KEYS */;

-- Dumping structure for table textadventure-database.npc
CREATE TABLE IF NOT EXISTS `npc` (
  `npc_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL DEFAULT 'NPC',
  `description` varchar(50) NOT NULL,
  `maxhp` int(5) NOT NULL,
  `met_npc` tinyint(4) DEFAULT 0,
  `npc_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`npc_id`),
  KEY `FK_npc_type` (`npc_type_id`),
  CONSTRAINT `FK_npc_type` FOREIGN KEY (`npc_type_id`) REFERENCES `type` (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-database.npc: ~2 rows (approximately)
/*!40000 ALTER TABLE `npc` DISABLE KEYS */;
INSERT INTO `npc` (`npc_id`, `name`, `description`, `maxhp`, `met_npc`, `npc_type_id`) VALUES
	(1, 'Figure', 'A dark figure', 100, 0, 1),
	(2, 'Bob', 'A bob is here', 1, 0, 2),
	(3, 'Enemy 1', 'enemy', 11, 0, 2),
	(4, 'Enemy 2', 'enemy', 1, 1, 2);
/*!40000 ALTER TABLE `npc` ENABLE KEYS */;

-- Dumping structure for table textadventure-database.prepositions
CREATE TABLE IF NOT EXISTS `prepositions` (
  `prepositions` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-database.prepositions: ~6 rows (approximately)
/*!40000 ALTER TABLE `prepositions` DISABLE KEYS */;
INSERT INTO `prepositions` (`prepositions`) VALUES
	('in'),
	('on'),
	('under'),
	('over'),
	('at'),
	('with');
/*!40000 ALTER TABLE `prepositions` ENABLE KEYS */;

-- Dumping structure for table textadventure-database.type
CREATE TABLE IF NOT EXISTS `type` (
  `type_id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  `defence` int(5) DEFAULT NULL,
  `attack` int(5) DEFAULT NULL,
  `friendly` tinyint(4) DEFAULT NULL,
  `hp` int(5) DEFAULT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-database.type: ~2 rows (approximately)
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
INSERT INTO `type` (`type_id`, `description`, `defence`, `attack`, `friendly`, `hp`) VALUES
	(1, 'Dark figure', 10, 10, 1, 100),
	(2, 'Bob is a man', NULL, NULL, 0, 0);
/*!40000 ALTER TABLE `type` ENABLE KEYS */;

-- Dumping structure for table textadventure-database.verbs
CREATE TABLE IF NOT EXISTS `verbs` (
  `id` int(11) DEFAULT NULL,
  `verbs` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventure-database.verbs: ~14 rows (approximately)
/*!40000 ALTER TABLE `verbs` DISABLE KEYS */;
INSERT INTO `verbs` (`id`, `verbs`) VALUES
	(0, 'get'),
	(0, 'take'),
	(0, 'pick up'),
	(1, 'look at'),
	(2, 'examine'),
	(2, 'inspect'),
	(3, 'kill'),
	(3, 'attack'),
	(3, 'hit'),
	(2, 'read'),
	(4, 'talk'),
	(4, 'talk to'),
	(4, 'speak'),
	(4, 'speak to'),
	(5, 'go'),
	(5, 'move');
/*!40000 ALTER TABLE `verbs` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
