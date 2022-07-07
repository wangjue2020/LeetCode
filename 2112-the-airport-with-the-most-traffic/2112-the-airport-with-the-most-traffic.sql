# Write your MySQL query statement below
with a as
(select departure_airport as airport_id, flights_count as num from flights 
union all
select arrival_airport as airport_id, flights_count as num from flights)

select airport_id
from a
group by airport_id
having sum(num) = (select sum(num) from a group by airport_id order by sum(num) desc limit 1);
