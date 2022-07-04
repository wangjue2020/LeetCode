# Write your MySQL query statement below
select customer_id, product_id, product_name
from
(select customer_id, product_id, product_name, count(order_id), dense_rank() over(partition by customer_id order by count(order_id) desc) as ra from orders o left join products using(product_id) group by customer_id, product_id) tmp
where ra = 1;