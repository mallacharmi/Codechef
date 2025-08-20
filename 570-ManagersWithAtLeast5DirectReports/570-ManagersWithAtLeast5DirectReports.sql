-- Last updated: 8/20/2025, 5:43:14 PM
# Write your MySQL query statement below
SELECT e1.name
FROM Employee e1 JOIN Employee e2 ON e1.id=e2.managerId
GROUP BY e2.managerId
Having Count(e2.managerId)>=5;