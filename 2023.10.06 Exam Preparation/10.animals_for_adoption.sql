SELECT
    an.name AS "Animal Name", EXTRACT(YEAR FROM an.birthdate) AS "Birth Year", ant.animal_type
FROM
    animals AS an
    JOIN animal_types AS ant
    ON ant.id = an.animal_type_id
WHERE
    ant.animal_type <> 'Birds' AND an.owner_id IS NULL AND age('01/01/2022', an.birthdate) < '5 years'
ORDER BY
    an.name ASC;
