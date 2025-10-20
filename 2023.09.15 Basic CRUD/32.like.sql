SELECT
    name, start_date
FROM
    projects
WHERE
    LEFT(name, 5) = 'MOUNT'
ORDER BY
    id ASC
