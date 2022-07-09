# Write your MySQL query statement below
select follower, num_follower as num
from (select followee, count(follower) as num_follower from follow group by followee
) ee join (select follower, count(followee) as num_followee from follow group by follower) er on ee.followee = er.follower
order by follower