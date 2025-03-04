-- There's yet another rating database

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_show_ratings
JOIN tv_show_genres ON tv_show_genres.show_id=tv_show_ratings.show_id
JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
GROUP BY name;