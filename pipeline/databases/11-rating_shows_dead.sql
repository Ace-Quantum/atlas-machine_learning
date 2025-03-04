-- Annnnd now we're downloading the rotten tomatoes database

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_show_ratings
GROUP BY tv_shows.title
INNER JOIN tv_show_ratings ON tv_show_ratings.show_id=tv_shows.id;