SELECT
    b.booking_id AS "Booking ID",
    DATE(b.starts_at) AS "Start Date",
    b.apartment_id AS "Apartment ID",
    concat(cs.first_name, ' ', cs.last_name) AS "Customer Name"
FROM
    bookings AS b
        RIGHT JOIN customers AS cs
        ON b.customer_id = cs.customer_id
ORDER BY
    "Customer Name" ASC
LIMIT 10
