# Write your MySQL query statement below
select ifnull(round(count(distinct session_id) / count(distinct user_id),2),0) as average_sessions_per_user
from activity
where datediff(date('2019-07-27'), activity_date) between 0 and 29