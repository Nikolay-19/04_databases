SELECT
    ap.name,
	sum(b.booked_for)
FROM
    apartments AS ap
        JOIN bookings AS b
        ON ap.apartment_id = b.apartment_id
GROUP BY
    ap.name
ORDER BY
    ap.name ASC
