CREATE OR REPLACE PROCEDURE VerificarTorneio(
    p_cod_torneio INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_organizador VARCHAR(255);
    v_patrocinadores TEXT;
    v_times_participantes TEXT;
BEGIN
    -- Obter o organizador do torneio
    SELECT Organizador INTO v_organizador
    FROM VisaoGeralTorneios
    WHERE CodTorneio = p_cod_torneio;
    
    -- Obter patrocinadores do torneio
    SELECT Patrocinadores INTO v_patrocinadores
    FROM VisaoGeralTorneios
    WHERE CodTorneio = p_cod_torneio;

    -- Obter times participantes do torneio
    SELECT TimesParticipantes INTO v_times_participantes
    FROM VisaoGeralTorneios
    WHERE CodTorneio = p_cod_torneio;

    -- Verificação condicional
    IF v_organizador IS NULL THEN
        RAISE EXCEPTION 'Erro: O torneio % não tem um organizador associado!', p_cod_torneio;
    ELSIF v_patrocinadores IS NULL OR v_patrocinadores = '' THEN
        RAISE NOTICE 'Aviso: O torneio % não tem patrocinadores!', p_cod_torneio;
    ELSIF v_times_participantes IS NULL OR v_times_participantes = '' THEN
        RAISE NOTICE 'Aviso: O torneio % não tem times participantes!', p_cod_torneio;
    ELSE
        RAISE NOTICE 'Torneio % está completo com organizador, patrocinadores e times participantes.', p_cod_torneio;
    END IF;
END;
$$;

CALL VerificarTorneio(4);