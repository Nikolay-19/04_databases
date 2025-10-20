SELECT
    country_code,
    count(*) AS mountain_range_count
FROM
    mountains_countries AS mc
        JOIN mountains AS m
        ON mc.mountain_id = m.id
WHERE
    mc.country_code in ('BG', 'US', 'RU')
GROUP BY
    country_code
ORDER BY
    mountain_range_count DESC
