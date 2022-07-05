# Write your MySQL query statement below
select p.product_id, p1.price as store1, p2.price as store2, p3.price as store3
from 
(select distinct product_id from products) p
left join (select * from products where store='store1') p1 using(product_id)
left join (select * from products where store='store2') p2 using(product_id)
left join (select * from products where store='store3') p3 using(product_id)