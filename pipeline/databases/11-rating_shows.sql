-- Annnnd now we're downloading the rotten tomatoes database

SELECT tv_shows.title,
Rating = SUM(tv_show_ratings)
FROM tv_shows
INNER JOIN tv_shows ON tv_show_ratings.show_id=tv_shows.id;