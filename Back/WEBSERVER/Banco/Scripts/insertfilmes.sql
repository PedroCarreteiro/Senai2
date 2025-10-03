use filmes;

insert into filme(titulo, orcamento, tempo_duracao, ano, poster)
VALUES
("Magu, o Retorno", 40000000.90, '02:30:02', 2025, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRqrhjmE6FuJ5r5Ad7bRm4UsnU_sNyDZVREg&s"),
("Piratas do Caribe", 189200000.00, '02:10:02', 2002, "https://m.media-amazon.com/images/I/91FIMaQlveL._UF894,1000_QL80_.jpg"),
("Valozes e Furiosos", 10371387.00, '01:33:02', 2012, "https://play-lh.googleusercontent.com/CorMIImjzd88bsUQTd8yTntjXqyMBYX7gdy9BCpCRFcd1fekoNby7MnW1KG8hDlp9P13"),
("Need For Speed", 108389163.00, '03:02:24', 2011, "https://br.web.img2.acsta.net/pictures/14/03/08/08/41/128657.jpg"),
("Formula 1", 19631314.00, '03:01:02', 2025, "https://m.media-amazon.com/images/S/pv-target-images/621953c18a79f28d07670e1c78827b4d8bb63c076c78481795f031c76a2ae41f.jpg"),
("Era uma vez em Hollywood", 92949221.00, '01:49:13', 2016, "https://br.web.img3.acsta.net/pictures/19/08/06/21/50/5749668.jpg"),
("Gran Turismo", 31471924.00, '02:59:24', 2017, "https://br.web.img2.acsta.net/pictures/23/06/30/20/36/1745850.jpg"),
("Gladiador", 87873289.00, '02:30:35', 2012, "https://upload.wikimedia.org/wikipedia/pt/4/44/GladiadorPoster.jpg"),
("Percy Jackson", 3742986493.00, '03:30:29', 2019, "https://br.web.img3.acsta.net/medias/nmedia/18/87/90/23/19962722.jpg"),
("Onde os Fracos não tem Vez", 27643062.00, '02:20:03', 2019, "https://m.media-amazon.com/images/S/pv-target-images/d3ace3a42566abd92090b2823b312711b6bab90e80240a5bfaac60bb65e06d81.jpg"),
("Batman", 924274042.00, '02:12:02', 2019, "https://br.web.img3.acsta.net/medias/nmedia/18/86/98/32/19870786.jpg"),
("Superman", 20482842.00, '01:01:01', 2019, "https://br.web.img3.acsta.net/img/86/64/8664d1b110b95eb32313683f1a655f5f.jpg"),
("Miranha", 247294790.00, '02:50:50', 2019, "https://www.sonypictures.com.br/sites/brazil/files/2022-03/DP_3409108_TC_1400x2100_DP_3409112_SpiderManHomecoming_INTL_2017_2000x3000_BR_thumbnail_xlarge.jpg"),
("Homem de Ferro", 992429411.00, '02:55:05', 2019, "https://upload.wikimedia.org/wikipedia/pt/1/19/Iron_Man_3_poster.jpg"),
("Vingadores", 19209742.00, '01:30:01', 2019, "https://br.web.img2.acsta.net/medias/nmedia/18/89/43/82/20052140.jpg"),
("Forrest Gump", 385720224.00, '03:40:50', 2019, "https://upload.wikimedia.org/wikipedia/pt/c/c0/ForrestGumpPoster.jpg"),
("Django Livre", 20947274.00, '02:30:30', 2019, "https://br.web.img3.acsta.net/c_310_420/medias/nmedia/18/90/07/53/20391069.jpg"),
("Interestellar", 20472071.00, '02:10:02', 2019, "https://upload.wikimedia.org/wikipedia/pt/3/3a/Interstellar_Filme.png"),
("Openheimmer", 24092741.00, '03:20:57', 2019, "https://movienonsense.com/wp-content/uploads/2023/12/oppenheimer.jpg"),
("Matrix", 98842842.00, '03:40:20', 2019, "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/The_Matrix.png/250px-The_Matrix.png");

insert into genero(nome)
values
("Suspense"),
("SciFi"),
("Histórico"),
("Ação"),
("Aventura"),
("Terror"),
("Drama"),
("Ficção");

insert into filme_genero(id_filme, id_genero)
values
(1,6),
(2,4),
(2,5),
(2,8),
(3,4),
(4,4),
(4,5),
(5,4),
(5,7),
(6,7),
(6,4),
(7,4),
(7,7),
(8,5),
(8,3),
(9,8),
(9,5),
(9,4),
(10,1),
(11,8),
(11,4),
(12,4),
(12,8),
(13,4),
(13,8),
(14,4),
(14,8),
(14,2),
(15,2),
(15,4),
(15,8),
(16,7),
(16,3),
(16,5),
(17,3),
(17,4),
(17,5),
(18,2),
(18,5),
(18,8),
(19,1),
(19,3),
(19,7),
(19,8),
(20,2),
(20,4),
(20,8);


insert into sexo(nome)
values
("Feminino"),
("Masculino"),
("Não binário");


insert into ator(nome, sobrenome, id_sexo)
values
("Magu", "Sores", 2),
("Robert", "Downey Jr", 2),
("Lucas", "Black", 2),
("Sung", "Kang", 1),
("Aaron", "Paul", 2),
("Imogen Poots", "Paul", 1);




