-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.


DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_score INT DEFAULT 0;

    SELECT AVG(score) INTO total_score
    FROM corrections WHERE corrections.user_id = user_id;

    UPDATE users SET average_score = total_score
    WHERE id = user_id;
END $$

DELIMITER ;
