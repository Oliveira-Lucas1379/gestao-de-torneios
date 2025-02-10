CREATE VIEW VisaoGeralTorneios AS
SELECT 
    T.CodTorneio,
    T.Nome AS NomeTorneio,
    T.DataInicial,
    T.DataFinal,
    R.Nome AS Regiao,
    Ti.Divisao AS Tier,
    O.Nome AS Organizador,
    STRING_AGG(DISTINCT P.Nome, ', ') AS Patrocinadores,
    STRING_AGG(DISTINCT Ti2.Nome, ', ') AS TimesParticipantes,
    STRING_AGG(DISTINCT Tec.Nome, ', ') AS Tecnicos,
    STRING_AGG(DISTINCT J.Nome, ', ') AS Jogadores
FROM 
    Torneio T
LEFT JOIN 
    Regiao R ON T.CodRegiao = R.CodRegiao
LEFT JOIN 
    Tier Ti ON T.CodTier = Ti.CodTier
LEFT JOIN 
    Organizadores O ON T.CodOrganizador = O.CodOrganizador
LEFT JOIN 
    Torneio_Patrocinador TP ON T.CodTorneio = TP.CodTorneio
LEFT JOIN 
    Patrocinadores P ON TP.CodPatrocinador = P.CodPatrocinador
LEFT JOIN 
    Classificacoes C ON T.CodTorneio = C.CodTorneio
LEFT JOIN 
    Times Ti2 ON C.CodTime = Ti2.CodTime
LEFT JOIN 
    Tecnico Tec ON Ti2.CodTime = Tec.CodTime
LEFT JOIN 
    Jogadores J ON Ti2.CodTime = J.CodTime
GROUP BY 
    T.CodTorneio, T.Nome, T.DataInicial, T.DataFinal, R.Nome, Ti.Divisao, O.Nome;

SELECT * FROM VisaoGeralTorneios;