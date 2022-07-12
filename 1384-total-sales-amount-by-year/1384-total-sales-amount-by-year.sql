# Write your MySQL query statement below
with a as
(select product_id,
case when period_start > date("2018-12-31") then null else period_start end as s_2018, 

case when period_start > date("2018-12-31") then null when period_end <= date("2018-12-31") then period_end else date("2018-12-31") end as e_2018, 
 
case when period_start >date('2019-12-31') or period_end < date('2019-01-01') then null when period_start < date("2019-01-01") then date("2019-01-01") else period_start end as s_2019,


case when period_start >date('2019-12-31') or period_end < date('2019-01-01') then null when period_end <= date("2019-12-31") then period_end else date("2019-12-31") end as e_2019,

case when period_end <date('2020-01-01') then null when period_start < date('2020-01-01') then date('2020-01-01') else period_start end as s_2020, 

case when period_end < date('2020-01-01') then null else period_end end as e_2020,
 period_start,period_end,average_daily_sales

from sales),

sales1 as
(select product_id, datediff(e_2018, s_2018)+1  as days_2018, datediff(e_2019,s_2019)+1 as days_2019, datediff(e_2020, s_2020)+1 as days_2020,  period_start,period_end,average_daily_sales from a)

select convert(product_id,CHAR) as product_id, product_name, '2019' as report_year, days_2019*average_daily_sales as total_amount from product join sales1 using(product_id) where days_2019 is not null
union
select convert(product_id,CHAR) as product_id, product_name, '2020' as report_year, days_2020*average_daily_sales as total_amount from product join sales1 using(product_id) where days_2020 is not null
union
select convert(product_id,CHAR) as product_id, product_name, '2018' as report_year, days_2018*average_daily_sales as total_amount from product join sales1 using(product_id) where days_2018 is not null
order by product_id, report_year
