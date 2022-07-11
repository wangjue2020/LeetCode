# Write your MySQL query statement below
with scores as (select first_player as player, first_score as score from matches union all select second_player as player, second_score as score from matches)

select group_id, player_id 
from (select group_id, player_id, row_number()over(partition by group_id order by total_score desc, player_id asc) as rn
from players left join 
(select player, sum(score) as total_score from scores group by player) t on t.player = players.player_id) t1 where rn=1;

