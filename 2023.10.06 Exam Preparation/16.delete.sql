DELETE FROM
    clients
WHERE NOT EXISTS
    (SELECT
        NULL
    FROM
        courses
    WHERE
        clients.id = courses.client_id);
