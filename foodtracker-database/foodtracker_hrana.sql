-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: foodtracker
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `hrana`
--

DROP TABLE IF EXISTS `hrana`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hrana` (
  `id_hrane` int NOT NULL AUTO_INCREMENT,
  `naziv_hrane` varchar(50) NOT NULL,
  `kolicina` float NOT NULL,
  `kalorije` float NOT NULL,
  `proteini` float NOT NULL,
  `ugljeni_hidrati` float NOT NULL,
  `masti` float NOT NULL,
  PRIMARY KEY (`id_hrane`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hrana`
--

LOCK TABLES `hrana` WRITE;
/*!40000 ALTER TABLE `hrana` DISABLE KEYS */;
INSERT INTO `hrana` VALUES (83,'eggs',150,214.5,18.9,1.08,14.27),(84,'bread',50,137,5.35,23.75,2.27),(85,'catsup',20,20.2,0.21,5.48,0.02),(86,'mayo',20,136,0.19,0.11,14.96),(87,'chicken',200,206.4,17.86,0,14.46),(88,'rice',150,547.5,10.69,119.93,0.99),(89,'mesclun',100,16,1.25,3.22,0.07),(90,'pancake mix',200,436,15.6,57.8,15.4),(91,'croissants',100,406,8.2,45.8,21),(92,'margarita mix',200,176,0,42.48,0),(93,'meat',250,285,53.08,0,6.47),(94,'orange marmelade',120,295.2,0.36,79.56,0),(95,'pineapples',50,25,0.27,6.55,0.06),(96,'canned tuna',150,135,28.5,0.12,1.41),(97,'bread roll dough',30,76.43,1.76,14.11,0.88),(98,'fresh mushrooms',100,22,3.09,3.26,0.34),(99,'capsicum',80,20.8,0.79,4.82,0.24),(100,'apple pie spice',75,256.5,4.32,51.96,9.45),(101,'waffle syrup',200,592,0,148.2,3.2),(102,'yolk',150,483,23.85,5.39,39.75),(103,'ham steaks',100,122,19.56,0,4.25),(104,'mussel',200,87.72,12.14,3.76,2.28),(105,'shell pasta',100,371,13.04,74.67,1.51),(106,'corn tortilla rounds',170,802.4,12.07,115.26,35.19);
/*!40000 ALTER TABLE `hrana` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-18 16:30:42
