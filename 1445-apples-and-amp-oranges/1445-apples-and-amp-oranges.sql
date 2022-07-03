# Write your MySQL query statement below
with apple as(select sale_date, sold_num as sold_num_a from sales where fruit = 'apples'),
orange as (select sale_date, sold_num as sold_num_o from sales where fruit = 'oranges'),
merged as 
(select sale_date, sold_num_a, ifnull(sold_num_o,0) as sold_num_o
from apple left join orange using(sale_date)
union 
select sale_date, ifnull(sold_num_a,0) as sold_num_a, sold_num_o
from apple right join orange using(sale_date))
select sale_date, sold_num_a-sold_num_o as diff from merged order by sale_date