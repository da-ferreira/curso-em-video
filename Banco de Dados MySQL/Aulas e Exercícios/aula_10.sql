
CREATE DATABASE IF NOT EXISTS exemplo
DEFAULT CHARACTER SET = utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

USE exemplo;

CREATE TABLE IF NOT EXISTS amigos (
	id int NOT NULL AUTO_INCREMENT,
    nome varchar(30) NOT NULL UNIQUE,
    telefone varchar(11),
    PRIMARY KEY (id)
) DEFAULT CHARSET = utf8mb4;

ALTER TABLE amigos
MODIFY COLUMN telefone varchar(15);

ALTER TABLE amigos
ADD idade int NOT NULL AFTER nome;

ALTER TABLE amigos
DROP COLUMN idade;  -- Não se cadastra idade, cadastra-se data de nascimento

ALTER TABLE amigos
ADD sexo ENUM('M', 'F') NOT NULL AFTER nome;

INSERT INTO amigos VALUES
(DEFAULT, 'Maria', 'F', '2222-3333'),
(DEFAULT, 'José', 'M', '2222-3333');

INSERT INTO amigos VALUES
(DEFAULT, 'João', 'M', '3333-4444'),
(DEFAULT, 'Ana', 'F', '1111-2222');

UPDATE amigos
SET telefone = '5555-6666'
WHERE id = '1';

DELETE FROM exemplo.amigos  -- O "exemplo.amigos" é opcional. Pode ser feito sem
WHERE amigos.id = '6';

TRUNCATE TABLE amigos;  -- Apagando os dados da tabela (não a estrutura, DML)
DROP TABLE amigos; -- Apagando a estrutura da tabela (DDL)
DROP DATABASE exemplo;  -- Apagando o banco de dados (DDL)
