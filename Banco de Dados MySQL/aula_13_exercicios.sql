
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
 