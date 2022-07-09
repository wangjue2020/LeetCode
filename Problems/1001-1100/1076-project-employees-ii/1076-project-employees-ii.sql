# Write your MySQL query statement below
select project_id from project group by project_id having count(distinct employee_id) = 
(select count(employee_id) as cnt
from project
group by project_id
order by cnt desc limit 1)