-- Last updated: 8/20/2025, 5:43:21 PM
DELETE FROM Person
WHERE id NOT IN (
    SELECT id FROM (
        SELECT MIN(id) AS id FROM Person GROUP BY email
    ) AS temp
);
