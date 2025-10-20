SELECT
    number, street
FROM
    addresses
WHERE
    (id >= 50 and id <= 100) OR number < 1000
