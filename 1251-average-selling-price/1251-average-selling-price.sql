# Write your MySQL query statement below
select u.product_id, round(sum(u.units * p.price) / sum(u.units), 2) as average_price from unitssold u join prices p using(product_id)
where u.purchase_date between p.start_date and p.end_date
group by u.product_id