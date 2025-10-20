SELECT
    CASE
        WHEN age BETWEEN 0 and 10 THEN '[0-10]'
        WHEN age BETWEEN 11 and 20 THEN '[11-20]'
        WHEN age BETWEEN 21 and 30 THEN '[21-30]'
        WHEN age BETWEEN 31 and 40 THEN '[31-40]'
        WHEN age BETWEEN 41 and 50 THEN '[41-50]'
        WHEN age BETWEEN 51 and 60 THEN '[51-60]'
        WHEN age >= 61 THEN '[61+]'
    END AS "Age Group",
	COUNT(*)
FROM
    wizard_deposits
GROUP BY
    "Age Group"
ORDER BY
    "Age Group" ASC
    