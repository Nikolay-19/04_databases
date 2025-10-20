CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(searched_balance NUMERIC)
LANGUAGE plpgsql
AS $$
DECLARE
    holder_info RECORD;
BEGIN
    FOR holder_info IN
        SELECT
            concat(first_name, ' ', last_name) AS full_name, sum(balance) AS total_balance
        FROM
            account_holders AS ah
        JOIN accounts AS ac
        ON ah.id = ac.account_holder_id
        GROUP BY
            full_name
        HAVING
            sum(balance) > searched_balance
        ORDER BY
            full_name ASC
    LOOP
        RAISE NOTICE '% - %', holder_info.full_name, holder_info.total_balance;
    END LOOP;
END; $$;
