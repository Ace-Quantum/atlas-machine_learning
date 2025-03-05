-- pull all bands considered glam rock and organize them

SELECT band_name, formed - split AS lifespan

FROM metal_bands;
WHERE style = '%Glam rock%';
ORDER BY lifespan DESC; 