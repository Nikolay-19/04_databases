SELECT
    b.booking_id AS "Booking ID",
    ap.name AS "Apartment Owner",
    ap.apartment_id AS "Apartment ID",
	concat(cs.first_name, ' ', cs.last_name) AS "Customer Name"
FROM
    apartments AS ap
        FULL JOIN bookings AS b
        ON ap.booking_id = b.booking_id
            FULL JOIN customers AS cs
            ON b.customer_id = cs.customer_id
ORDER BY
    b.booking_id ASC, ap.name ASC, concat(cs.first_name, ' ', cs.last_name) ASC
