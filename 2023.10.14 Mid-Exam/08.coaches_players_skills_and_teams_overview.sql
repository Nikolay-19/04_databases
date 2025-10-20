SELECT
    concat(cc.first_name, ' ', cc.last_name) AS coach_full_name, concat(pl.first_name, ' ', pl.last_name) AS player_full_name,
    tm.name, sd.passing, sd.shooting, sd.speed
FROM
    coaches AS cc
    JOIN players_coaches AS pc
    ON cc.id = pc.coach_id
        JOIN players AS pl
        ON pl.id = pc.player_id
            JOIN skills_data AS sd
            ON sd.id = pl.skills_data_id
                JOIN teams AS tm
                ON tm.id = pl.team_id
ORDER BY
    concat(cc.first_name, ' ', cc.last_name) ASC,
    concat(pl.first_name, ' ', pl.last_name) DESC;
