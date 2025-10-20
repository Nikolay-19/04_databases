SELECT
    concat(o.name, ' - ', an.name) AS "Owners - Animals", o.phone_number, ac.cage_id AS "Cage ID"
FROM
    animals AS an
    JOIN owners AS o
    ON an.owner_id = o.id
        JOIN animals_cages AS ac
        ON ac.animal_id = an.id
            JOIN animal_types AS ant
            ON ant.id = an.animal_type_id
WHERE
    ant.animal_type = 'Mammals'
ORDER BY
    o.name ASC, an.name DESC;
