-- SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

-- Briefly change DELIMITER

DELIMITER // ;

CREATE TRIGGER validate_email BEFORE UPDATE
FOR EACH ROW
	BEGIN
		IF NEW.name != OLD.name THEN SET NEW.valid_email = 0;
		END IF;
	END; //
-- Revert DELIMITER

DELIMITER ; //
