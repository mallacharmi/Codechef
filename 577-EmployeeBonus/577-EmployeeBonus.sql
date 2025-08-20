-- Last updated: 8/20/2025, 5:43:10 PM
# Write your MySQL query statement below
SELECT e.name,b.bonus
FROM Employee e LEFT JOIN Bonus b ON e.empId=b.empId
where b.bonus <1000 or b.bonus IS NULL;