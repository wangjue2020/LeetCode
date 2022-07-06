# Write your MySQL query statement below
select user1_id, user2_id
from
(select r1.user_id as user1_id, r2.user_id as user2_id, dense_rank() over(order by count(*) desc) as ra
from relations r1 join relations r2 on r1.user_id < r2.user_id and r1.follower_id = r2.follower_id group by r1.user_id, r2.user_id) t
where ra=1;