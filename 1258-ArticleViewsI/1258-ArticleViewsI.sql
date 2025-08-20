-- Last updated: 8/20/2025, 5:42:31 PM
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id;
