CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(animal_name VARCHAR(30), OUT owner_name VARCHAR(50))
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT
        o.name
    FROM
        animals AS an
        JOIN owners AS o
        ON an.owner_id = o.id
    WHERE
        an.name = animal_name
	INTO
        owner_name;
    IF owner_name IS NULL THEN
        owner_name := 'For adoption';
    END IF;
    RETURN;
END; $$;
