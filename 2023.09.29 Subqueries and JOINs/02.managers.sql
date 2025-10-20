SELECT
    employees.employee_id, concat(employees.first_name, ' ', employees.last_name) AS full_name, departments.department_id, departments.name
FROM
    employees
        JOIN departments
        ON employees.employee_id = departments.manager_id
ORDER BY
    employees.employee_id ASC
LIMIT 5;
