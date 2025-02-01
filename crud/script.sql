-- Criando as tabelas principais
CREATE TABLE Organizadores (
    CodOrganizador SERIAL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL
);

CREATE TABLE Patrocinadores (
    CodPatrocinador SERIAL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Origem VARCHAR(255)
);

CREATE TABLE Regiao (
    CodRegiao SERIAL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Localizacao VARCHAR(255)
);

CREATE TABLE Tier (
    CodTier SERIAL PRIMARY KEY,
    Nivel VARCHAR(50) NOT NULL
);

CREATE TABLE Tecnico (
    ID_Tecnico SERIAL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Tipo VARCHAR(100) NOT NULL
);

CREATE TABLE Times (
    CodTime SERIAL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Logo BYTEA
);

CREATE TABLE Jogadores (
    ID_Jogador SERIAL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Funcao VARCHAR(100) NOT NULL,
    CodTime INT REFERENCES Times(CodTime)
);

CREATE TABLE Torneio (
    CodTorneio INT PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Data DATE NOT NULL,
    CodOrganizador INT REFERENCES Organizadores(CodOrganizador),
    CodTier INT REFERENCES Tier(CodTier)
);

CREATE TABLE Partidas (
    CodPartida SERIAL PRIMARY KEY,
    Data DATE NOT NULL,
    CodTorneio INT REFERENCES Torneio(CodTorneio),
    CodTimeVencedor INT REFERENCES Times(CodTime) NULL,
    CodTimePerdedor INT REFERENCES Times(CodTime) NULL,
    EstadoPartida VARCHAR(50) CHECK (EstadoPartida IN ('Concluída', 'Em Andamento', 'Agendada'))
);

CREATE TABLE Classificacoes (
    CodClassificacao SERIAL PRIMARY KEY,
    Classificacao INT NOT NULL,
    Premiacao DECIMAL(10,2),
    CodTime INT REFERENCES Times(CodTime),
    CodTorneio INT REFERENCES Torneio(CodTorneio)
);

-- Tabelas de relacionamento
CREATE TABLE Torneio_Patrocinador (
    CodTorneio INT REFERENCES Torneio(CodTorneio),
    CodPatrocinador INT REFERENCES Patrocinadores(CodPatrocinador),
    PRIMARY KEY (CodTorneio, CodPatrocinador)
);

CREATE TABLE Torneio_Regiao (
    CodTorneio INT REFERENCES Torneio(CodTorneio),
    CodRegiao INT REFERENCES Regiao(CodRegiao),
    PRIMARY KEY (CodTorneio, CodRegiao)
);

CREATE TABLE Tecnico_Time (
    ID_Tecnico INT REFERENCES Tecnico(ID_Tecnico),
    CodTime INT REFERENCES Times(CodTime),
    PRIMARY KEY (ID_Tecnico, CodTime)
);
