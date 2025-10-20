SELECT
    b.booking_id,
    b.apartment_id,
    cs.companion_full_name
FROM
    bookings AS b
        JOIN customers AS cs
        ON b.customer_id = cs.customer_id
WHERE
    b.apartment_id IS NULL
