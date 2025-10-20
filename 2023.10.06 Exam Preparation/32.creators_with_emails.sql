SELECT
    concat(cr.first_name, ' ', cr.last_name) AS full_name, cr.email, max(bg.rating)
FROM
    creators_board_games AS cb
    JOIN creators AS cr
    ON cb.creator_id = cr.id
        JOIN board_games AS bg
        ON cb.board_game_id = bg.id
WHERE
    right(cr.email, 4) = '.com'
GROUP BY
    concat(cr.first_name, ' ', cr.last_name), cr.email
ORDER BY
    concat(cr.first_name, ' ', cr.last_name) ASC;
