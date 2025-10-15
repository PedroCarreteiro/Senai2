create database filmes;

use filmes;

CREATE TABLE filme (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	titulo VARCHAR(255) NOT NULL,
	orcamento FLOAT NOT NULL,
	tempo_duracao INTEGER NOT NULL,
	ano YEAR NOT NULL,
	orcamento DECIMAL NOT NULL,
	tempo_duracao TIME NOT NULL,
	ano DATE NOT NULL,
	poster VARCHAR(255),
	PRIMARY KEY(id)
);


CREATE TABLE genero (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	nome VARCHAR(255) NOT NULL,
	PRIMARY KEY(id)
);


CREATE TABLE filme_genero (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	id_filme INTEGER NOT NULL,
	id_genero INTEGER NOT NULL,
	PRIMARY KEY(id),
    FOREIGN KEY (id_filme) REFERENCES filme(id),
    FOREIGN KEY (id_genero) REFERENCES genero(id)
);

CREATE TABLE ator (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	nome VARCHAR(255) NOT NULL,
	sobrenome VARCHAR(255) NOT NULL,
	id_sexo INTEGER NOT NULL,
	PRIMARY KEY(id)
);


CREATE TABLE sexo (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	nome VARCHAR(255) NOT NULL,
	PRIMARY KEY(id)
);


CREATE TABLE diretor (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	nome VARCHAR(255) NOT NULL,
	sobrenome VARCHAR(255) NOT NULL,
	id_sexo INTEGER NOT NULL,
	PRIMARY KEY(id)
);


CREATE TABLE nacionalidade (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	nome VARCHAR(255) NOT NULL,
	id_pais INTEGER NOT NULL,
	PRIMARY KEY(id)
);


CREATE TABLE pais (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	nome VARCHAR(255) NOT NULL,
	PRIMARY KEY(id)
);


CREATE TABLE produtora (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	nome VARCHAR(255) NOT NULL,
	PRIMARY KEY(id)
);


CREATE TABLE linguagem (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	nome VARCHAR(255) NOT NULL,
	PRIMARY KEY(id)
);


CREATE TABLE filme_diretor (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	id_filme INTEGER NOT NULL,
	id_diretor INTEGER NOT NULL,
	PRIMARY KEY(id),
    FOREIGN KEY (id_filme) REFERENCES filme(id),
    FOREIGN KEY (id_diretor) REFERENCES diretor(id)
);


CREATE TABLE filme_ator (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	id_filme INTEGER NOT NULL,
	id_ator INTEGER NOT NULL,
	PRIMARY KEY(id),
    FOREIGN KEY (id_filme) REFERENCES filme(id),
    FOREIGN KEY (id_ator) REFERENCES ator(id)
);


CREATE TABLE filme_linguagem (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	id_filme INTEGER NOT NULL,
	id_linguagem INTEGER NOT NULL,
	PRIMARY KEY(id),
    FOREIGN KEY (id_filme) REFERENCES filme(id),
    FOREIGN KEY (id_linguagem) REFERENCES linguagem(id)
);


CREATE TABLE filme_pais (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	id_filme INTEGER NOT NULL,
	id_pais INTEGER NOT NULL,
	PRIMARY KEY(id),
    FOREIGN KEY (id_filme) REFERENCES filme(id),
    FOREIGN KEY (id_pais) REFERENCES pais(id)
);


CREATE TABLE filme_produtora (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	id_filme INTEGER NOT NULL,
	id_produtora INTEGER NOT NULL,
	PRIMARY KEY(id),
    FOREIGN KEY (id_filme) REFERENCES filme(id),
    FOREIGN KEY (id_produtora) REFERENCES produtora(id)
);


CREATE TABLE ator_nacionalidade (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	id_ator INTEGER NOT NULL,
	id_nacionalidade INTEGER NOT NULL,
	PRIMARY KEY(id),
    FOREIGN KEY (id_ator) REFERENCES ator(id),
    FOREIGN KEY (id_nacionalidade) REFERENCES nacionalidade(id)
);


CREATE TABLE diretor_nacionalidade (
	id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	id_diretor INTEGER NOT NULL,
	id_nacionalidade INTEGER NOT NULL,
	PRIMARY KEY(id),
    FOREIGN KEY (id_diretor) REFERENCES diretor(id),
    FOREIGN KEY (id_nacionalidade) REFERENCES nacionalidade(id)
);