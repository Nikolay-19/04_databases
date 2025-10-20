CREATE TABLE notification_emails(
    id SERIAL PRIMARY KEY,
    recipient_id INT,
    subject VARCHAR(50),
    body TEXT);


CREATE OR REPLACE FUNCTION trigger_fn_send_email_on_balance_change()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO notification_emails(recipient_id, subject, body)
    VALUES(
        old.id,
        'Balance change for account: %', old.id,
        'On % your balance was changed from % to %.', CURRENT_DATE, old.old_sum, new.new_sum);
    RETURN NULL;
END; $$;


CREATE TRIGGER tr_send_email_on_balance_change
    AFTER UPDATE
    ON logs
    FOR EACH ROW
    WHEN (old.old_sum <> new.new_sum)
    EXECUTE FUNCTION
        trigger_fn_send_email_on_balance_change();
