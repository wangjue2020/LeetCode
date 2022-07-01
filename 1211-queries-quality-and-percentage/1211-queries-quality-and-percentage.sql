# Write your MySQL query statement below
# select query_name, avg(rating/position) as quality, 
select query_name, round(avg(rating/position) ,2) as quality, round((sum(less) / count(less))*100,2) as poor_query_percentage
from (select *, case when rating < 3 then 1 else 0 end as less from queries) tmp
group by query_name