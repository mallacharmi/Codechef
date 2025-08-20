-- Last updated: 8/20/2025, 5:42:17 PM
-- User who rated the most movies
(
  SELECT name AS results
  FROM Users u
  JOIN (
    SELECT user_id, COUNT(*) AS rating_count
    FROM MovieRating
    GROUP BY user_id
  ) r ON u.user_id = r.user_id
  ORDER BY rating_count DESC, name
  LIMIT 1
)

UNION ALL

-- Movie with highest average rating in Feb 2020
(
  SELECT title AS results
  FROM Movies m
  JOIN (
    SELECT movie_id, AVG(rating) AS avg_rating
    FROM MovieRating
    WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY movie_id
  ) r ON m.movie_id = r.movie_id
  ORDER BY avg_rating DESC, title
  LIMIT 1
);
