-- Not a fan of how much they're making us download.

SELECT metal_bands.origin, SUM(metal_bands.fans) as nb_fans
FROM metal_bands
GROUP BY origin;