-- Last updated: 8/20/2025, 5:42:57 PM
# Write your MySQL query statement below
WITH CTE AS(SELECT requester_id FROM RequestAccepted UNION ALL SELECT accepter_id FROM RequestAccepted)
SELECT requester_id AS id,COUNT(*) AS num FROM CTE GROUP BY requester_id ORDER BY num DESC LIMIT 1;