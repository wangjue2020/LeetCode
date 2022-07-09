# Write your MySQL query statement below
with fri as
(select * from friendship
union
select user2_id as user1_id, user1_id as user2_id from friendship)

select  f.*, count(*) as common_friend
from friendship f left join fri f1 on f.user1_id = f1.user1_id and f.user2_id <> f1.user2_id left join fri f2 on f.user2_id = f2.user1_id and f.user1_id <> f2.user2_id
where f1.user2_id = f2.user2_id group by f.user1_id, f.user2_id having count(*) >= 3;