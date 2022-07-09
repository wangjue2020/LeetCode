# Write your MySQL query statement below
select s.user_id, ifnull(round(confirmed,2), 0) as confirmation_rate
from signups s left join 
(select user_id, sum((case action when "confirmed" then 1 else 0 end)) / count(*) as confirmed from confirmations 
group by user_id) confirm_rate on s.user_id = confirm_rate.user_id