# Write your MySQL query statement below
with tmp as 
(select id, visit_date, people, id-row_number()over(order by id) as tag
from stadium
where people >= 100)

select id, visit_date, people
from tmp
where tag in (select tag
from  tmp
group by tag
having count(*)>=3)
order by visit_date asc;