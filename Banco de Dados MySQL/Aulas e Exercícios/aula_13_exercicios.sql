
USE cadastro;

SELECT * FROM gafanhotos;

-- 1. Uma lista com as profissoes dos gafanhatos e seus respectivos quantitativos

SELECT profissao, COUNT(*) FROM gafanhotos
GROUP BY profissao
ORDER BY COUNT(*) DESC;

-- 2.  Quantos gafanhotos homens e mulheres nasceram após 01/jan/2005?

SELECT sexo, COUNT(*) FROM gafanhotos
WHERE nascimento > '2005-01-01'
GROUP BY sexo;

-- 3. Uma lista com gafanhotos que nasceram fora do Brasil, mostrando o país de origem e o total de pessoas nascidas lá. 
--    Só nos interessam os países que tiverem mais de 3 gafanhotos com essa nacionalidade.

SELECT nacionalidade, COUNT(*) FROM gafanhotos
WHERE nacionalidade != 'Brasil'
GROUP BY nacionalidade
HAVING COUNT(*) > 3
ORDER BY COUNT(*) DESC;

-- 4. Uma lista agrupada pela altura dos gafanhotos, mostrando quantas pessoas pesam mais de 100kg e que estão acima da média da altura de todos os cadastrados

SELECT altura, peso, COUNT(*) FROM gafanhotos
WHERE peso > '100.00'
GROUP BY altura
HAVING altura > (SELECT AVG(altura) FROM gafanhotos)
ORDER BY altura DESC;

-- 5. Agrupe a nacionalidade de todos os gafanhotos homens nascidos entre 01-01-1990 à 31-12-2020. 
--    O resultado tem ser visto da nacionalidade com menor número de gafanhotos ao maior

SELECT nacionalidade, COUNT(*) FROM gafanhotos
WHERE sexo = 'M' AND nascimento BETWEEN '1990-01-01' AND '2020-12-31'
GROUP BY nacionalidade
ORDER BY COUNT(*);

-- 6. Agrupe o peso de todos os gafanhotos sendo que só devem aparecer o peso que contém mais de um gafanhotos

SELECT peso, COUNT(*) FROM gafanhotos
GROUP BY peso
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC;

-- 7. Agrupe a altura de todos os gafanhotos sendo que só devem ser mostrados aquelas que contem 4 à 6 gafanhotos. 
--    À altura e o número de gafanhotos deve ser mostrado de forma descendente

SELECT altura, COUNT(*) FROM gafanhotos
GROUP BY altura
HAVING COUNT(*) BETWEEN 4 AND 6
ORDER BY altura DESC, COUNT(*) DESC;

-- 8. Agrupe o total de aulas existentes nos cursos feitos no ano de 2016, 2018 e 2019. Só devem ser mostrados
--    o total de aulas iguais ou acima da méida de aulas, ordenados pela quantidade existente nelas

SELECT totaulas, COUNT(*) FROM cursos
WHERE ano IN (2016, 2018, 2019)
GROUP BY totaulas
HAVING totaulas >= (SELECT AVG(totaulas) FROM cursos)
ORDER BY COUNT(*) DESC;
 