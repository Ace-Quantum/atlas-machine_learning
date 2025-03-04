-- There's yet another rating database

SELECT tv_genres.name, tv_show_ratings.rate
FROM tv_show_ratings
JOIN tv_show_genres ON tv_show_genres.show_id=tv_show_ratings.show_id
JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id;