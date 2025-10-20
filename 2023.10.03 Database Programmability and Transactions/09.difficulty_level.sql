CREATE OR REPLACE FUNCTION fn_difficulty_level("level" INTEGER)
RETURNS VARCHAR(30)
LANGUAGE plpgsql
AS $$
DECLARE difficulty VARCHAR(30);
BEGIN
    IF "level" <= 40 THEN
        difficulty := 'Normal Difficulty';
    ELSIF "level" <= 60 THEN
        difficulty := 'Nightmare Difficulty';
	ELSIF "level" >= 61 THEN 
        difficulty := 'Hell Difficulty';
	END IF;
	RETURN difficulty;
END; $$;
