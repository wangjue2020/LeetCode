# Write your MySQL query statement below
with valid_salary as 
(select salary from employees group by salary having count(salary)>1)

select employee_id, name, salary, dense_rank()over(order by salary asc) as team_id from employees join valid_salary using(salary) order by team_id asc, employee_id asc;