-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.


DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE total_weighted_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
    DECLARE average_weighted_score FLOAT DEFAULT 0;

    CREATE TEMPORARY TABLE tmp_user_ids AS SELECT id FROM users;

    WHILE (SELECT COUNT(*) FROM tmp_user_ids) > 0 DO
        -- Get the first user ID from the temporary table
        SELECT id INTO user_id FROM tmp_user_ids LIMIT 1;

        -- print all id
        SELECT "--";
        SELECT * FROM tmp_user_ids;
        SELECt id FROM tmp_user_ids;
	SELECT user_id;
	SELECT "--";

        -- Calculate the total weighted score and total weight for the current user
        SELECT SUM(c.score * p.weight), SUM(p.weight)
        INTO total_weighted_score, total_weight
        FROM corrections AS c
        JOIN projects AS p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Calculate the average weighted score
        IF total_weight != 0 THEN
            SET average_weighted_score = total_weighted_score / total_weight;
        ELSE
            SET average_weighted_score = 0;
        END IF;

        -- Update the user's average score
        UPDATE users SET average_score = average_weighted_score
        WHERE id = user_id;

        -- Remove the processed user ID from the temporary table
        DELETE FROM tmp_user_ids WHERE id = user_id;
    END WHILE;

    -- Drop the temporary table
    DROP TEMPORARY TABLE tmp_user_ids;
END $$

DELIMITER ;

-- output
-- id      name    average_score
-- 1       Bob     90.6667
-- 2       Jeanne  79
-- id      name    weight
-- 1       C is fun        1
-- 2       Python is cool  2
-- user_id project_id      score
-- 1       1       80
-- 1       2       96
-- 2       1       91
-- 2       2       73
-- --
-- --
-- id
-- 1
-- 2
-- id
-- 1
-- 2
-- user_id
-- 1
-- --
-- --
-- --
-- --
-- id
-- 2
-- id
-- 2
-- user_id
-- 2
-- --
-- --
-- --
-- --
-- id      name    average_score
-- 1       Bob     90.6667
-- 2       Jeanne  79
