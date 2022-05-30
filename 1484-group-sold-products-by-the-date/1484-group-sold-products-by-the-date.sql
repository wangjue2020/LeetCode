# Write your MySQL query statement below
select sell_date, count(distinct product) as num_sold, GROUP_CONCAT(distinct product order by product) as products 
from Activities
group by sell_date
order by sell_date;

# select sell_date, count(distinct product) as num_sold,  group_concat(distinct product order by product) AS products
# from Activities
# group by sell_date
# order by sell_date
