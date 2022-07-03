# Write your MySQL query statement below
with 
cnt as (select activity, count(activity) as cnt from friends group by activity),
max_cnt as (select max(cnt) as maxc from cnt),
min_cnt as (select min(cnt) as minc from cnt)
select activity
from cnt left join max_cnt on cnt.cnt=maxc left join min_cnt on cnt.cnt=min_cnt.minc where maxc is null and minc is null