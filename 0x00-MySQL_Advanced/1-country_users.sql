-- An SQL script that creates a new table called users

-- Creating a new table based on the following requirements
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- If the table already exists, your script should not fail
-- country, enumeration of countries: US, CO and TN

-- Drop the table if it already exist and create a new one

DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
	id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
	);
