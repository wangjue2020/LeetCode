# Write your MySQL query statement below
with s as (
select distinct spend_date, tmp.platform from spending,(select 'desktop' as platform union select 'mobile' as platform union select 'both' as platform) tmp),
a as
(select spend_date, user_id from spending group by spend_date, user_id having count(distinct platform) = 1),
b as
(select spend_date, user_id from spending group by spend_date, user_id having count(distinct platform) = 2)

# select * from s
select s.spend_date, s.platform, ifnull(total_amount, 0) as total_amount, ifnull(total_users, 0) as total_users
from s left join (select spend_date, platform, sum(amount) as total_amount, count(distinct user_id) as total_users
from a left join spending using(spend_date, user_id) group by spend_date, platform
union
select spend_date, 'both' as platform, sum(amount) as total_amount, count(distinct user_id) as total_users
from b left join spending using(spend_date, user_id) group by spend_date) res using(spend_date, platform)