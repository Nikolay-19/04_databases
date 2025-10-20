SELECT
    mc.country_code,
    m.mountain_range,
    p.peak_name,
    p.elevation
FROM
    mountains_countries as mc
        JOIN mountains as m
        ON mc.mountain_id = m.id
            JOIN peaks as p
            ON p.mountain_id = m.id
WHERE
    mc.country_code = 'BG' AND
    p.elevation > 2835
ORDER BY
    p.elevation DESC;
