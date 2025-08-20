-- Last updated: 8/20/2025, 5:42:15 PM
# Write your MySQL query statement below
SELECT eu.unique_id,e.name
FROM Employees e LEFT JOIN EmployeeUNI eu ON e.id=eu.id;