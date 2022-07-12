# Write your MySQL query statement below
select u.user_id as seller_id, ifnull(case when item_brand=favorite_brand then 'yes' else 'no' end, 'no') as 2nd_item_fav_brand
from
users u left join 
(select * from (select item_id, seller_id, row_number()over(partition by seller_id order by order_date asc) as rn from orders) t2 where rn=2) t1 on u.user_id=t1.seller_id
left join items i on t1.item_id=i.item_id