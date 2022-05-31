# Write your MySQL query statement below
select user_id, max(time_stamp) as last_stamp
from Logins
where time_stamp < date("2021-01-01")
group by user_id
having max(time_stamp)>=date("2020-01-01");