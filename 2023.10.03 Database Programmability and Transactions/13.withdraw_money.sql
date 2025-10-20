CREATE OR REPLACE PROCEDURE sp_withdraw_money(account_id INT, money_amount NUMERIC(4))
LANGUAGE plpgsql
AS $$
DECLARE temp_balance NUMERIC(19, 4);
BEGIN
    temp_balance := (SELECT balance FROM accounts WHERE accounts.id = account_id);
    IF temp_balance - money_amount < 0 THEN
        RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
		ROLLBACK;
    ELSE
        UPDATE accounts SET balance = balance - money_amount WHERE accounts.id = account_id;
        COMMIT;
    END IF;
END; $$;
