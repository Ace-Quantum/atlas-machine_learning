-- Annnnd now we're downloading the rotten tomatoes database

SELECT tv_shows.title, tv_show_ratings.rate
FROM tv_show_ratings
INNER JOIN tv_shows ON tv_show_ratings.show_id=tv_shows.id;