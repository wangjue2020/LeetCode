# Write your MySQL query statement below
# select tmp1.team_id, 
# (select *, dense_rank()over(order by points desc, name asc) as ori_rank from teampoints) tmp1 join
# (select t1.team_id, name, dense_rank()over(order by points_change+points desc, name asc) as ne_rank from teamPoints t1 left join pointschange p using(team_id)) tmp2 using(team_id, name)

with a as (select 
t.team_id,
t.name,
t.points,
case when p.points_change is null then 0 else p.points_change end as points_change,
case when p.points_change is null then t.points else t.points + p.points_change end as new_points
from TeamPoints t
left join PointsChange p
on t.team_id = p.team_id)

, b as (select a.*, 
 rank() over (ORDER BY new_points DESC, a.name ASC) as new_rank,
 rank() over (ORDER BY a.points DESC, a.name ASC) as old_rank
from a)

select b.team_id,
b.name,
#new_rank,
#old_rank,
cast(old_rank as signed) - cast(new_rank as signed) as rank_diff
from b