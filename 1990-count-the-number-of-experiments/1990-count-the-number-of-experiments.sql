# Write your MySQL query statement below
with a as 
(select 'Reading' as experiment_name
union 
select 'Sports' as experiment_name
union
select 'Programming' as experiment_name),
b as 
(select 'IOS' as platform
union 
select 'Android' as platform
union
select 'Web' as platform)

select b.platform, a.experiment_name, count(e.experiment_id) as num_experiments
from b join a left join experiments e on b.platform=e.platform and a.experiment_name = e.experiment_name
group by b.platform, a.experiment_name;