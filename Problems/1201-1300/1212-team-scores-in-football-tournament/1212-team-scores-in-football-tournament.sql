# Write your MySQL query statement below
select t.team_id, t.team_name, sum(ifnull(points,0)) as num_points
from teams t left join 
(select host_team as team_id, case when host_goals > guest_goals then 3 when host_goals = guest_goals then 1 else 0 end as points from matches
union all
select guest_team as team_id, case when guest_goals > host_goals then 3 when guest_goals = host_goals then 1 else 0 end as points from matches) m  using(team_id)
group by t.team_id
order by num_points desc, t.team_id asc;