-- SQL script that creates a function SafeDiv that divides (and returns) the first by the second number

-- The function SafeDiv takes 2 arguments (a, b)

-- It returns a / b or 0 if b == 0

-- Change DELIMITER
DELIMITER // ;

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
	DECLARE result FLOAT;
	SET result = IF(b = 0, 0, a / b);
	RETURN result;
END; //

-- Revert DELIMITER

DELIMITER ; //
