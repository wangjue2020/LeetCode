# Write your MySQL query statement below
# select distinct page_id as recommended_page
# from (select case when user1_id = 1 then user2_id else user1_id end as friends
# from friendship where user1_id = 1 or user2_id = 1) fri left join likes on fri.friends = likes.user_id
# where page_id not in (select page_id from likes where user_id=1);

select distinct page_id as recommended_page
from (select case when user1_id = 1 then user2_id else user1_id end as friends
from friendship where user1_id = 1 or user2_id = 1) fri left join likes on fri.friends = likes.user_id
where page_id not in (select page_id from likes where user_id=1) and page_id is not null