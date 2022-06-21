# Write your MySQL query statement below
select customer_id, name
from (select o.customer_id, c.name, extract(month from order_date) as month, sum(o.quantity * p.price) as cost
from orders o left join product p on o.product_id = p.product_id left join customers c on c.customer_id = o.customer_id
where extract(year from order_date) = 2020 and extract(month from order_date) in (6,7)
group by o.customer_id, extract(month from order_date)) result
where cost >= 100
group by customer_id
having count(*) > 1

