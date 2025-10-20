SELECT
    user_id, age(starts_at, booked_at) AS "Early Birds"
FROM
    bookings
WHERE
    age(starts_at, booked_at) > INTERVAL '10 months'
