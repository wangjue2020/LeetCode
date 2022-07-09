# Write your MySQL query statement below
with a as
(select gender, day, sum(score_points) as total
from scores
group by day, gender
order by gender asc, day asc)

# select * from a a1, a a2 where a1.gender = a2.gender and a1.day <= a2.day  order by a1.gender asc, a1.day asc;
select a1.gender, a1.day, sum(a2.total) as total from a a1, a a2 where a1.gender = a2.gender and a1.day >= a2.day group by a1.day, a1.gender order by gender asc, day asc;