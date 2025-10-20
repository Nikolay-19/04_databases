SELECT
    d.first_name, d.last_name, cr.make, cr.model, cr.mileage
FROM
    drivers AS d
    JOIN cars_drivers AS cd
    ON d.id = cd.driver_id
        JOIN cars AS cr
        ON cr.id = cd.car_id
WHERE
    mileage IS NOT NULL
ORDER BY
    mileage DESC, d.first_name ASC;
