CREATE OR REPLACE FUNCTION fn_courses_by_client(phone_num VARCHAR(20))
RETURNS BIGINT
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN
        (SELECT
            count(*)
        FROM
            courses
            JOIN clients
            ON courses.client_id = clients.id
        WHERE
            clients.phone_number = phone_num);
END; $$;
