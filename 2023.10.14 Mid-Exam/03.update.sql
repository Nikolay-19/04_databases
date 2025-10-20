UPDATE
    coaches
SET
    salary = salary * coach_level
WHERE EXISTS
    (SELECT
        *
    FROM
        coaches
        JOIN players_coaches
        ON coaches.id = players_coaches.coach_id
    WHERE
        substring(first_name, 1, 1) = 'C');
