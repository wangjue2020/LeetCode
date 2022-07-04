# Write your MySQL query statement below
select product_name, product_id, order_id, order_date
from
(select p.product_name, p.product_id, o.order_id, o.order_date, dense_rank() over (partition by p.product_id order by o.order_date desc) as row_num from products p left join orders o using(product_id)) tmp
where row_num=1 and order_id is not null order by product_name asc, product_id asc, order_id asc;