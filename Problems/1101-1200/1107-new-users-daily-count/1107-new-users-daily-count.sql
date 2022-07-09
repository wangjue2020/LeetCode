# Write your MySQL query statement below
with tmp as 
(select user_id, min(activity_date) as login_date from traffic where activity = 'login' group by user_id)

select login_date, count(user_id) as user_count
from tmp
where datediff(date('2019-06-30'),login_date) between 0 and 90
group by login_date
order by login_date