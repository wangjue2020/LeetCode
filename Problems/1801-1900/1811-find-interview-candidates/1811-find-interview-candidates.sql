# Write your MySQL query statement below
select distinct u.name, u.mail
from users u, contests c1, contests c2, contests c3
where c2.contest_id - c1.contest_id = 1 and c3.contest_id - c2.contest_id = 1 and (u.user_id=c1.gold_medal or u.user_id=c1.silver_medal or u.user_id = c1.bronze_medal) and (u.user_id=c2.gold_medal or u.user_id=c2.silver_medal or u.user_id = c2.bronze_medal) and (u.user_id=c3.gold_medal or u.user_id=c3.silver_medal or u.user_id = c3.bronze_medal)

union

select u.name, u.mail
from users u, contests c
where u.user_id = c.gold_medal
group by u.user_id
having count(c.contest_id) >= 3