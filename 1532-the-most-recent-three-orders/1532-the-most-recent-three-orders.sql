# Write your MySQL query statement below
select name as customer_name, customer_id, order_id, order_date
from
(select * , ROW_NUMBER() OVER(PARTITION BY cu.customer_id ORDER BY ord.order_date desc)  as row_num from customers cu left join orders ord using(customer_id) ) tmp 
where row_num <=3  and order_id is not null 
order by customer_name asc, customer_id asc, order_date desc;