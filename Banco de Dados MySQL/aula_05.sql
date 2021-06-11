
USE cadastro;

-- Insira na tabela pessoas os valores

INSERT INTO pessoas
(id, nome, nascimento, sexo, peso, altura, nacionalidade)
VALUES
(DEFAULT, 'Creuza', '1920-12-30', 'F', '50.3', '1.65', DEFAULT);  -- Para o BD tudo que está entre aspas símples são dados

-- Se a ordem dos campos for a mesma que a ordem que foi definida no banco, não
-- é necessário informar os campos entre parenteses, ou seja, pode ser feito assim:

INSERT INTO pessoas VALUES
(DEFAULT, 'Adalgiza', '1930-11-2', 'F', '63.2', '1.75', 'Irlanda');

-- Modo de inserção de várias instâncias separadas por vírgulas:

INSERT INTO pessoas VALUES
(DEFAULT, 'Cláudio', '1975-04-22', 'M', '99.0', '2.15', 'Brasil'),
(DEFAULT, 'Pedro', '1999-12-03', 'M', '87', '2', DEFAULT),
(DEFAULT, 'Janaína', '1987-11-12', 'F', '75.4', '1.66', 'EUA');	

SELECT * FROM pessoas;
