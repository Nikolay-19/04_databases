CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS(SELECT id FROM employees WHERE id = employee_id) THEN
        UPDATE employees
        SET salary = salary * 1.05
        WHERE id = employee_id;
        COMMIT;
    ELSE
        ROLLBACK;
    END IF;
END;
$$;
