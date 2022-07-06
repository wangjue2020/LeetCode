# Write your MySQL query statement below
select distinct c1.user_id from confirmations c1, confirmations c2 where c1.user_id = c2.user_id and timestampdiff(second, c1.time_stamp, c2.time_stamp) between 0 and 86400 and c1.time_stamp <> c2.time_stamp