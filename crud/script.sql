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
    Divisao VARCHAR(50) NOT NULL
);

CREATE TABLE Times (
    CodTime SERIAL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Logo BYTEA
);

CREATE TABLE Tecnico (
    ID_Tecnico SERIAL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Funcao VARCHAR(100) NOT NULL,
    CodTime INT,
    FOREIGN KEY (CodTime) REFERENCES Times(CodTime)
);

CREATE TABLE Jogadores (
    ID_Jogador SERIAL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Funcao VARCHAR(100) NOT NULL,
    CodTime INT,
    FOREIGN KEY (CodTime) REFERENCES Times(CodTime)
);

CREATE TABLE Torneio (
    CodTorneio INT PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    DataInicial DATE,
	DataFinal DATE,
    CodRegiao INT,
    CodTier INT,
    CodOrganizador INT,
    FOREIGN KEY (CodRegiao) REFERENCES Regiao(CodRegiao),
    FOREIGN KEY (CodTier) REFERENCES Tier(CodTier),
    FOREIGN KEY (CodOrganizador) REFERENCES Organizadores(CodOrganizador),
);

CREATE TABLE Resultados (
    id SERIAL PRIMARY KEY,
    Resultado VARCHAR(50),
    CodTimeVencedor INT,
    CodTimePerdedor INT,
    FOREIGN KEY (CodTimeVencedor) REFERENCES Times(CodTime),
    FOREIGN KEY (CodTimePerdedor) REFERENCES Times(CodTime)
);

CREATE TABLE Partidas (
    CodPartida SERIAL PRIMARY KEY,
    Data DATE NOT NULL,
    CodTorneio INT,
    idResultado INT,
    FOREIGN KEY (CodTorneio) REFERENCES Torneio(CodTorneio),
    FOREIGN KEY (idResultado) REFERENCES Resultados(id)
);

CREATE TABLE Premiacao (
    Colocacao SERIAL PRIMARY KEY,
    ValorPremiacao DECIMAL(10,2)
);

CREATE TABLE Classificacoes (
    id SERIAL PRIMARY KEY,
    Colocacao INT,
    CodTime INT,
    CodTorneio INT,
    FOREIGN KEY (Colocacao) REFERENCES Premiacao(Colocacao),
    FOREIGN KEY (CodTime) REFERENCES Times(CodTime),
    FOREIGN KEY (CodTorneio)  REFERENCES Torneio(CodTorneio)
);

-- Tabelas de relacionamento
CREATE TABLE Torneio_Patrocinador (
    CodTorneio INT,
    CodPatrocinador INT,
    PRIMARY KEY (CodTorneio, CodPatrocinador),
    FOREIGN KEY (CodTorneio) REFERENCES Torneio(CodTorneio),
    FOREIGN KEY (CodPatrocinador) REFERENCES Patrocinadores(CodPatrocinador)
);

CREATE TABLE Times_Partidas (
    CodPartida INT,
    CodTime INT,
    PRIMARY KEY (CodPartida, CodTime),
    FOREIGN KEY (CodPartida) REFERENCES Partidas(CodPartida),
    FOREIGN KEY (CodTime) REFERENCES Times(CodTime)
);


-- Criando as FUNCTIONS
CREATE OR REPLACE FUNCTION GetTimesByTorneio(torneio_id INT)
RETURNS TABLE(TimeId INT)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT T.CodTime AS Time
    FROM Times T
    JOIN Times_Partidas TP ON T.CodTime = TP.CodTime
    JOIN Partidas P ON TP.CodPartida = P.CodPartida
    JOIN Torneio TR ON P.CodTorneio = TR.CodTorneio
    WHERE TR.CodTorneio = torneio_id;
END;
$$;
