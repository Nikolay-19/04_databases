SELECT
    teams.id, teams.name, count(players.id) AS player_count, teams.fan_base
FROM
    teams
    LEFT JOIN players
    ON teams.id = players.team_id
WHERE
    teams.fan_base > 30000
GROUP BY
    teams.id, teams.name
ORDER BY
    count(players.id) DESC, teams.fan_base DESC;
