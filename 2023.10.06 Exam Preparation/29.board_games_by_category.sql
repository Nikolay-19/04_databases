SELECT
    board_games.id, board_games.name, board_games.release_year, categories.name AS category_name
FROM
    board_games
    JOIN categories
    ON board_games.category_id = categories.id
WHERE
    categories.name IN ('Strategy Games', 'Wargames')
ORDER BY
    board_games.release_year DESC;
