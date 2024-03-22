-- SQL script that creates a stored procedure ComputeAverageScoreForUser.
-- The procedure computes and store the average score for a student.
-- An average score can be a decimal

-- First change the DELIMITER

DELIMITER // ;

CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	DECLARE average FLOAT;
	DECLARE total_score INT;
	DECLARE total_project INT;
	-- Obtain the total score of a particular student.
	SET total_score = (SELECT SUM(score) FROM corrections WHERE user_id = user_id);
	-- Obtain the total number of project of a particular student.
	SET total_project =(SELECT DISTINCT COUNT(project_id) FROM corrections WHERE user_id = user_id);
	SET average = IF(total_project > 0, total_score / total_project, 0);
	UPDATE users
	SET average_score = average
	WHERE id = user_id;
END; //

-- Revert DELIMITER

DELIMITER ; //
