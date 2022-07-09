# Write your MySQL query statement below
select s1.product_id, tmp.year as first_year, s1.quantity, s1.price
from sales s1 join
(select product_id, min(year) as year from sales group by product_id) tmp using(product_id, year)
