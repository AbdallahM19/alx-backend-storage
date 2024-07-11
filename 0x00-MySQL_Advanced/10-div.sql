-- Write a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score.


DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    IF b != 0 THEN
        RETURN a / b;
    END IF;
    RETURN 0;
END $$
DELIMITER ;
