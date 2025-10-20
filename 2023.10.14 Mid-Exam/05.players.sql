SELECT
    concat(first_name, ' ', last_name) AS full_name, age, hire_date
FROM
    players
WHERE
    substring(first_name, 1, 1) = 'M'
ORDER BY
    age DESC, concat(first_name, ' ', last_name) ASC;
