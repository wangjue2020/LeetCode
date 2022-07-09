# Write your MySQL query statement below
select seller_id
from sales
group by seller_id
having sum(price) = (select sum(price) as total
from sales
group by seller_id
order by total desc limit 1)