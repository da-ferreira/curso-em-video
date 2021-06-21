
USE cadastro;

SELECT * FROM cursos;
SELECT * FROM gafanhotos;

-- Seleciona todos os registros de "curso" por ordem de "nome"
SELECT * FROM cursos
ORDER BY nome;

-- Seleciona todos os registros de "curso" por ordem DECRESCENTE de "nome" 
SELECT * FROM cursos
ORDER BY nome DESC;  -- Para ver em ordem CRESCENTE (ascendente) é só usar ASC no lugar de DESC

-- Filtrando colunas
SELECT ano, nome, carga FROM cursos  -- A ordem de filtragem pode ser aleatória
ORDER BY ano;

-- Filtrando e ordenando por mais de uma coluna
SELECT ano, nome, carga FROM cursos
ORDER BY ano, nome;

-- Filtrando as linhas com a cláusula WHERE e usando os OPERADORES relacionais BÁSICOS
SELECT * FROM cursos
WHERE ano = '2017'  -- Todos os cursos que tem ano == 2017
ORDER BY nome;
	
SELECT nome, descricao, carga FROM cursos
WHERE ano = '2017'
ORDER BY carga DESC;

SELECT ano, nome, descricao FROM cursos
WHERE ano <= 2015  -- Seleciona os registros onde o ano é menor ou igual a 2015 (Se for númerico pode sem sem aspas)
ORDER BY ano, nome;

SELECT ano, nome, descricao FROM cursos
WHERE ano < 2015
ORDER BY ano, nome;

SELECT ano, nome, descricao FROM cursos
WHERE ano > 2016
ORDER BY ano, nome;

SELECT ano, nome, descricao FROM cursos
WHERE ano >= 2016
ORDER BY ano;

SELECT ano, nome, descricao FROM cursos
WHERE ano != 2016  -- O símbolo de diferente pode ser representado também como "<>"
ORDER BY ano, nome;

-- Filtrando as linhas com a cláusula WHERE usando OPERADORES mais AVANÇADOS
SELECT * FROM cursos
WHERE totaulas BETWEEN '20' AND '30'  -- BETWEEN significa entre, ou seja, "onde o totaulas esteja entre 20 e 30"
ORDER BY totaulas, nome;

SELECT ano, nome, descricao FROM cursos
WHERE ano BETWEEN 2015 AND 2018
ORDER BY ano DESC, nome ASC;

SELECT ano, nome, descricao FROM cursos
WHERE ano IN (2014, 2016, 2018)  -- No IN é possível especificar valores
ORDER BY ano DESC, nome;

-- Combinando operadores e formando expressões lógicas nas filtragens com a cláusula WHERE
SELECT nome, carga, totaulas FROM cursos
WHERE carga > 35 AND totaulas < 30;

SELECT nome, carga, totaulas FROM cursos
WHERE carga > 35 OR totaulas < 30;
 