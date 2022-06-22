# Write your MySQL query statement below
# select ifnull(round(avg(times),2),0) as average_sessions_per_user
# from (select count(*) as times
# from activity
# where datediff(date('2019-07-27'), activity_date ) between 0 and 30 and activity_type not in ('open_session', 'end_session')
# group by user_id) tmp

# select user_id, count(*) as times
# from activity
# where datediff(date('2019-07-27'), activity_date ) between 0 and 30 and activity_type not in ('open_session', 'end_session')
# group by user_id
# order by user_id



select coalesce(round(count(distinct session_id)/ count(distinct user_id),2) ,0.00)
average_sessions_per_user
from Activity
where activity_date between date_add('2019-07-27', interval -29 day) and '2019-07-27'