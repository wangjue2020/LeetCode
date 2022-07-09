# Write your MySQL query statement below
select user_id, product_id from
(select user_id, product_id, dense_rank() over(partition by user_id order by sum(quantity*price) desc) as ro from sales left join product using(product_id) group by user_id, product_id) tmp
where ro = 1 ;

# select user_id, product_id, dense_rank() over(partition by user_id order by sum(quantity*price) desc) as ro from sales left join product using(product_id) group by user_id, product_id