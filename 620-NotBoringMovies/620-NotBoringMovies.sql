-- Last updated: 8/20/2025, 5:42:52 PM
# Write your MySQL query statement below
SELECT id,movie,description,rating
FROM Cinema
WHERE description!='boring' AND id%2=1
ORDER BY rating DESC
