<h3> This tutorial project is based on advanced concepts in MYSQL database. </h3>
<p> Project over - took place from Mar 20, 2024 6:00 AM to Mar 22, 2024 6:00 AM </p>
<p> An auto review will be launched at the deadline</p>
<h4> Learning Objectives </h4>
<ul>
<li>How to create tables with constraints</li>
<li>How to optimize queries by adding indexes</li>
<li>What is and how to implement stored procedures and functions in MySQL</li>
<li>What is and how to implement views in MySQL</li>
<li>What is and how to implement triggers in MySQL</li>
</ul>

<h4> Requirements </h4>
<ul>
<li> All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)</li>
<li> All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (SELECT, WHERE…)</li>
<li> A README.md file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using wc</li>
</ul>
<h4> Resources</h4>
<ul>
<li><a href="https://devhints.io/mysql"> MYSQL CHEATSHEET </a></li>
<li><a href="https://www.liquidweb.com/kb/mysql-optimization-how-to-leverage-mysql-database-indexing/"> https://www.liquidweb.com/kb/mysql-optimization-how-to-leverage-mysql-database-indexing/</a></li>
<li><a href="https://www.w3resource.com/mysql/mysql-procedure.php">Stored Procedure</a></li>
<li><a href="https://www.w3resource.com/mysql/mysql-triggers.php">Triggers</a></li>
<li><a href="https://www.w3resource.com/mysql/mysql-views.php">Views</a></li>
<li><a href="https://dev.mysql.com/doc/refman/5.7/en/functions.html">https://dev.mysql.com/doc/refman/5.7/en/functions.html</a></li>
<li><a href="https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html">Trigger Syntax and Examples</a></li>
<li><a href="https://dev.mysql.com/doc/refman/5.7/en/create-table.html">CREATE TABLE Statement</a></li>
<li><a href="https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html">CREATE PROCEDURE and CREATE FUNCTION Statements</a></li>
<li><a href="https://dev.mysql.com/doc/refman/5.7/en/create-index.html">CREATE INDEX Statement</a></li>
<li><a href="https://dev.mysql.com/doc/refman/5.7/en/create-view.html">CREATE VIEW Statement</a></li>
</ul>

<h4> TASKS </h4>
<ul>
<li>Write a SQL script that creates a table users following these requirements:

With these attributes:
id, integer, never null, auto increment and primary key
email, string (255 characters), never null and unique
name, string (255 characters)
If the table already exists, your script should not fail
Your script can be executed on any database
Context: Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application</li>
<li>Write a SQL script that creates a table users following these requirements:

With these attributes:
id, integer, never null, auto increment and primary key
email, string (255 characters), never null and unique
name, string (255 characters)
country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
If the table already exists, your script should not fail
Your script can be executed on any database</li>
<li>Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

Requirements:

Import this table dump: metal_bands.sql.zip
Column names must be: origin and nb_fans
Your script can be executed on any database
Context: Calculate/compute something is always power intensive… better to distribute the load!</li>
<li>Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

Requirements:

Import this table dump: metal_bands.sql.zip
Column names must be: band_name and lifespan (in years until 2022 - please use 2022 instead of YEAR(CURDATE()))
You should use attributes formed and split for computing the lifespan
Your script can be executed on any database</li>
<li>Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table items can be negative.

Context: Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!</li>
<li>Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

Context: Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!</li>
<li>Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

Requirements:

Procedure AddBonus is taking 3 inputs (in this order):
user_id, a users.id value (you can assume user_id is linked to an existing users)
project_name, a new or already exists projects - if no projects.name found in the table, you should create it
score, the score value for the correction
Context: Write code in SQL is a nice level up!</li>
<li>Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

Requirements:

Procedure ComputeAverageScoreForUser is taking 1 input:
user_id, a users.id value (you can assume user_id is linked to an existing users)</li>
<li>Write a SQL script that creates an index idx_name_first on the table names and the first letter of name.

Requirements:

Import this table dump: names.sql.zip
Only the first letter of name must be indexed</li>
<li>Write a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score.

Requirements:

Import this table dump: names.sql.zip
Only the first letter of name AND score must be indexed</li>
<li>Write a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

Requirements:

You must create a function
The function SafeDiv takes 2 arguments:
a, INT
b, INT
And returns a / b or 0 if b == 0</li>
<li>Write a SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.

Requirements:

The view need_meeting should return all students name when:
They score are under (strict) to 80
AND no last_meeting date OR more than a month</li>
<li>Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

Requirements:

Procedure ComputeAverageScoreForUser is taking 1 input:
user_id, a users.id value (you can assume user_id is linked to an existing users)</li>
<li>Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.

Requirements:

Procedure ComputeAverageWeightedScoreForUsers is not taking any input.
Tips:

Calculate-Weighted-Average</li>
<li>
</ul>
