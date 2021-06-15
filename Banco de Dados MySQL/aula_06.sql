
USE cadastro;

DESCRIBE gafanhotos;  -- Descrevendo a tabela
DESCRIBE cursos;

-- Alterando a tabela "pessoas" para adicionar uma nova coluna (ou campo) "profissao"

ALTER TABLE pessoas
ADD COLUMN profissao varchar(10);

-- Apagando uma coluna de "pessoas"

ALTER TABLE pessoas
DROP COLUMN profissao;

-- Escolhendo uma nova posição para uma coluna ser adicionada

ALTER TABLE pessoas
ADD COLUMN profissao varchar(10) AFTER nome;  -- "profissao" será adicionada depois da coluna "nome"

-- Adicionando uma coluna na primeira posição da tabela

ALTER TABLE	pessoas
ADD codigo int FIRST;  -- O comando COLUMN é opcional

-- Modificando uma coluna com Modify (seus tipos primitivos e constraints)

UPDATE pessoas
SET profissao = '';
ALTER TABLE pessoas
MODIFY COLUMN profissao varchar(20) NOT NULL DEFAULT '';  -- O default é vazio para nao gerar conflitos no BD

-- Renomeando uma coluna (ao renomear é preciso informar novamente todas suas constraints e tipos)

ALTER TABLE pessoas
CHANGE COLUMN profissao prof varchar(20);  -- "profissao" será renomeado para "prof"

-- Renomenado uma tabela

ALTER TABLE pessoas
RENAME TO gafanhotos;

-- Criação de uma tabela com o comando IF NOT EXIST (só cria algo se ele não existir; tem o IF EXIST também)

CREATE TABLE IF NOT EXISTS cursos (
	nome varchar(30) NOT NULL UNIQUE,  -- O comando "UNIQUE" (único) não permite dois registros com o mesmo nome 
	descricao text,
	carga int UNSIGNED,  -- Só aceita número maior que 0
	total_aulas int UNSIGNED,
	ano year DEFAULT '2021'
) DEFAULT CHARSET = utf8mb4; 

-- Adicionando uma chave primária numa tabela já criada (com a nova coluna id_curso)

ALTER TABLE cursos
ADD COLUMN id_curso int FIRST;

ALTER TABLE cursos
ADD PRIMARY KEY (id_curso);

-- Criando tabela e inserindo registros para apaga-la com o DROP

CREATE TABLE IF NOT EXISTS teste (
	id int,
    nome varchar(10),
    idade int
);

INSERT INTO teste VALUES
('1', 'David', '22'),
('2', 'Robson', '23'),
('3', 'Maria', '77');

DROP TABLE IF EXISTS teste;

SELECT * FROM gafanhotos;
SELECT * FROM cursos;
SELECT * FROM teste;
   