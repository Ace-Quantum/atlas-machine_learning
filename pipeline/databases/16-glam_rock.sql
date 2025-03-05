-- pull all bands considered glam rock and organize them

SELECT band_name
-- CASE
-- WHEN split IS NULL THEN 2020 - formed
-- ELSE split - formed
-- END AS `lifespan until 2020 (in years)`
FROM metal_bands
WHERE style = '%Glam rock%'
-- ORDER BY `lifespan until 2020 (in years)` DESC; 