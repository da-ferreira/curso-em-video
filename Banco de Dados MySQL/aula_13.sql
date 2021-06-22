
USE cadastro;

SELECT * FROM gafanhotos;
SELECT * FROM cursos;

-- Agrupando e Agregando
SELECT carga, COUNT(nome) FROM cursos  -- Quantos registros de cada carga tem na tabela
GROUP BY carga
ORDER BY COUNT(nome) DESC;

SELECT totaulas, COUNT(*) FROM cursos
GROUP BY totaulas
ORDER BY COUNT(*) DESC;

SELECT carga, COUNT(*) FROM cursos
WHERE totaulas = '30'
GROUP BY carga;

-- Agrupando especificando quem deve ser mostrando com o parametro HAVING
SELECT ano, COUNT(*) FROM cursos
GROUP BY ano
HAVING COUNT(ano) > 3  -- Somente os anos que tem mais de 3 aparições nos cursos será selecionado. No do having só pode usar o campo de foi agrupado (GROUP BY)
ORDER BY ano DESC;

-- Seleciono ano de cursos onde o total de aulas é maior que 30, agrupado pelos anos, selecionando somente os anos acima de 2013 
SELECT ano, COUNT(*) FROM cursos
WHERE totaulas > '30'
GROUP BY ano
HAVING ano > 2013
ORDER BY COUNT(*) DESC;

-- SELECT dentro de SELECT
SELECT carga, COUNT(*) FROM cursos
WHERE ano > 2015
GROUP BY carga
HAVING carga > (SELECT AVG(carga) FROM cursos)
ORDER BY COUNT(*) DESC;
 