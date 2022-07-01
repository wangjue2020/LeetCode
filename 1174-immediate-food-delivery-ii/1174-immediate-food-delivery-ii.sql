# Write your MySQL query statement below
select round((sum(immediate) / count(*))*100,2 ) as immediate_percentage
# select sum(immediate), count
from (select case when  delivery.order_date = customer_pref_delivery_date then 1 else 0 end as immediate
from delivery join (select customer_id, min(order_date) as order_date from delivery group by customer_id) tmp using(customer_id, order_date)) t