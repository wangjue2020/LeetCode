# Write your MySQL query statement below
select * from orders where customer_id in (select customer_id from orders group by customer_id having count(distinct order_type) > 1) and order_type = 0
union
select * from orders where customer_id in (select customer_id from orders group by customer_id having count(distinct order_type) = 1)