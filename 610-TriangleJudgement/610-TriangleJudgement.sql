-- Last updated: 8/20/2025, 5:43:00 PM
SELECT x, y, z, 
       CASE 
           WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
           ELSE 'No'
       END AS triangle
FROM Triangle;
