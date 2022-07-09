# Write your MySQL query statement below
select name as warehouse_name, sum(units*(width*length*height)) as volume from warehouse left join products using(product_id) group by name