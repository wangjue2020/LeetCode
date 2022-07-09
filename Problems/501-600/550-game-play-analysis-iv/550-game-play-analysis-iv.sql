# Write your MySQL query statement below
select round((select count(*) as cnt from (select player_id, min(event_date) as register from activity group by player_id) fl join activity a on fl.player_id = a.player_id and fl.register!=a.event_date
where datediff(a.event_date, fl.register) = 1)
/ (select count(distinct player_id) from activity ),2) as fraction