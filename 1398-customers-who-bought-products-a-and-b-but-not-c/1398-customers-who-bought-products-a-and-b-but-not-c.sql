# Write your MySQL query statement below
select tmp.*, customer_name from (select customer_id from orders where product_name in ('A', 'B') group by customer_id having count(distinct product_name) = 2) tmp join customers using(customer_id)

where customer_id not in (select customer_id from orders where product_name in ('A', 'B','C') group by customer_id having count(distinct product_name) = 3)


