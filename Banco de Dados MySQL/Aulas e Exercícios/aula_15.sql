
USE cadastro;
DESCRIBE gafanhotos;

-- Adicionando a chave estrangeira (Foreign Key) 'curso_preferido' na tabela 'gafanhotos'
ALTER TABLE gafanhotos
ADD COLUMN curso_preferido int;

ALTER TABLE gafanhotos
ADD FOREIGN KEY (curso_preferido)
REFERENCES cursos(idcurso);  -- Indicando que qual tabela é a chave primária que virou estrangeira

SELECT * FROM gafanhotos;
SELECT * FROM cursos;

-- Adicionando as chaves estrangeiras aos registros (o curso preferido de cada pessoa)
UPDATE gafanhotos
SET curso_preferido = '6'
WHERE id = '1';

-- Integridade Referencial: não é possivel apagar o curso cujo idcurso é igual a '6' porque há algum relacionamento com o registro
DELETE FROM cursos
WHERE idcurso = '6';

-- Já o registro abaixo não contém nenhuma relação, logo é possível apaga-lo
DELETE FROM cursos
WHERE idcurso = '28';

-- Join (inner join) -> juntando a tabela 'gafanhotos' com a tabela 'cursos' com a cláusula ON.
-- A cláusula ON da sentido a junção das tabelas, referenciando as relações que ligam um registro de uma tabela na outra
SELECT gafanhotos.nome, cursos.nome, cursos.ano 
FROM gafanhotos INNER JOIN cursos 
ON cursos.idcurso = gafanhotos.curso_preferido
ORDER BY gafanhotos.nome;

-- Usando apelidos para tabelas com AS
SELECT g.nome, c.nome, c.ano 
FROM gafanhotos AS g INNER JOIN cursos AS c 
ON c.idcurso = g.curso_preferido
ORDER BY g.nome;

-- Left Outer Join (ou só left join) -> Dá preferencia a tabela que está no lado ESQUERDO do JOIN
SELECT gafanhotos.nome, cursos.nome, cursos.ano 
FROM gafanhotos LEFT OUTER JOIN cursos 
ON cursos.idcurso = gafanhotos.curso_preferido;

-- Right Outer Join (ou só right join) -> Dá preferencia a tabela que está no lado DIREITO do JOIN
SELECT gafanhotos.nome, cursos.nome, cursos.ano 
FROM gafanhotos RIGHT OUTER JOIN cursos 
ON cursos.idcurso = gafanhotos.curso_preferido;
 