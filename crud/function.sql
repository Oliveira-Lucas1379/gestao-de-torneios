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
