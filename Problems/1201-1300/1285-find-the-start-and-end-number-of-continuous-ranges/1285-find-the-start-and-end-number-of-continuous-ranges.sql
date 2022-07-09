# Write your MySQL query statement below


select min(log_id) as start_id, max(log_id) as end_id
from 
(select log_id, log_id-rank() over (order by log_id) gid from logs
) t
group by gid
order by start_id;
