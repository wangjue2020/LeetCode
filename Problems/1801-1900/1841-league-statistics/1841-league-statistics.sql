# Write your MySQL query statement below
select team_name, count(*) as matches_played, sum(points) as points, sum(goal_for) as goal_for, sum(goal_agians) as goal_against, sum(goal_for) - sum(goal_agians) as goal_diff
from
(select home_team_id as team_id, home_team_goals as goal_for, away_team_goals as goal_agians, home_points as points
from (select *, (case when home_team_goals > away_team_goals then 3 
          when home_team_goals = away_team_goals then 1
          else 0
          end) as home_points,
 (case when home_team_goals < away_team_goals then 3 
          when home_team_goals = away_team_goals then 1
          else 0
          end) as away_points
from matches) new_matches

union all

select away_team_id as team_id, away_team_goals as goal_for, home_team_goals as goal_agians, away_points as points
from (select *, (case when home_team_goals > away_team_goals then 3 
          when home_team_goals = away_team_goals then 1
          else 0
          end) as home_points,
 (case when home_team_goals < away_team_goals then 3 
          when home_team_goals = away_team_goals then 1
          else 0
          end) as away_points
from matches) new_matches) new join teams on new.team_id = teams.team_id
group by new.team_id
order by points desc, goal_diff desc, teams.team_name
