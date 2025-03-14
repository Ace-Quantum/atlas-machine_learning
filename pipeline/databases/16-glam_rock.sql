-- pull all bands considered glam rock and organize them

SELECT band_name,
  CASE
    WHEN `split` IS NULL THEN 2020
    WHEN split < 2020 THEN split
    ELSE 2020
  END
    - formed
  AS lifespan

FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC; 