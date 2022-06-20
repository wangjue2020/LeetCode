# Write your MySQL query statement below
select person1, person2, count(*) as call_count, sum(duration) as total_duration
from (select (case when from_id < to_id then from_id else to_id end ) as person1, 
(case when from_id>to_id then from_id else to_id end ) as person2, duration
from calls) new
group by person1, person2;