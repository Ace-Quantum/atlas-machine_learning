-- Annnnd now we're downloading the rotten tomatoes database

SELECT tv_shows.title, tv_show_ratings.rate
SUM(tv_show_ratings.rate) AS rating
FROM tv_show_ratings
INNER JOIN tv_shows ON tv_show_ratings.show_id=tv_shows.id;