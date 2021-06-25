CREATE DATABASE  IF NOT EXISTS `esporte` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `esporte`;
-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: esporte
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `times_brasileiros`
--

DROP TABLE IF EXISTS `times_brasileiros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `times_brasileiros` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `sigla` varchar(8) DEFAULT NULL,
  `fundacao` date NOT NULL,
  `localizacao` enum('Acre','Alagoas','Amapá','Amazonas','Bahia','Ceará','Distrito Federal','Espírito Santo','Goiás','Maranhão','Mato Grosso','Mato Grosso do Sul','Minas Gerais','Pará','Paraíba','Paraná','Pernambuco','Piauí','Rio de Janeiro','Rio Grande do Norte','Rio Grande do Sul','Rondônia','Roraima','Santa Catarina','São Paulo','Sergipe','Tocantins') DEFAULT NULL,
  `treinador` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `times_brasileiros`
--

LOCK TABLES `times_brasileiros` WRITE;
/*!40000 ALTER TABLE `times_brasileiros` DISABLE KEYS */;
INSERT INTO `times_brasileiros` VALUES (1,'São Paulo Futebol Clube','SPFC','1930-01-25','São Paulo','Hernán Crespo'),(2,'Sport Club Corinthians Paulista','SCCP','1910-09-01','São Paulo','Sylvinho'),(3,'Ferroviário Atlético Clube','FAC','1933-05-09','Ceará','Francisco Diá'),(4,'Goiânia Esporte Clube','GEC','1938-07-05','Goiás','Arthur Neto'),(5,'Guarani Futebol Clube','GFC','1911-04-02','São Paulo','Daniel Paulista'),(6,'Cruzeiro Esporte Clube','CEC','1921-01-02','Minas Gerais','Mozart Santos'),(7,'Fortaleza Esporte Clube','FEC','1918-10-18','Ceará','Juan Pablo Vojvoda'),(8,'Clube Atlético Mineiro','CAM','1918-03-25','Minas Gerais','Cuca'),(9,'Paysandu Sport Club','PSC','1914-02-02','Pará','Vinícius Eutrópio'),(10,'Sociedade Esportiva Palmeiras','SEP','1914-08-26','São Paulo','Abel Ferreira');
/*!40000 ALTER TABLE `times_brasileiros` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-25  9:35:41
