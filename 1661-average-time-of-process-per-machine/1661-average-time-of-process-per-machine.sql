# Write your MySQL query statement below
select machine_id, round(avg(end_time-start_time),3) as processing_time from
(select machine_id, process_id, timestamp as start_time from activity where activity_type = 'start') s join (select machine_id, process_id, timestamp as end_time from activity where activity_type = 'end') e using(machine_id, process_id)
group by machine_id