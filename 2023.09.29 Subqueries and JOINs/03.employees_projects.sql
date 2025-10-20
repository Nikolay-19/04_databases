SELECT
    ep.employee_id, concat(e.first_name, ' ', e.last_name) AS full_name, ep.project_id, p.name
FROM
    employees_projects AS ep
        JOIN projects AS p
        ON ep.project_id = p.project_id
            JOIN employees AS e
            ON e.employee_id = ep.employee_id
WHERE
    ep.project_id = 1
