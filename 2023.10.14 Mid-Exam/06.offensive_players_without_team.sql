SELECT
    players.id, concat(players.first_name, ' ', players.last_name), players.age, players.position, players.salary,
    skills_data.pace, skills_data.shooting
FROM
    players
    JOIN skills_data
    ON players.skills_data_id = skills_data.id
WHERE
    team_id IS NULL AND
    "position" = 'A' AND
    (skills_data.pace + skills_data.shooting) > 130;
