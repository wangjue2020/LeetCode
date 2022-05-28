# Write your MySQL query statement below
select d.name as "Department", e1.name as "Employee", e1.salary
from Employee e1 left join Department d on e1.departmentId=d.id
    left join 
    (select max(e.salary) as max_salary, e.departmentId
    from Employee e 
    group by e.departmentId
    ) as m on e1.departmentId = m.departmentId
where e1.salary = m.max_salary