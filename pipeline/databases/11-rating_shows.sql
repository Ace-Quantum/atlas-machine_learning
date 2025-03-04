-- Annnnd now we're downloading the rotten tomatoes database

SELECT tv_shows.title, tv_show_ratings.rate
-- Rating = SUM(tv_show_ratings)
FROM tv_show_ratings;
JOIN tv_show_ratings ON tv_shows.id=tv_show_ratings.show_id;