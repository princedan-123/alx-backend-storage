-- SQL script that lists all bands with Glam rock as their main style.
-- The result is ranked by their longevity
-- Column names must be: band_name and lifespan (in years until 2022
-- please use 2022 insteadof YEAR(CURDATE()))
-- You should use attributes formed and split for computing the lifespan

SELECT band_name,
CASE
	WHEN split IS NULL THEN 2022 - formed
	ELSE split - formed
END AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC
