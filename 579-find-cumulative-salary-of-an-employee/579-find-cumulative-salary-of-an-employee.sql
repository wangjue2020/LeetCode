# Write your MySQL query statement below
with most_recent as (select id, max(month) as month from employee group by id)
select e.id, e.month, sum(e1.salary) as salary
from employee e left join employee e1 on e.id = e1.id and e.month >= e1.month left join most_recent m on e.id = m.id 
where abs(e1.month - e.month) between 0 and 2 and e.month <>m.month
group by e.id, e.month
order by e.id , e.month desc