# Write your MySQL query statement below
select product.product_id, sum(quantity) as total_quantity
from sales  join product using(product_id)
group by product.product_id