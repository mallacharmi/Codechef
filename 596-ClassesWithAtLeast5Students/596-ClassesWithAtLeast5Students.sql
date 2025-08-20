-- Last updated: 8/20/2025, 5:43:03 PM
# Write your MySQL query statement below
SELECT class
FROM Courses
GROUP BY class
Having COUNT(class)>=5
