-- Last updated: 8/20/2025, 5:43:37 PM
# Write your MySQL query statement below
SELECT p.firstname AS firstname,p.lastname AS lastname,a.city AS city,a.state AS state
FROM Person p LEFT OUTER JOIN Address a ON p.personId=a.personId;