SELECT
    board_games.name, board_games.rating, categories.name
FROM
    board_games
    JOIN players_ranges
    ON board_games.players_range_id = players_ranges.id
        JOIN categories
        ON board_games.category_id = categories.id
WHERE
    (board_games.rating > 7 AND
    (board_games.name LIKE '%a%' OR board_games.name LIKE '%A%')) OR
    (board_games.rating > 7.5 AND
    (min_players + max_players) BETWEEN 2 AND 5)
ORDER BY
    board_games.name ASC, board_games.rating DESC
LIMIT 5;
