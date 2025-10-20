CREATE OR REPLACE PROCEDURE sp_players_team_name(IN player_name VARCHAR(50), OUT team_name VARCHAR(45))
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT
        teams.name
    INTO
        team_name
    FROM
        players
        JOIN teams
        ON players.team_id = teams.id
    WHERE
        concat(players.first_name, ' ', players.last_name) = player_name;
    IF team_name IS NULL THEN
        SELECT 'The player currently has no team' INTO team_name;
    END IF;
END; $$;
