# Write your MySQL query statement below
select ids.product_id, ifnull(new_price, 10) as price
from
(select distinct product_id from products) ids

left join

(select p.product_id, p.new_price
from products p join 
(select product_id, max(change_date) as change_date
from products
where change_date <= date('2019-08-16')
group by product_id) max_date on p.change_date = max_date.change_date and p.product_id = max_date.product_id) prices on ids.product_id = prices.product_id