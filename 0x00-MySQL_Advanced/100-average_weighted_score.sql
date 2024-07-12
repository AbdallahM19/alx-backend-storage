-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.


DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
    DECLARE average_weighted_score FLOAT DEFAULT 0;

    -- Calculate the total weighted score and total weight
    SELECT SUM(c.score * p.weight), SUM(p.weight)
    INTO total_weighted_score, total_weight
    FROM corrections AS c
    JOIN projects AS p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculate the average weighted score
    SET average_weighted_score = total_weighted_score / total_weight;

    -- Update the user's average score
    UPDATE users SET average_score = average_weighted_score
    WHERE id = user_id;
END $$

DELIMITER ;
