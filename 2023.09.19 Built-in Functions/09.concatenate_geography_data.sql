CREATE VIEW "view_continents_countries_currencies_details" AS
SELECT
    concat(trim(continents.continent_name), ': ', continents.continent_code) AS "Continent Details",
	concat(countries.country_name, ' - ', countries.capital, ' - ', countries.area_in_sq_km, ' - km2') AS "Country Information",
	concat(currencies.description, ' (', currencies.currency_code, ')') AS "Currencies"
FROM
    continents, countries, currencies
WHERE
    continents.continent_code = countries.continent_code AND
	countries.currency_code = currencies.currency_code
ORDER BY
    "Country Information" ASC,
	"Currencies" ASC
