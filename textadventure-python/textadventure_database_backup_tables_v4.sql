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

-- Dumping structure for table textadventuredatabase.answer
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

-- Dumping data for table textadventuredatabase.answer: ~9 rows (approximately)
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

-- Dumping structure for table textadventuredatabase.articles
CREATE TABLE IF NOT EXISTS `articles` (
  `article` varchar(10) NOT NULL,
  PRIMARY KEY (`article`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventuredatabase.articles: ~2 rows (approximately)
/*!40000 ALTER TABLE `articles` DISABLE KEYS */;
INSERT INTO `articles` (`article`) VALUES
	('a'),
	('an'),
	('the');
/*!40000 ALTER TABLE `articles` ENABLE KEYS */;

-- Dumping structure for table textadventuredatabase.character_
CREATE TABLE IF NOT EXISTS `character_` (
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

-- Dumping data for table textadventuredatabase.character_: ~0 rows (approximately)
/*!40000 ALTER TABLE `character_` DISABLE KEYS */;
INSERT INTO `character_` (`character_id`, `name`, `hp`, `max_hp`, `attack`, `defence`, `money`, `alive`, `inventory`, `location_id`) VALUES
	(1, 'Traveller', 100, 100, 10, 10, 0, 1, 0, 1);
/*!40000 ALTER TABLE `character_` ENABLE KEYS */;

-- Dumping structure for table textadventuredatabase.dictionary
CREATE TABLE IF NOT EXISTS `dictionary` (
  `id` int(11) DEFAULT 255,
  `dictionary` varchar(20) NOT NULL DEFAULT '255',
  PRIMARY KEY (`dictionary`),
  KEY `FK_dictionary_dictionary_group` (`id`),
  CONSTRAINT `FK_dictionary_dictionary_group` FOREIGN KEY (`id`) REFERENCES `dictionary_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventuredatabase.dictionary: ~17 rows (approximately)
/*!40000 ALTER TABLE `dictionary` DISABLE KEYS */;
INSERT INTO `dictionary` (`id`, `dictionary`) VALUES
	(1, 'note'),
	(1, 'paper'),
	(2, 'figure'),
	(3, 'blade'),
	(3, 'sword'),
	(4, 'd'),
	(4, 'down'),
	(4, 'e'),
	(4, 'east'),
	(4, 'n'),
	(4, 'north'),
	(4, 's'),
	(4, 'south'),
	(4, 'u'),
	(4, 'up'),
	(4, 'w'),
	(4, 'west');
/*!40000 ALTER TABLE `dictionary` ENABLE KEYS */;

-- Dumping structure for table textadventuredatabase.dictionary_group
CREATE TABLE IF NOT EXISTS `dictionary_group` (
  `id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventuredatabase.dictionary_group: ~5 rows (approximately)
/*!40000 ALTER TABLE `dictionary_group` DISABLE KEYS */;
INSERT INTO `dictionary_group` (`id`, `name`) VALUES
	(1, 'note'),
	(2, 'figure'),
	(3, 'sword'),
	(4, 'direction'),
	(255, '255');
/*!40000 ALTER TABLE `dictionary_group` ENABLE KEYS */;

-- Dumping structure for table textadventuredatabase.direction
CREATE TABLE IF NOT EXISTS `direction` (
  `direction_id` char(1) NOT NULL,
  `direction` varchar(10) NOT NULL,
  PRIMARY KEY (`direction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventuredatabase.direction: ~6 rows (approximately)
/*!40000 ALTER TABLE `direction` DISABLE KEYS */;
INSERT INTO `direction` (`direction_id`, `direction`) VALUES
	('d', 'down'),
	('e', 'east'),
	('n', 'north'),
	('s', 'south'),
	('u', 'up'),
	('w', 'west');
/*!40000 ALTER TABLE `direction` ENABLE KEYS */;

-- Dumping structure for table textadventuredatabase.item
CREATE TABLE IF NOT EXISTS `item` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `description` varchar(200) NOT NULL,
  `attack` int(5) DEFAULT 0,
  `defence` int(5) DEFAULT 0,
  `money` int(5) DEFAULT 0,
  `addhp` int(5) DEFAULT 0,
  `pickable` tinyint(4) DEFAULT NULL,
  `item_location_id` int(11) NOT NULL,
  `item_character_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  KEY `FK_item_location` (`item_location_id`),
  KEY `FK_item_character` (`item_character_id`),
  CONSTRAINT `FK_item_character` FOREIGN KEY (`item_character_id`) REFERENCES `character_` (`character_id`),
  CONSTRAINT `FK_item_location` FOREIGN KEY (`item_location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventuredatabase.item: ~2 rows (approximately)
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` (`item_id`, `name`, `description`, `attack`, `defence`, `money`, `addhp`, `pickable`, `item_location_id`, `item_character_id`) VALUES
	(1, 'Sword', 'A shiny sword', 10, 0, 0, 0, 1, 2, NULL),
	(2, 'note', 'This is the text within the note. This note tells many secrets and untold stories..', 0, 0, 0, 0, 1, 1, NULL);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;

-- Dumping structure for table textadventuredatabase.item_word_table
CREATE TABLE IF NOT EXISTS `item_word_table` (
  `Column 1` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventuredatabase.item_word_table: ~0 rows (approximately)
/*!40000 ALTER TABLE `item_word_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `item_word_table` ENABLE KEYS */;

-- Dumping structure for table textadventuredatabase.jump_table
CREATE TABLE IF NOT EXISTS `jump_table` (
  `verb` int(11) DEFAULT 255,
  `direct_object` int(11) DEFAULT 255,
  `preposition` int(11) DEFAULT 255,
  `indirect_object` int(11) DEFAULT 255,
  `subroutine` varchar(70) DEFAULT NULL,
  KEY `FK_jump_table_verb_group` (`verb`),
  KEY `FK_jump_table_dictionary_group` (`direct_object`),
  KEY `FK_jump_table_prepositions` (`preposition`),
  KEY `FK_jump_table_dictionary_group_2` (`indirect_object`),
  CONSTRAINT `FK_jump_table_dictionary_group` FOREIGN KEY (`direct_object`) REFERENCES `dictionary_group` (`id`),
  CONSTRAINT `FK_jump_table_dictionary_group_2` FOREIGN KEY (`indirect_object`) REFERENCES `dictionary_group` (`id`),
  CONSTRAINT `FK_jump_table_prepositions` FOREIGN KEY (`preposition`) REFERENCES `prepositions` (`id`),
  CONSTRAINT `FK_jump_table_verb_group` FOREIGN KEY (`verb`) REFERENCES `verb_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventuredatabase.jump_table: ~9 rows (approximately)
/*!40000 ALTER TABLE `jump_table` DISABLE KEYS */;
INSERT INTO `jump_table` (`verb`, `direct_object`, `preposition`, `indirect_object`, `subroutine`) VALUES
	(2, 2, 5, 255, 'talk_answer.answer(conn, location_id, direct_str, 0)'),
	(2, 2, 255, 255, 'talk_answer.answer(conn, location_id, direct_str, 0)'),
	(2, 255, 255, 255, 'talk_answer.talk(conn, location_id)'),
	(1, 255, 255, 255, 'loc_npc_look.look_around(conn, location_id)'),
	(2, 255, 5, 255, 'talk_answer.talk(conn, location_id)'),
	(3, 4, 5, 255, 'loc_npc_look.move(conn, location_id, direct_str)'),
	(3, 4, 255, 255, 'loc_npc_look.move(conn, location_id, direct_str)'),
	(255, 4, 255, 255, 'loc_npc_look.move(conn, location_id, direct_str)'),
	(3, 255, 255, 255, 'loc_npc_look.move(conn, location_id, direct_str)');
/*!40000 ALTER TABLE `jump_table` ENABLE KEYS */;

-- Dumping structure for table textadventuredatabase.line
CREATE TABLE IF NOT EXISTS `line` (
  `line_npc_id` int(11) NOT NULL,
  `line_id` int(11) NOT NULL AUTO_INCREMENT,
  `line` varchar(100) DEFAULT '0',
  PRIMARY KEY (`line_id`,`line_npc_id`),
  KEY `FK__npc` (`line_npc_id`),
  CONSTRAINT `FK__npc` FOREIGN KEY (`line_npc_id`) REFERENCES `npc` (`npc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventuredatabase.line: ~12 rows (approximately)
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

-- Dumping structure for table textadventuredatabase.location
CREATE TABLE IF NOT EXISTS `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `location_name` varchar(20) NOT NULL DEFAULT 'Room',
  `description` varchar(200) NOT NULL,
  `difficulty` int(3) NOT NULL DEFAULT 1,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventuredatabase.location: ~5 rows (approximately)
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` (`location_id`, `location_name`, `description`, `difficulty`) VALUES
	(1, 'Room 1', 'This room is the first room. This room is empty.', 1),
	(2, 'Room 2', 'The second room. Infront of you, you see a sword.', 2),
	(3, 'Room 3', 'Infront of you, you see a person', 3),
	(4, 'Room 4', 'This room is empty and dark. There are stairs leading down.', 3),
	(5, 'Room 5', 'This is a basement', 2);
/*!40000 ALTER TABLE `location` ENABLE KEYS */;

-- Dumping structure for table textadventuredatabase.neighbours
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

-- Dumping data for table textadventuredatabase.neighbours: ~6 rows (approximately)
/*!40000 ALTER TABLE `neighbours` DISABLE KEYS */;
INSERT INTO `neighbours` (`from_location_id`, `to_location_id`, `neighbour_direction_id`) VALUES
	(1, 2, 'n'),
	(2, 3, 'e'),
	(2, 4, 'w'),
	(4, 5, 'd'),
	(3, 2, 'w'),
	(4, 2, 'e');
/*!40000 ALTER TABLE `neighbours` ENABLE KEYS */;

-- Dumping structure for table textadventuredatabase.npc
CREATE TABLE IF NOT EXISTS `npc` (
  `npc_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL DEFAULT 'NPC',
  `description` varchar(50) NOT NULL,
  `maxhp` int(5) NOT NULL,
  `met_npc` tinyint(4) DEFAULT 0,
  `npc_location_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`npc_id`),
  KEY `FK_npc_location` (`npc_location_id`),
  CONSTRAINT `FK_npc_location` FOREIGN KEY (`npc_location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Dumping data for table textadventuredatabase.npc: ~4 rows (approximately)
/*!40000 ALTER TABLE `npc` DISABLE KEYS */;
INSERT INTO `npc` (`npc_id`, `name`, `description`, `maxhp`, `met_npc`, `npc_location_id`) VALUES
	(1, 'Figure', 'A dark figure', 100, 0, 1),
	(2, 'Bob', 'A bob is here', 1, 0, 3),
	(3, 'Enemy 1', 'enemy 1', 11, 0, 1),
	(4, 'Enemy 2', 'enemy 2', 1, 1, 4);
/*!40000 ALTER TABLE `npc` ENABLE KEYS */;

-- Dumping structure for table textadventuredatabase.prepositions
CREATE TABLE IF NOT EXISTS `prepositions` (
  `id` int(11) NOT NULL,
  `prepositions` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventuredatabase.prepositions: ~8 rows (approximately)
/*!40000 ALTER TABLE `prepositions` DISABLE KEYS */;
INSERT INTO `prepositions` (`id`, `prepositions`) VALUES
	(1, 'at'),
	(2, 'in'),
	(3, 'on'),
	(4, 'over'),
	(5, 'to'),
	(6, 'under'),
	(7, 'with'),
	(255, '255');
/*!40000 ALTER TABLE `prepositions` ENABLE KEYS */;

-- Dumping structure for table textadventuredatabase.subroutine
CREATE TABLE IF NOT EXISTS `subroutine` (
  `id` int(11) NOT NULL,
  `subroutine` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventuredatabase.subroutine: ~2 rows (approximately)
/*!40000 ALTER TABLE `subroutine` DISABLE KEYS */;
INSERT INTO `subroutine` (`id`, `subroutine`) VALUES
	(1, 'talk'),
	(2, 'location');
/*!40000 ALTER TABLE `subroutine` ENABLE KEYS */;

-- Dumping structure for table textadventuredatabase.verbs
CREATE TABLE IF NOT EXISTS `verbs` (
  `id` int(11) DEFAULT NULL,
  `verbs` varchar(20) NOT NULL,
  PRIMARY KEY (`verbs`),
  KEY `FK_verbs_verb_group` (`id`),
  CONSTRAINT `FK_verbs_verb_group` FOREIGN KEY (`id`) REFERENCES `verb_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventuredatabase.verbs: ~8 rows (approximately)
/*!40000 ALTER TABLE `verbs` DISABLE KEYS */;
INSERT INTO `verbs` (`id`, `verbs`) VALUES
	(0, 'get'),
	(0, 'pick'),
	(0, 'take'),
	(1, 'look'),
	(2, 'speak'),
	(2, 'talk'),
	(3, 'go'),
	(3, 'move');
/*!40000 ALTER TABLE `verbs` ENABLE KEYS */;

-- Dumping structure for table textadventuredatabase.verb_group
CREATE TABLE IF NOT EXISTS `verb_group` (
  `id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table textadventuredatabase.verb_group: ~5 rows (approximately)
/*!40000 ALTER TABLE `verb_group` DISABLE KEYS */;
INSERT INTO `verb_group` (`id`, `name`) VALUES
	(0, 'get'),
	(1, 'look'),
	(2, 'talk'),
	(3, 'move'),
	(255, '255');
/*!40000 ALTER TABLE `verb_group` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
