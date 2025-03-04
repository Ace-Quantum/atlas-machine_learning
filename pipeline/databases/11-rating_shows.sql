-- Annnnd now we're downloading the rotten tomatoes database

SELECT title, tv_show_ratings.rate
-- Rating = SUM(tv_show_ratings)
FROM tv_shows;
JOIN tv_show_ratings ON tv_show_ratings.show_id=tv_shows.id;