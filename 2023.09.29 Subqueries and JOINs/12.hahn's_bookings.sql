SELECT
    count(*)
FROM
    bookings AS b
        JOIN customers AS cs
        ON b.customer_id = cs.customer_id
WHERE
    cs.last_name = 'Hahn'
