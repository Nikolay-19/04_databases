SELECT
    towns.town_id, towns.name as town_name, addresses.address_text
FROM towns
    JOIN addresses
        ON towns.town_id = addresses.town_id
WHERE
    towns.name IN ('San Francisco', 'Sofia', 'Carnation')
ORDER BY
    town_id ASC, address_id ASC
