CREATE VIEW view_addresses AS
SELECT
    concat(first_name, ' ', last_name) AS "Full Name", department_id, concat(number, ' ', street) AS "Address"
FROM
    employees AS emp
JOIN 
    addresses AS adr
	ON
    emp.address_id = adr.id
ORDER BY
    "Address" ASC
