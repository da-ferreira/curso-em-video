
USE cadastro;

-- Criando uma nova tabela para entidade 'assiste' na cardinalidade muitos-para-muitos:
-- |Gafanhoto| n ...<Assiste>... n |Curso|, que se torna
-- |Gafanhoto| 1...<>...n |Assiste| n...<>...1 |Curso|

CREATE TABLE gafanhoto_assiste_curso (
    id          int NOT NULL AUTO_INCREMENT,
    data        date,
    idgafanhoto int,
    idcurso     int,
    PRIMARY KEY (id),
    FOREIGN KEY (idgafanhoto) REFERENCES gafanhotos(id),
    FOREIGN KEY (idcurso) REFERENCES cursos(idcurso)
) DEFAULT CHARSET = utf8mb4;

-- Inserindo os registros na tabela:

INSERT INTO gafanhoto_assiste_curso VALUES
(DEFAULT, '2014-03-01', '1', '2');

INSERT INTO gafanhoto_assiste_curso VALUES
(DEFAULT, '2015-12-22', '3', '6'),
(DEFAULT, '2014-01-01', '22', '12'),
(DEFAULT, '2016-05-12', '1', '19');

SELECT * FROM gafanhoto_assiste_curso;

SELECT gafanhotos.id, gafanhotos.nome, assiste.idgafanhoto, assiste.idcurso FROM gafanhotos  
INNER JOIN gafanhoto_assiste_curso AS assiste  -- Não é necessário colocar o 'AS' para dar um apelido
ON gafanhotos.id = assiste.idgafanhoto;

-- Sem o id do gafanhoto
SELECT gafanhotos.nome, assiste.idcurso FROM gafanhotos  
INNER JOIN gafanhoto_assiste_curso AS assiste
ON gafanhotos.id = assiste.idgafanhoto
ORDER BY gafanhotos.nome;

-- Join com mais de duas tabelas e dando apelido para atributos
SELECT gafanhotos.nome AS 'Nome do gafanhoto', cursos.nome AS 'Nome do curso', cursos.descricao AS 'Descrição do curso', assiste.idcurso AS 'ID do curso' FROM gafanhotos 
INNER JOIN gafanhoto_assiste_curso AS assiste
ON gafanhotos.id = assiste.idgafanhoto
INNER JOIN cursos
ON assiste.idcurso = cursos.idcurso
ORDER BY gafanhotos.nome;
 