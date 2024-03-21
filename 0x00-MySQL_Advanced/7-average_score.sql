-- SQL script that creates a stored procedure ComputeAverageScoreForUser.
-- The procedure computes and store the average score for a student.
-- An average score can be a decimal

-- First change the DELIMITER

DELIMITER // ;

CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	DECLARE average FLOAT;
	-- Obtain the average score of a particular user from corrections table
	SET average = (SELECT AVG(score) AS average_score FROM corrections WHERE user_id = user_id);
	UPDATE users
	SET average_score = average
	WHERE id = user_id;
END; //

-- Revert DELIMITER

DELIMITER ; //
