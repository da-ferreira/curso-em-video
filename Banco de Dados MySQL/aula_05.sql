
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
(DEFAULT, 'David Ferreira', '2002-11-07', 'M', '60.0', '1.70', 'Brasil'),
(DEFAULT, 'Kaio Vinicius', '2001-05-02', 'M', 80.5, 1.82, DEFAULT),
(DEFAULT, 'Kelli Francis', '2000-05-15', 'F', 62.5, 1.70, 'Canadá'),
(DEFAULT, 'Sorra Marcs', '1980-11-22', 'F', 60.5, 1.60, 'França'),
(DEFAULT, 'Francis Mandela', '1983-10-15', 'M', 72.3, 1.75, 'África do Sul');

SELECT * FROM pessoas;
