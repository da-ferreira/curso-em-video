
USE cadastro;

INSERT INTO cursos VALUES
('1', 'HTML5', 'Curso de HTML5', '40', '37', '2014'),
('2', 'Algoritmos', 'Lógica de Programação', '20', '15', '2014'),
('3', 'Photoshop', 'Dicas de Photoshop CC', '10', '8', '2014'),
('4', 'PHP', 'Curso de PHP para iniciantes', '40', '20', '2015'),
('5', 'Java', 'Introdução à Linguagem Java', '40', '29', '2015'),
('6', 'MySQL', 'Banco de Dados MySQL', '30', '15', '2016'),
('7', 'Word', 'Curso Completo de Word', '40', '30', '2016');

SELECT * FROM cursos;
SELECT * FROM gafanhotos;

DESCRIBE cursos;
DESCRIBE gafanhotos;

SHOW TABLES;  -- Mostra todas as tabelas do BD usado

-- Apagando o Banco de Dados "cadastro" para usar seu Dump depois

DROP DATABASE IF EXISTS cadastro;
