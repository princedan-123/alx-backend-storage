-- SQL script that creates a table users

-- Creating a table called users with the following attributes.
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- If the table already exists, your script should not fail

CREATE TABLE IF NOT EXISTS users (
	id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
	);
