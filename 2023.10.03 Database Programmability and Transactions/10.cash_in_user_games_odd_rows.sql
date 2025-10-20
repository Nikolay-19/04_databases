CREATE OR REPLACE FUNCTION fn_cash_in_users_games(game_name VARCHAR(50))
RETURNS TABLE(total_cash NUMERIC)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
        SELECT
            temp1.total_cash
        FROM
            (
            SELECT
                round(sum(ug.cash), 2) AS total_cash, ROW_NUMBER() OVER (ORDER BY ug.cash DESC) AS row_num
            FROM
                users_games AS ug
                JOIN games AS g
                ON ug.game_id = g.id
            WHERE
                g.name = game_name
            GROUP BY
                ug.cash
            ) AS temp1
        WHERE
            row_num % 2 <> 0;
END; $$;
