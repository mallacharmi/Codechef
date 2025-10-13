-- Last updated: 10/13/2025, 5:14:14 PM
# Write your MySQL query statement below
select u.name,sum(t.amount) as balance
from Users u join Transactions t on u.account=t.account
group by t.account
having sum(amount)>10000;
