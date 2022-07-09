# Write your MySQL query statement below
# select action_date, count(*) from actions where action="report" and extra="spam" group by action_date

select round(avg(percent)*100,2) as average_daily_percent 
from (select a.action_date, count(distinct r.post_id)/ count(distinct a.post_id) as percent from actions a left join removals r on a.post_id = r.post_id where action="report" and extra='spam' group by a.action_date) a


# select a.action_date, count(r.post_id)/ count(*) as percent from actions a left join removals r on a.post_id = r.post_id where action="report" and extra='spam' group by a.action_date


# select round(sum(daily_percent)/count(daily_percent)*100,2)
# as average_daily_percent from

# (select count(distinct r.post_id)/count(distinct a.post_id) as daily_percent from
# Actions a left join Removals r using(post_id)
# where action = 'report'
# and extra = 'spam'
# group by action_date) sq1