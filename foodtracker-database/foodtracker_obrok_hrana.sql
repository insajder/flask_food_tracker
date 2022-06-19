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
-- Table structure for table `obrok_hrana`
--

DROP TABLE IF EXISTS `obrok_hrana`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `obrok_hrana` (
  `id_obrok_hrana` int NOT NULL AUTO_INCREMENT,
  `id_korisnika` int NOT NULL,
  `obrok` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8_general_ci NOT NULL,
  `id_hrane` int NOT NULL,
  `datum` date NOT NULL,
  PRIMARY KEY (`id_obrok_hrana`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `obrok_hrana`
--

LOCK TABLES `obrok_hrana` WRITE;
/*!40000 ALTER TABLE `obrok_hrana` DISABLE KEYS */;
INSERT INTO `obrok_hrana` VALUES (68,11,'dorucak',83,'2022-06-18'),(69,11,'dorucak',84,'2022-06-18'),(70,11,'dorucak',85,'2022-06-18'),(71,11,'dorucak',86,'2022-06-18'),(72,11,'rucak',87,'2022-06-18'),(73,11,'rucak',88,'2022-06-18'),(74,11,'vecera',89,'2022-06-18'),(75,11,'uzina',90,'2022-06-18'),(76,11,'dorucak',91,'2022-06-17'),(77,11,'vecera',92,'2022-06-17'),(78,11,'rucak',93,'2022-06-17'),(79,11,'rucak',94,'2022-06-17'),(80,11,'uzina',95,'2022-06-17'),(81,1,'dorucak',96,'2022-06-18'),(82,1,'dorucak',97,'2022-06-18'),(83,1,'rucak',98,'2022-06-18'),(84,1,'rucak',99,'2022-06-18'),(85,1,'uzina',100,'2022-06-18'),(86,1,'vecera',101,'2022-06-18'),(87,1,'dorucak',102,'2022-06-17'),(88,1,'dorucak',103,'2022-06-17'),(89,1,'rucak',104,'2022-06-17'),(90,1,'rucak',105,'2022-06-17'),(91,1,'uzina',106,'2022-06-17');
/*!40000 ALTER TABLE `obrok_hrana` ENABLE KEYS */;
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
