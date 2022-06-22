# Write your MySQL query statement below
select product_name, sale_date, count(sale_id)  as total from
(select lower(trim(product_name)) as product_name, substring(sale_date, 1,7) as sale_date, sale_id from sales 
# group by product_name, substring(sale_date, 1,7)
) tmp
group by product_name, sale_date
order by product_name asc, sale_date asc
