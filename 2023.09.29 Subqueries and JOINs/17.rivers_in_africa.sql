SELECT
    c.country_name,
    r.river_name
FROM
    countries_rivers AS cv
        RIGHT JOIN rivers AS r
        ON cv.river_id = r.id
            RIGHT JOIN countries AS c
            ON cv.country_code = c.country_code
WHERE
    c.continent_code = 'AF'
ORDER BY
    c.country_name ASC
LIMIT 5;
