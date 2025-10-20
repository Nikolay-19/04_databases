SELECT
    o.name, count(*) AS "Count of animals"
FROM
    animals AS an
    JOIN owners AS o
    ON an.owner_id = o.id
GROUP BY
    o.name
ORDER BY
    "Count of animals" DESC, o.name ASC
LIMIT 5
