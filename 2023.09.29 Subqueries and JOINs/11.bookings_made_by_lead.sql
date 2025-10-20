SELECT
    b.apartment_id,
    b.booked_for,
    cs.first_name,
    cs.country
FROM
    bookings AS b
        INNER JOIN customers AS cs
        ON b.customer_id = cs.customer_id
WHERE
    cs.job_type LIKE '%Lead%'
