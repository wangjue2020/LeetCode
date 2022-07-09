# Write your MySQL query statement below
select  department.name as Department,tmp.name as Employee, Salary from
(select id, name, salary, departmentId, dense_rank() over(partition by departmentId order by salary desc) as ra 
from Employee ) tmp join department on tmp.departmentId = department.id
where ra <= 3;