
USE cadastro;

INSERT INTO cursos VALUES
('1', 'HTML4', 'Curso de HTML5', '40', '37', '2014'),
('2', 'Algoritmos', 'Lógica de Programação', '20', '15', '2014'),
('3', 'Photoshop', 'Dicas de Photoshop CC', '10', '8', '2014'),
('4', 'PGP', 'Curso de PHP para iniciantes', '40', '20', '2010'),
('5', 'Jarva', 'Introdução à Linguagem Java', '10', '29', '2000'),
('6', 'MySQL', 'Banco de Dados MySQL', '30', '15', '2016'),
('7', 'Word', 'Curso Completo de Word', '40', '30', '2016'),
('8', 'Sapateado', 'Danças Rítmicas', '40', '30', '2018'),
('9', 'Cozinha Árabe', 'Aprenda a fazer Kibe', '40', '30', '2018'),
('10', 'YouTuber', 'Gerar polêmica e ganhar inscritos', '5', '2', '2018');

-- Modificando o nome da linha 1 da tabela cursos

UPDATE cursos
SET nome = 'HTML5'
WHERE id_curso = '1';

-- Modificando o nome e ano da linha 4 da tabela cursos

UPDATE cursos
SET nome = 'PHP', ano = '2015'
WHERE id_curso = '4';

-- Modificando o nome, carga e ano da linha 5 da tabela cursos

UPDATE cursos
SET nome = 'Java', carga = '40', ano = '2015'
WHERE id_curso = '5'
LIMIT 1;  -- Limitando para 1 o número de linhas afetadas por esse comando

-- Modificando várias linhas ao mesmo tempo

UPDATE cursos
SET ano = '2050', carga = '800'
WHERE ano = '2018';

UPDATE cursos
SET ano = '2018', carga = '0'
WHERE ano = '2050'
LIMIT 1;  -- A modificação do comando só vai se limitar a uma linha

-- Apagando linhas de uma tabela

DELETE FROM cursos
WHERE id_curso = '8';

DELETE FROM cursos
WHERE ano = '2050'
LIMIT 2;

TRUNCATE TABLE cursos;  -- Apagando TODAS as linhas de uma tabela

SELECT * FROM cursos;
