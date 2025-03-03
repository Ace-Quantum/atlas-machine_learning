-- And I'm not going to be able to

SELECT city, MAX(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY city ASC;