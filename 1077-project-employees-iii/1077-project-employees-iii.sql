# Write your MySQL query statement below
select project_id, employee_id
from project left join employee using(employee_id) join
(select project_id, max(experience_years) as max_years
from project p left join employee e using(employee_id)
group by project_id) tmp using (project_id)
where experience_years = max_years
