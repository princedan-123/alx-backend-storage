-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
-- it takes user_id, a users.id value (you can assume user_id is linked to an existing users)

-- Briefly changing DELIMITER
DELIMITER // ;

-- Creating Procedure

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE total_score INT;
	DECLARE total_weight INT;
	SELECT SUM(corrections.score * projects.weight) INTO total_score
	FROM corrections
	INNER JOIN projects
	ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;
	SELECT SUM(projects.weight) INTO total_weight FROM projects INNER JOIN corrections
	ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;
	UPDATE users
	SET average_score = IF(total_weight > 0, total_score / total_weight, 0);
END; //

-- Revert DELIMITER
DELIMITER ; //
