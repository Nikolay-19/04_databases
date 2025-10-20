CREATE TABLE logs(
    id SERIAL PRIMARY KEY,
    account_id INTEGER,
    old_sum NUMERIC(20, 4),
    new_sum NUMERIC(20, 4));

CREATE OR REPLACE FUNCTION trigger_fn_insert_new_entry_into_logs()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO logs(account_id, old_sum, new_sum)
    VALUES(old.id, old.balance, new.balance);
	RETURN NEW;
END; $$;

CREATE TRIGGER tr_account_balance_change
    AFTER UPDATE OF balance
    ON ACCOUNTS
    FOR EACH ROW
    WHEN (new.balance <> old.balance)
    EXECUTE FUNCTION
        trigger_fn_insert_new_entry_into_logs();
