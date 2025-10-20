CREATE OR REPLACE FUNCTION fn_creator_with_board_games(first_name1 VARCHAR(30))
RETURNS BIGINT
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN
    (SELECT
        count(*)
    FROM
        board_games AS bg
        JOIN creators_board_games AS cb
        ON bg.id = cb.board_game_id
            JOIN creators AS cr
            ON cr.id = cb.creator_id
    WHERE
        cr.first_name = first_name1);
END; $$;
