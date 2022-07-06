# Write your MySQL query statement below
select distinct transaction_id from (select transaction_id, dense_rank()over(partition by date(day) order by amount desc) as ra from transactions order by day) tmp where ra=1 order by transaction_id asc;

# select transaction_id, date(day), dense_rank()over(partition by date(day) order by amount desc) as ra from transactions order by substring(day, 1,8)