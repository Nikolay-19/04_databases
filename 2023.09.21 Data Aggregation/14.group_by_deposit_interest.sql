SELECT
   deposit_group, sum(deposit_interest) AS "Deposit Interest"
FROM
    wizard_deposits
GROUP BY
    deposit_group
ORDER BY
    sum(deposit_interest) DESC
