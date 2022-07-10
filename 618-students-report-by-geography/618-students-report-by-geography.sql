# Write your MySQL query statement below
select America, Asia, Europe
from
(select name as America, row_number()over(order by name) as rn from student where continent='America') a 
left join
(select name as Asia, row_number()over(order by name) as rn from student where continent='Asia') b using(rn)
left join
(select name as Europe, row_number()over(order by name) as rn from student where continent = 'Europe') c using(rn);