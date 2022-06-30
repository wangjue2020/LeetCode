# Write your MySQL query statement below
select name, bonus
from employee left join Bonus using(empId)
where bonus is null or bonus<1000;