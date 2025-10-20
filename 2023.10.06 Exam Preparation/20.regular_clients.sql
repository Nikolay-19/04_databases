SELECT
    clients.full_name, count(DISTINCT courses.car_id) AS count_of_cars, sum(courses.bill) AS total_sum
FROM
    clients
    JOIN courses
    ON clients.id = courses.client_id
WHERE
    substring(clients.full_name, 2, 1) = 'a'
GROUP BY
    clients.full_name
HAVING
    count(DISTINCT courses.car_id) > 1
ORDER BY
    clients.full_name
