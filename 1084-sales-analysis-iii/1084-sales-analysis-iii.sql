# Write your MySQL query statement below
select s.product_id, p.product_name
from sales s join product p on s.product_id=p.product_id
group by s.product_id
having max(s.sale_date)<=date("2019-03-31") and min(s.sale_date)>=date("2019-01-01")
