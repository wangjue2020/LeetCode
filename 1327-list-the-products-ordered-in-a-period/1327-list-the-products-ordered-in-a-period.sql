# Write your MySQL query statement below
select product_name, sum(unit) as unit
from orders join products using(product_id)
where substring(order_date, 1,7)='2020-02'
group by orders.product_id
having sum(unit) >= 100;