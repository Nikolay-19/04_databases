SELECT
    cr.id, cr.make, cr.mileage, count(co.id) AS count_of_courses, round(avg(co.bill), 2) AS average_bill
FROM
    cars AS cr
    LEFT JOIN courses AS co
    ON cr.id = co.car_id
GROUP BY
    cr.id
HAVING
    count(co.id) <> 2
ORDER BY
    count_of_courses DESC, cr.id ASC;
