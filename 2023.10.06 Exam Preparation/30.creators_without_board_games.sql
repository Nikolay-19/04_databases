SELECT
    creators.id, concat(creators.first_name, ' ', creators.last_name), creators.email
FROM
    creators
    LEFT JOIN creators_board_games
    ON creators.id = creators_board_games.creator_id
        LEFT JOIN board_games
        ON board_games.id = creators_board_games.board_game_id
WHERE
    creators_board_games.creator_id IS NULL AND
    creators_board_games.board_game_id IS NULL;
