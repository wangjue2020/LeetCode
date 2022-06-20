# Write your MySQL query statement below
select b.bus_id, count(bt.passenger_id) as passengers_cnt
from
(select p.passenger_id, min(b.arrival_time) as bus_t
from passengers p, buses b 
where p.arrival_time <= b.arrival_time
group by p.passenger_id) bt right join buses b on bt.bus_t = b.arrival_time
group by b.bus_id
order by b.bus_id