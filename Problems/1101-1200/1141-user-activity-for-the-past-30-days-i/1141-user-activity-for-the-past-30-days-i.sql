# Write your MySQL query statement below

# Write an SQL query to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.

select activity_date as day, count(distinct user_id) as active_users
from Activity a 
where DATEDIFF(date('2019-07-27'), a.activity_date) < 30 
group by activity_date
