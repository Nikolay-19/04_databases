SELECT
    population,
	length(cast(population AS VARCHAR)) AS "length"
FROM
    countries
