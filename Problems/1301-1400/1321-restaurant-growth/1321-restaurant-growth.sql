# Write your MySQL query statement below
with tmp as
(select visited_on, sum(amount) as amount
from Customer
group by visited_on)

select t1.visited_on, sum(t2.amount) as amount, round(sum(t2.amount) / count(*), 2) as average_amount
from tmp t1, tmp t2
where datediff(t1.visited_on,t2.visited_on) between 0 and 6
group by t1.visited_on
having count(*) >=7
order by t1.visited_on
