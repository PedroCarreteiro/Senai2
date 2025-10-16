USE filmes;

-- 1. Tabelas sem dependência

-- Tabela: sexo
INSERT INTO sexo (nome) VALUES
('Masculino'), -- id = 1
('Feminino'),  -- id = 2
('Não Binário'); -- id = 3

-- Tabela: pais
INSERT INTO pais (nome) VALUES
('Estados Unidos'), -- id = 1
('Brasil'),         -- id = 2
('Reino Unido'),    -- id = 3
('Coreia do Sul'),  -- id = 4
('Japão');          -- id = 5

-- Tabela: produtora
INSERT INTO produtora (nome) VALUES
('Warner Bros'),     -- id = 1
('Paramount Pictures'), -- id = 2
('Miramax Films'),    -- id = 3
('20th Century Fox'), -- id = 4
('Studio Ghibli');    -- id = 5

-- Tabela: linguagem
INSERT INTO linguagem (nome) VALUES
('Inglês'),       -- id = 1
('Português'),    -- id = 2
('Espanhol'),     -- id = 3
('Coreano'),      -- id = 4
('Japonês');      -- id = 5

-- Tabela: genero
INSERT INTO genero (nome) VALUES
('Drama'),        -- id = 1
('Ação'),         -- id = 2
('Comédia'),      -- id = 3
('Ficção Científica'), -- id = 4
('Animação'),     -- id = 5
('Suspense');     -- id = 6


-- 2. Tabelas com dependência simples

-- Tabela: filme (Reutilizando os 20 INSERTs do pedido anterior)
INSERT INTO filme (titulo, orcamento, tempo_duracao, ano, poster) VALUES
('O Poderoso Chefão', 6000000.00, 175, 1972, 'caminho/para/poster1.jpg'),       -- id = 1
('Um Sonho de Liberdade', 25000000.00, 142, 1994, 'caminho/para/poster2.jpg'),  -- id = 2
('A Lista de Schindler', 22000000.00, 195, 1993, 'caminho/para/poster3.jpg'),   -- id = 3
('O Cavaleiro das Trevas', 185000000.00, 152, 2008, 'caminho/para/poster4.jpg'), -- id = 4
('Pulp Fiction: Tempo de Violência', 8000000.00, 154, 1994, 'caminho/para/poster5.jpg'), -- id = 5
('O Senhor dos Anéis: O Retorno do Rei', 94000000.00, 201, 2003, 'caminho/para/poster6.jpg'), -- id = 6
('Forrest Gump: O Contador de Histórias', 55000000.00, 142, 1994, 'caminho/para/poster7.jpg'), -- id = 7
('A Origem', 160000000.00, 148, 2010, 'caminho/para/poster8.jpg'),               -- id = 8
('Clube da Luta', 63000000.00, 139, 1999, 'caminho/para/poster9.jpg'),           -- id = 9
('Matrix', 63000000.00, 136, 1999, 'caminho/para/poster10.jpg'),                 -- id = 10
('Parasita', 11300000.00, 132, 2019, 'caminho/para/poster11.jpg'),               -- id = 11
('Interestelar', 165000000.00, 169, 2014, 'caminho/para/poster12.jpg'),         -- id = 12
('Guerra nas Estrelas: Uma Nova Esperança', 11000000.00, 121, 1977, 'caminho/para/poster13.jpg'), -- id = 13
('Vingadores: Ultimato', 356000000.00, 181, 2019, 'caminho/para/poster14.jpg'),  -- id = 14
('Titanic', 200000000.00, 195, 1997, 'caminho/para/poster15.jpg'),               -- id = 15
('O Resgate do Soldado Ryan', 70000000.00, 169, 1998, 'caminho/para/poster16.jpg'), -- id = 16
('Whiplash: Em Busca da Perfeição', 3300000.00, 107, 2014, 'caminho/para/poster17.jpg'), -- id = 17
('Mad Max: Estrada da Fúria', 150000000.00, 120, 2015, 'caminho/para/poster18.jpg'), -- id = 18
('A Viagem de Chihiro', 15000000.00, 125, 2001, 'caminho/para/poster19.jpg'),    -- id = 19
('Cidade de Deus', 3300000.00, 130, 2002, 'caminho/para/poster20.jpg');          -- id = 20

-- Tabela: nacionalidade (depende de pais)
INSERT INTO nacionalidade (nome, id_pais) VALUES
('Americana', 1),   -- id = 1
('Brasileira', 2),  -- id = 2
('Britânica', 3),   -- id = 3
('Sul-coreana', 4); -- id = 4

-- Tabela: ator (depende de sexo)
INSERT INTO ator (nome, sobrenome, id_sexo) VALUES
('Tom', 'Hanks', 1),      -- id = 1
('Morgan', 'Freeman', 1), -- id = 2
('Keanu', 'Reeves', 1),   -- id = 3
('Brad', 'Pitt', 1),      -- id = 4
('Sandra', 'Bullock', 2), -- id = 5
('Alice', 'Braga', 2);    -- id = 6

-- Tabela: diretor (depende de sexo)
INSERT INTO diretor (nome, sobrenome, id_sexo) VALUES
('Steven', 'Spielberg', 1),   -- id = 1
('Quentin', 'Tarantino', 1),  -- id = 2
('Christopher', 'Nolan', 1),  -- id = 3
('Hayao', 'Miyazaki', 1),     -- id = 4
('Fernando', 'Meirelles', 1); -- id = 5


-- 3. Tabelas de relacionamento (Nacionalidade)

-- Tabela: ator_nacionalidade
INSERT INTO ator_nacionalidade (id_ator, id_nacionalidade) VALUES
(1, 1), -- Tom Hanks (Americana)
(2, 1), -- Morgan Freeman (Americana)
(3, 1), -- Keanu Reeves (Americana)
(6, 2); -- Alice Braga (Brasileira)

-- Tabela: diretor_nacionalidade
INSERT INTO diretor_nacionalidade (id_diretor, id_nacionalidade) VALUES
(1, 1), -- Steven Spielberg (Americana)
(2, 1), -- Quentin Tarantino (Americana)
(3, 3), -- Christopher Nolan (Britânica - assumindo)
(5, 2); -- Fernando Meirelles (Brasileira)


-- 4. Tabelas de relacionamento de filme (N:M)

-- Tabela: filme_genero (Drama, Ação, Ficção, etc.)
INSERT INTO filme_genero (id_filme, id_genero) VALUES
(1, 1),  -- O Poderoso Chefão (Drama)
(4, 2),  -- O Cavaleiro das Trevas (Ação)
(4, 6),  -- O Cavaleiro das Trevas (Suspense)
(8, 4),  -- A Origem (Ficção Científica)
(10, 4), -- Matrix (Ficção Científica)
(11, 6), -- Parasita (Suspense)
(19, 5), -- A Viagem de Chihiro (Animação)
(20, 1); -- Cidade de Deus (Drama)

-- Tabela: filme_diretor
INSERT INTO filme_diretor (id_filme, id_diretor) VALUES
(3, 1),  -- A Lista de Schindler (Steven Spielberg)
(5, 2),  -- Pulp Fiction (Quentin Tarantino)
(8, 3),  -- A Origem (Christopher Nolan)
(12, 3), -- Interestelar (Christopher Nolan)
(19, 4), -- A Viagem de Chihiro (Hayao Miyazaki)
(20, 5); -- Cidade de Deus (Fernando Meirelles)

-- Tabela: filme_ator
INSERT INTO filme_ator (id_filme, id_ator) VALUES
(7, 1),  -- Forrest Gump (Tom Hanks)
(2, 2),  -- Um Sonho de Liberdade (Morgan Freeman)
(10, 3), -- Matrix (Keanu Reeves)
(9, 4),  -- Clube da Luta (Brad Pitt)
(18, 6); -- Mad Max (Alice Braga)

-- Tabela: filme_linguagem
INSERT INTO filme_linguagem (id_filme, id_linguagem) VALUES
(1, 1),  -- O Poderoso Chefão (Inglês)
(11, 4), -- Parasita (Coreano)
(19, 5), -- A Viagem de Chihiro (Japonês)
(20, 2); -- Cidade de Deus (Português)

-- Tabela: filme_pais (país de origem principal)
INSERT INTO filme_pais (id_filme, id_pais) VALUES
(1, 1),  -- O Poderoso Chefão (EUA)
(11, 4), -- Parasita (Coreia do Sul)
(19, 5), -- A Viagem de Chihiro (Japão)
(20, 2); -- Cidade de Deus (Brasil)

-- Tabela: filme_produtora
INSERT INTO filme_produtora (id_filme, id_produtora) VALUES
(1, 2),  -- O Poderoso Chefão (Paramount)
(4, 1),  -- O Cavaleiro das Trevas (Warner Bros)
(5, 3),  -- Pulp Fiction (Miramax)
(19, 5); -- A Viagem de Chihiro (Studio Ghibli)
