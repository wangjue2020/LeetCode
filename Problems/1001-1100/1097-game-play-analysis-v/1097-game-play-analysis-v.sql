# Write your MySQL query statement below
with first_login as (select player_id, min(event_date) as login_date from activity group by player_id)

# select *
# from activity a left join activity a1 using(player_id) right join first_login using (player_id) where datediff(a1.event_date, a.event_date) =1 and a.event_date = login_date
# group by a.event_date

select login_date as install_dt, count(*) as installs, round(count(a1.player_id) / count(a.player_id),2) as Day1_retention
from first_login f left join activity a on f.player_id=a.player_id and f.login_date=a.event_date 
left join activity a1 on f.player_id=a1.player_id and datediff(a1.event_date, a.event_date) = 1 group by f.login_date