# Write your MySQL query statement below
select employee_id, team_size
from employee left join (select team_id, count(employee_id) as team_size from employee group by team_id) t on employee.team_id = t.team_id;