
CREATE DATABASE IF NOT EXISTS esporte
DEFAULT CHARACTER SET = utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

USE esporte;

CREATE TABLE IF NOT EXISTS times_brasileiros (
	id          int         NOT NULL AUTO_INCREMENT,
    nome        varchar(50) NOT NULL,
    sigla       varchar(8),
    fundacao    date        NOT NULL,
    localizacao varchar(20),
    treinador   varchar(50),
    PRIMARY KEY (id)
) DEFAULT CHARSET = utf8mb4;

ALTER TABLE times_brasileiros
MODIFY COLUMN localizacao enum('Acre', 'Alagoas',  'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão',
                               'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro',
							   'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins');

INSERT INTO times_brasileiros VALUES
(DEFAULT, 'São Paulo Futebol Clube', 'SPFC', '1930-01-25', 'São Paulo', 'Hernán Crespo'),
(DEFAULT, 'Sport Club Corinthians Paulista', 'SCCP', '1910-09-01', 'São Paulo', 'Sylvinho'),
(DEFAULT, 'Ferroviário Atlético Clube', 'FAC', '1933-05-09', 'Ceará', 'Francisco Diá'),
(DEFAULT, 'Goiânia Esporte Clube', 'GEC', '1938-07-05', 'Goiás', 'Arthur Neto'),
(DEFAULT, 'Guarani Futebol Clube', 'GFC', '1911-04-02', 'São Paulo', 'Daniel Paulista'),
(DEFAULT, 'Cruzeiro Esporte Clube', 'CEC', '1921-01-02', 'Minas Gerais', '	Mozart Santos'),
(DEFAULT, 'Fortaleza Esporte Clube', 'FEC', '1918-10-18', 'Ceará', 'Juan Pablo Vojvoda'),
(DEFAULT, 'Clube Atlético Mineiro', 'CAM', '1918-03-25', 'Minas Gerais', 'Cuca'),
(DEFAULT, 'Paysandu Sport Club', 'PSC', '1914-02-02', 'Pará', '	Vinícius Eutrópio'),
(DEFAULT, 'Sociedade Esportiva Palmeiras', 'SEP', '1914-08-26', 'São Paulo', 'Abel Ferreira');

UPDATE times_brasileiros
SET treinador = 'Mozart Santos'
WHERE id = '6';

UPDATE times_brasileiros
SET treinador = 'Vinícius Eutrópio'
WHERE nome = 'Paysandu Sport Club';

SELECT * FROM times_brasileiros;
  