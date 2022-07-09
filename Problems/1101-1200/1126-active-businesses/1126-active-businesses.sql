# Write your MySQL query statement below
select business_id
from events left join
(select event_type, avg(occurences) as average_activity from events group by event_type) tmp using(event_type)
where occurences > average_activity
group by business_id
having count(distinct event_type) >=2