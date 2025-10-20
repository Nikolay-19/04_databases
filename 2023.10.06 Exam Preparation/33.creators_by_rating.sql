SELECT
    cr.last_name, ceil(avg(bg.rating)) AS average_rating, pb.name AS publisher_name
FROM
    creators_board_games AS cb
    JOIN creators AS cr
    ON cb.creator_id = cr.id
        JOIN board_games AS bg
        ON cb.board_game_id = bg.id
            JOIN publishers AS pb
            ON bg.publisher_id = pb.id
WHERE
    pb.name = 'Stonemaier Games'
GROUP BY
    cr.last_name, pb.name
ORDER BY
    avg(bg.rating) DESC;
