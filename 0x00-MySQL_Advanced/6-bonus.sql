-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

-- Procedure AddBonus is taking 3 inputs (in this order
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
-- project_name, a new or already exists projects - if no projects.name found in the table, you should create it
-- score, the score value for the correction

-- Change delimiter first to //
DELIMITER // ;


CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
	DECLARE project_id INT;
	-- Check if project_id exist if not create a new project record to obtain id
	SELECT id FROM projects WHERE name = project_name INTO project_id ;
	IF project_id IS NULL
	THEN INSERT INTO projects(name) VALUES(project_name);
	END IF;
	SELECT id FROM projects WHERE name = project_name INTO project_id ;
	-- Add new correction in corrections table
	INSERT INTO corrections(user_id,  project_id, score) VALUES(user_id, project_id, score);
END; //

-- Revert the delimiter
DELIMITER ; //
