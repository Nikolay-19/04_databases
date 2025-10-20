SELECT
    v.name, v.phone_number, v.address, v.animal_id, v.department_id
FROM
    volunteers AS v
    LEFT JOIN animals AS an
    ON v.animal_id = an.id
        LEFT JOIN volunteers_departments AS vd
        ON v.department_id = vd.id
ORDER BY
    v.name ASC, an.id ASC, vd.id ASC
