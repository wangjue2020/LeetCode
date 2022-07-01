# Write your MySQL query statement below
select q1.person_name
from queue q1, queue q2 where q2.turn <= q1.turn
group by q1.turn
having sum(q2.weight)<=1000
order by sum(q2.weight) desc limit 1