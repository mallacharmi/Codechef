-- Last updated: 8/20/2025, 5:42:34 PM
# Write your MySQL query statement below
WITH FirstLogin AS (
    SELECT player_id, MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(
    COUNT(DISTINCT A.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity),
    2
) AS fraction
FROM Activity A
JOIN FirstLogin F ON A.player_id = F.player_id
WHERE A.event_date = DATE_ADD(F.first_login_date, INTERVAL 1 DAY);
