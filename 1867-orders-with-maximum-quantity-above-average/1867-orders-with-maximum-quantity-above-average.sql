# Write your MySQL query statement below
select order_id
from ordersdetails
group by order_id
having max(quantity) > all (select avg(quantity) from ordersdetails group by order_id)