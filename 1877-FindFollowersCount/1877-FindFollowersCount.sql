-- Last updated: 8/20/2025, 5:42:04 PM
SELECT user_id, COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;
