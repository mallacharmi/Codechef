-- Last updated: 8/20/2025, 5:42:37 PM
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
