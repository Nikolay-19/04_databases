CREATE VIEW view_initials AS
SELECT
    left(first_name, 2) AS "initial", last_name
FROM
    employees
ORDER BY
    last_name ASC
