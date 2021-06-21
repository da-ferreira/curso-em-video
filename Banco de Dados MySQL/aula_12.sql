
USE cadastro;

SELECT * FROM cursos;
SELECT * FROM gafanhotos;

-- Usando o operador LIKE (parecido/semelhante), para pegar todos os registros que tem seu nome começando com a letra P:
SELECT * FROM cursos
WHERE nome LIKE 'P%'  -- % -> Wild Card (carta coringa: caracter coringa que substitui nenhum ou vários caracteres). O LIKE não é case-sensitive
ORDER BY idcurso;

-- Alternando a posição do caracter coringa:
SELECT * FROM cursos
WHERE nome LIKE '%A';  -- Nomes que terminam com a letra 'Aa'

SELECT * FROM cursos
WHERE nome LIKE '%A%'; -- Nomes que contém a letra 'Aa'

SELECT * FROM cursos
WHERE nome NOT LIKE '%A%';  -- Nome que NÃO contém a letra 'Aa'

SELECT * FROM cursos
WHERE nome LIKE 'PH%P%';

SELECT * FROM cursos
WHERE nome LIKE 'P__';  -- Wild Card '_' -> Obriga que tenha algum caractere

SELECT * FROM gafanhotos
WHERE nome LIKE '%_Silva%';  -- Pessoas com Silva no nome

-- Distinguindo com o parametro DISTINCT
SELECT DISTINCT nacionalidade FROM gafanhotos  -- Pega todas as nacionalidades sem repeti-las
ORDER BY nacionalidade;

SELECT DISTINCT carga FROM cursos  -- Cargas horárias dos cursos sem repetição
ORDER BY carga DESC;

-- Funções de Agregação
SELECT COUNT(*) FROM cursos;  -- Conta quantos registros a tabela tem
 
SELECT COUNT(*) FROM cursos
WHERE carga > 40;  -- Quantos cursos tem carga acima de 40

SELECT MAX(totaulas) FROM cursos;  -- Retorna o máximo dentro de um campo
SELECT MIN(totaulas) FROM cursos;  -- Retorna o mínimo dentro de um campo

SELECT MAX(carga) FROM cursos  -- A maior carga dos cursos que tem ano de 2017
WHERE ano = '2017';

SELECT nome, descricao, MIN(carga) FROM cursos  -- A menor carga, nome e descricao
WHERE ano = '2017';

SELECT SUM(totaulas) FROM cursos;  -- Somatório de totais de aulas dos cursos
SELECT SUM(carga) FROM cursos;

SELECT SUM(carga) FROM cursos  -- Somatorio de todas as cargas dos cursos de 2017
WHERE ano = '2017';

SELECT AVG(carga) FROM cursos;  -- AVG (average -> média em ingles)
SELECT AVG(totaulas) FROM cursos;

SELECT AVG(totaulas) FROM cursos
WHERE ano = 2016;
 