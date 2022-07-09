# Write your MySQL query statement below
with tmp as (select product_id, count(order_id) as cnt, extract(year from purchase_date) as year from orders group by product_id, year)

select distinct t1.product_id from tmp t1 left join tmp t2 using(product_id) where t1.year+1 = t2.year and t1.cnt >= 3 and t2.cnt >= 3;

# select * from tmp order by product_id, year