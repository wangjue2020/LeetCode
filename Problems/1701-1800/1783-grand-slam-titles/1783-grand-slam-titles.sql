# Write your MySQL query statement below
select player_id, player_name, ifnull(w,0) + ifnull(u,0) + ifnull(f,0) + ifnull(a,0) as grand_slams_count
from
players p left join
(select wimbledon as player_id, count(wimbledon) as w from championships group by wimbledon
) w using(player_id)
left join (select fr_open as player_id, count(fr_open) as f from championships group by fr_open) f using(player_id)
left join (select US_open as player_id, count(US_open) as u from championships group by US_open) u using(player_id)
left join (select Au_open as player_id, count(Au_open) as a from championships group by Au_open) a using(player_id)
where w is not null or f is not null or u is not null or a is not null;