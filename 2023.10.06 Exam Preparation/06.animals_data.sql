SELECT
    an.name, ant.animal_type, to_char(an.birthdate, 'DD.MM.YYYY')
FROM
    animals AS an
    LEFT JOIN animal_types AS ant
    ON an.animal_type_id = ant.id
ORDER BY
    an.name ASC
