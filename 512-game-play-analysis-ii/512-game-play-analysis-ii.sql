# Write your MySQL query statement below
select ac.player_id , device_id
from activity ac join (select player_id, min(event_date) as first from activity group by player_id) a on ac.player_id=a.player_id
where ac.event_date = a.first;