CREATE OR REPLACE FUNCTION fn_is_game_over(is_game_over BOOLEAN)
RETURNS TABLE("name" VARCHAR(50), game_type_id INTEGER, is_finished BOOLEAN)
LANGUAGE plpgsql
AS $$
BEGIN
    IF is_game_over IS TRUE THEN
        RETURN QUERY
            SELECT games."name", games.game_type_id, games.is_finished FROM games WHERE games.is_finished IS TRUE;
    ELSE
        RETURN QUERY
            SELECT games."name", games.game_type_id, games.is_finished FROM games WHERE games.is_finished IS FALSE;
    END IF;
END;
$$
