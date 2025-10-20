CREATE OR REPLACE FUNCTION fn_full_name(first_name VARCHAR(30), last_name VARCHAR(30))
RETURNS VARCHAR
LANGUAGE plpgsql
AS $$
DECLARE full_name VARCHAR;
BEGIN
    IF first_name IS NOT NULL AND last_name IS NOT NULL THEN
        full_name := concat(initcap(first_name), ' ', initcap(last_name));
    ELSIF first_name IS NOT NULL AND last_name IS NULL THEN
        full_name := initcap(first_name);
    ELSIF first_name IS NULL AND last_name IS NOT NULL THEN
        full_name := initcap(last_name);
	END IF;
    RETURN full_name;
END
$$;